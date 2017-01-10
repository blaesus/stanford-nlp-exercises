from typing import Tuple, List, Dict, Callable
from collections import Counter

Tokens = List[str]
Vocabulary = List[str]
Frequency_Table = Dict[Tuple, Dict[str, float]]


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
    tokens = clean(text).split()
    vocabulary = list(set(tokens))
    return tokens, vocabulary


def get_frequency_table(text: str, n: int = 3) -> Frequency_Table:
    pass


def laplace_smooth(table: Frequency_Table) -> Frequency_Table:
    pass


def get_language_model(text: str, n: int=3) -> Callable[[Tokens], float]:
    pass

if __name__ == '__main__':
    text = open('./shakespeare.txt').read()
    tokens, vocabulary = analyse_text(text)
    print(tokens[0: 10])
    print(vocabulary[0: 10])
