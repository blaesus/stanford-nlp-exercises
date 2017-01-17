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

    def __init__(self, text: str, max_n: int=3):
        tokens, vocabulary = analyse_text(text)
        self.vocabulary = vocabulary
        self.max_n = max_n

        for n in range(1, max_n+1):
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

        # Build up probabilities of initial tokens, for example, for trigram,
        # prob(<START>, 'this')
        # when length of conditional tokens is less than N
        for k in range(1, self.n-1):
            preceding_tokens = tokens[:k]
            last_token = tokens[k]
            print('tokens:', ' '.join(preceding_tokens), last_token)

            freq_all = 0
            freq_conditional = 0
            for key in self.frequency_table:
                if key[:k] == preceding_tokens:
                    item_freq = sum(self.frequency_table[key].values())
                    freq_all += item_freq
                    if key[k] == last_token:
                        freq_conditional += item_freq
            p_initial = freq_conditional / freq_all
            print('p = ', p_initial)
            p *= p_initial

        # Compound probability of tokens following the initial tokens
        while index + self.n < len(tokens) + 1:
            preceding_tokens = tokens[index:index+self.n-1]
            last_token = tokens[index+self.n-1]
            print('tokens:', ' '.join(preceding_tokens), last_token)
            p *= conditional_prob(last_token, preceding_tokens)
            print('p = ', conditional_prob(last_token, preceding_tokens))
            index += 1
        return p

    def shannon(self, initial_tokens: Tuple[str], length=10) -> Tuple[str]:

        assert(len(initial_tokens) >= self.n - 1)

        result = initial_tokens
        preceding = initial_tokens[-self.n+1:]

        while len(result) < length:
            candidate_freq = self.frequency_table[preceding]
            most_likely_next_word = max(candidate_freq, key=candidate_freq.get)
            result += (most_likely_next_word,)
            preceding = preceding[1:] + (most_likely_next_word,)

        return result


class Laplace_Language_Model(MLE_Language_Model):

    def __init__(self, text: str, n: int=3, delta=1):
        self.n = n
        self.delta = delta
        self.frequency_table = Frequency_Table(text, n)

        # Smoothing
        d = self.delta
        vocabulary = self.frequency_table.vocabulary
        preceding_word_combinations = permutations(vocabulary, n-1)
        for preceding_words in preceding_word_combinations:
            for last_word in vocabulary:
                try:
                    self.frequency_table[preceding_words][last_word] += d
                except KeyError:
                    self.frequency_table[preceding_words][last_word] = d


if __name__ == '__main__':
    text = open('./lincoln.txt').read()
    lm_mle = MLE_Language_Model(text, n=4)
    # print(lm_mle.predict(('am', 'i', 'but', 'three', 'years')))
    print(lm_mle.shannon(('united', 'states', 'is')))

    # lm_laplace = Laplace_Language_Model(text, n=2)
    # print(lm_laplace.predict(('am', 'i', 'but', 'three', 'years')))
