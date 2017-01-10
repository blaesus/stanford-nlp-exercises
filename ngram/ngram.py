from typing import Tuple, List, Dict, Callable

Vocabulary = List[str]
Tokens = List[str]

Frequency_Table = Dict[Tuple, Dict[str, float]]


def analyse_text(text: str) -> Tuple[Vocabulary, Tokens]:
    pass


def get_frequency_table(text: str) -> Frequency_Table:
    pass


def laplace_smooth(table: Frequency_Table) -> Frequency_Table:
    pass


def get_language_model(text: str, n: int=3) -> Callable[Tokens, float]:
    pass

if __name__ == '__main__':
    text = open('./shakespeare.txt').read()
    lm = get_language_model(text)
