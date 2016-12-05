from typing import List


def is_vowel(char: str, previous_char: str = '') -> bool:
    vowels = 'aeiou'
    return (char in vowels) or (char == 'y' and previous_char not in vowels)


def get_vc_list(word: str) -> List[str]:
    chars = list(word)
    for index, char in reversed(list(enumerate(chars))):
        if index == 0:
            previous_char = ''
        else:
            previous_char = chars[index-1]
        if is_vowel(char, previous_char):
            chars[index] = 'v'
        else:
            chars[index] = 'c'
    return chars


def get_m(word: str) -> int:
    vc_list = get_vc_list(word)
    while vc_list and vc_list[0] == 'c':
        del vc_list[0]
    while vc_list and vc_list[-1] == 'v':
        del vc_list[-1]
    if vc_list:
        return ''.join(vc_list).count('cv') + 1
    else:
        return 0

print(get_m('trees'))

rules = [
    # (min_m,
    #  ends_with_letters,
    #  contains_vowel,
    #  ends_with_double_consonant,
    #  ends_with_cvc,
    #  search_string,
    #  replacement
    # )
    ()
]


def apply(s: str, rule) -> str:
    pass


def stem(s: str) -> str:
    for rule in rules:
        s = apply(s, rule)
    return s

FULL = 0
STEM = 1

# test_data = [
#     ('', ''),
#     ('12345', '12345'),
#     ('hello', 'hello'),
#     ('morning', 'morning'),
#     ('communism', 'commune'),
#     ('relationship', 'relation'),
# ]
#
# for datum in test_data:
#     word = datum[FULL]
#     true_stem = datum[STEM]
#     print(word, true_stem, 'Correct' if stem(word) == true_stem else 'X')
