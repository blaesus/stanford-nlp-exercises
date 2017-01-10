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
            if type(preceding_words) != tuple:
                print(preceding_words)
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


def laplace_smooth(table: Frequency_Table) -> Frequency_Table:
    pass


def get_language_model(text: str, n: int=3) -> Callable[[Tokens], float]:
    pass

if __name__ == '__main__':
    text = open('./shakespeare.txt').read()
    bigram = Frequency_Table(text, 2)
    bigram.normalize()
    print(sum(bigram[('this',)].values()))
