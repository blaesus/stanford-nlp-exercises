from typing import Tuple, List, Dict, Callable
from collections import Counter
from itertools import permutations

Tokens = List[str]
Vocabulary = List[str]


def clean(text: str) -> str:
    replace_table = (
        (',', ' '),
        ('.', ' '),
        (';', ' '),
        (':', ' '),
        ('-', ' '),
        ('?', ' '),
        ('!', ' ')
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
            last_word = tokens[i+n]
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
        preceding_words = tokens[-1 * self.n:-1]
        last_word = tokens[-1]

        try:
            p1 = self.frequency_table[preceding_words][last_word]
            p2 = sum(self.frequency_table[preceding_words].values())
            return p1 / p2
        except KeyError:
            return 0

if __name__ == '__main__':
    text = open('./shakespeare.txt').read()
    lm = MLE_Language_Model(text)
    print(lm.predict(('this', 'is', 'a',)))
