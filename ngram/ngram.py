from typing import Tuple, List, Dict, Callable
from collections import Counter
from itertools import permutations

Tokens = Tuple[str]
Vocabulary = List[str]
START_TOKEN = '<start>'


def clean(text: str) -> str:
    replace_table = (
        (',', ' '),
        ('.', ' '+START_TOKEN),
        (';', ' '),
        (':', ' '),
        ('-', ' '),
        ('"', ' '),
        ("'", ' '),
        ('?', ' '+START_TOKEN),
        ('!', ' '+START_TOKEN),
    )
    result = text.lower()
    for pair in replace_table:
        result = result.replace(pair[0], pair[1])
    return result


def analyse_text(text: str) -> Tuple[Tokens, Vocabulary]:
    tokens = tuple(clean(text).split())
    vocabulary = list(set(tokens))
    return tokens, vocabulary


class Frequency_Table(Dict[str, float]):

    def __init__(self, text: str, max_n: int=3):
        tokens, vocabulary = analyse_text(text)
        self.vocabulary = vocabulary
        self.max_n = max_n
        self.freq_cache = {}

        for n in range(1, max_n+1):
            for i in range(len(tokens) - n + 1):
                word_tuple = tokens[i:i+n]
                try:
                    self[word_tuple] += 1
                except KeyError:
                    self[word_tuple] = 1

    def count(self, tokens: Tuple[str]) -> int:
        try:
            return self[tokens]
        except KeyError:
            return 0

    def count_tokens_of_frequency(self, frequency: int, n: int=None) -> int:
        try:
            return self.freq_cache[(frequency, n)]
        except KeyError:
            if n is None:
                n = self.max_n

            count = 0
            for key in self:
                if len(key) == n and self[key] == frequency:
                    print('found:', key)
                    count += 1

            self.freq_cache[(frequency, n)] = count
            return count

    def subdict_key_starting_with(self, tokens: Tokens) -> Dict:
        result = {}
        l = len(tokens)
        for key in self:
            if key[:l] == tokens:
                result[key] = self[key]
        return result


class ML_Language_Model(object):

    def __init__(self, text: str, n: int=3):
        self.frequency_table = Frequency_Table(text, n)
        self.n = n

    def calc_cond_prob(self, tokens: Tokens, conditioning_tokens: Tokens) -> float:
        ft = self.frequency_table
        conditioning_tokens = conditioning_tokens[-self.n+1:]  # Markov property
        return ft.count(conditioning_tokens + tokens) / ft.count(conditioning_tokens)

    def predict(self, tokens: Tokens, conditioning_tokens: Tokens = ()) -> float:

        if tokens == (START_TOKEN,):
            # All sentences should start with `<start>`
            assert len(conditioning_tokens) == 0
            p = 1

        elif len(tokens) == 1:
            p = self.calc_cond_prob(tokens, conditioning_tokens)
            # print('calculating', 'P(', ','.join(tokens), '|', ','.join(conditioning_tokens), ')')
            # print('p =', p)
        else:
            # Chain rule of conditional probabilty
            # P(cde|Sab) = P(cd|Sab) * P(e|Sabcd)
            prior_prob = self.predict(tokens[:-1], conditioning_tokens)
            if prior_prob == 0:  # Lazy evaluation to shortcircuit operation below
                p = 0
            else:
                conditional_prob = self.predict(tokens[-1:], conditioning_tokens + tokens[:-1])
                p = prior_prob * conditional_prob

        return p


if __name__ == '__main__':
    # text = open('./lincoln.txt').read() + open('./churchill.txt').read()
    text = open('./mini.txt').read()
    lm = ML_Language_Model(text, 3)
    print(lm.predict(('<start>', 'a', 'text', 'corpus', 'is')))
    print(lm.predict(('c', 'd'), (START_TOKEN, 'a', 'b')))
    print(lm.predict(('<start>', 'a', 'x', 'corpus', 'is')))
    print(lm.predict((START_TOKEN, 'a', 'b', 'c', 'd', 'e')))
    # print(lm.predict(('<start>', 'this', 'is', 'the', 'war', 'of', 'the'))
