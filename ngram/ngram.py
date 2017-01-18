from typing import Tuple, List, Dict, Callable
from collections import Counter
from itertools import permutations

Tokens = List[str]
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


class ML_Language_Model(object):

    def __init__(self, text: str, n: int=3):
        self.frequency_table = Frequency_Table(text, n)
        self.n = n

    def prob(self, token: str, conditioning_tokens: Tuple[str]) -> float:
        ft = self.frequency_table
        try:
            return ft.count(conditioning_tokens + (token,)) / ft.count(conditioning_tokens)
        except ZeroDivisionError:
            return 0.0

    def predict(self, sentence: Tuple[str]) -> float:
        p = 1.0
        for i in range(1, len(sentence)):
            token = sentence[i]
            preceding_tokens = sentence[max(i-self.n+1, 0):i]
            p *= self.prob(token, preceding_tokens)
        return p


if __name__ == '__main__':
    text = open('./lincoln.txt').read() + open('./churchill.txt').read()
    # text = open('./mini.txt').read()
    ml = ML_Language_Model(text, 3)
    print(ml.predict(('<start>', 'this', 'is', 'the', 'war', 'of', 'the')))
