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


class Frequency_Table(Dict[Tuple, Dict[str, float]]):

    def __init__(self, text: str, n: int=3):
        tokens, vocabulary = analyse_text(text)

        for i in range(0, len(tokens) - n):
            preceding_words = tokens[i:i+n-1]
            last_word = tokens[i+n-1]
            try:
                self[preceding_words][last_word] += 1
            except KeyError:
                self[preceding_words][last_word] = 1

    def __missing__(self, key):
        value = self[key] = dict()
        return value

    def normalize(self) -> None:
        for preceding_word_tuple in self:
            freq_sum = sum(self[preceding_word_tuple].values())
            for last_word in self[preceding_word_tuple]:
                self[preceding_word_tuple][last_word] /= freq_sum


class MLE_Language_Model(object):

    def __init__(self, text: str, n: int=3):
        self.frequency_table = Frequency_Table(text, n)
        self.n = n

    def predict(self, tokens: Tuple[str]) -> float:

        def conditional_prob(last_token: str, preceding_tokens: Tuple[str]) -> float:
            marginal_frequencies = self.frequency_table[preceding_tokens]
            try:
                return marginal_frequencies[last_token] / sum(marginal_frequencies.values())
            except KeyError:
                return 0

        p = 1.0
        index = 0
        tokens = (START_TOKEN,) + tokens

        # Probability of initial tokens, say prob(<START>, 'this') for trigram
        for k in range(1, self.n-1):
            preceding_tokens = tokens[:k]
            last_token = tokens[k]
            print('k', preceding_tokens, last_token)

        # Compound probability of tokens following the initial tokens
        while index + self.n < len(tokens) + 1:
            preceding_tokens = tokens[index:index+self.n-1]
            last_token = tokens[index+self.n-1]
            print(preceding_tokens, last_token)
            p *= conditional_prob(last_token, preceding_tokens)
            print(conditional_prob(last_token, preceding_tokens))
            index += 1
        return p

    def shannon(self, initial_tokens: Tuple[str], length=10) -> Tuple[str]:

        result = initial_tokens
        preceding = initial_tokens

        while length > 0:
            candidate_freq = self.frequency_table[preceding]
            most_likely_next_word = max(candidate_freq, key=candidate_freq.get)
            result = result + (most_likely_next_word,)
            preceding = preceding[1:] + (most_likely_next_word,)
            length -= 1

        return result

if __name__ == '__main__':
    text = open('./shakespeare.txt').read()
    lm = MLE_Language_Model(text, n=4)
    print(lm.predict(('am', 'i', 'but', 'three', 'inches')))
    # print(lm.shannon(('if', 'you')))
