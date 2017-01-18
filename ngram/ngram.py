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

    def count_tokens_of_frequency(self, frequency: int, n=None) -> int:
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


class Language_Model(object):

    def __init__(self):
        pass

    def predict(self, sentence: Tuple[str]) -> float:
        pass


if __name__ == '__main__':
    # text = open('./lincoln.txt').read() + open('./churchill.txt').read()
    text = open('./mini.txt').read()
    # lm_mle = MLE_Language_Model(text, n=4)
    # print(lm_mle.predict(('am', 'i', 'but', 'three', 'years')))
    # print(lm_mle.shannon(('united', 'states', 'is')))

    # lm_laplace = Laplace_Language_Model(text, n=2)
    # print(lm_laplace.predict(('am', 'i', 'but', 'three', 'years')))

    ft = Frequency_Table(text)
    print(ft.count(('this',)))
