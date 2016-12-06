"""
    Stemmer with Porter's Algorithm, as specified in
        http://snowball.tartarus.org/algorithms/porter/stemmer.html

    Most functions expect lowercase input.
"""

from typing import Tuple, List
import re


def is_vowel(char: str, previous_char: str = '') -> bool:
    vowels = 'aeiou'
    return (char in vowels) or (char == 'y' and previous_char not in vowels)


def has_vowel(s: str) -> bool:
    for char in s:
        if is_vowel(char):
            return True
    return False


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

rule_sets = {
    # rule_set_name: [
    #   (m_lower_bound_exclusive,
    #    ends_with_letters,
    #    stem_contains_vowel,
    #    ends_with_double_consonant,
    #    ends_with_cvc,
    #    search_string,
    #    replacement,
    #   ),
    #   ...
    # ]


    '1a': [
        (None, None, None, None, None, 'SSES', 'SS'),
        (None, None, None, None, None, 'IES',  'I'),
        (None, None, None, None, None, 'SS',   'SS'),
        (None, None, None, None, None, 'S',    ''),
    ],

    '1b': [
        (0,    None, None, None, None, 'EED', 'EE'),
        (None, None, True, None, None, 'ED',  ''),
        (None, None, True, None, None, 'ING', ''),
    ],

    '1c': [
        (None, None, True, None, None, 'Y', 'I'),
    ],

    '2': [
        (0,    None, None, None, None, 'ATIONAL', 'ATE'),
        (0,    None, None, None, None, 'TIONAL', 'TION'),
        (0,    None, None, None, None, 'ENCI', 'ENCE'),
        (0,    None, None, None, None, 'ANCI', 'ANCE'),
        (0,    None, None, None, None, 'IZER', 'IZE'),
        (0,    None, None, None, None, 'ABLI', 'ABLE'),
        (0,    None, None, None, None, 'ALLI', 'AL'),
        (0,    None, None, None, None, 'ENTLI', 'ENT'),
        (0,    None, None, None, None, 'ELI', 'E'),
        (0,    None, None, None, None, 'OUSLI', 'OUS'),
        (0,    None, None, None, None, 'IZATION', 'IZE'),
        (0,    None, None, None, None, 'ATION', 'ATE'),
        (0,    None, None, None, None, 'ATOR', 'ATE'),
        (0,    None, None, None, None, 'ALISM', 'AL'),
        (0,    None, None, None, None, 'IVENESS', 'IVE'),
        (0,    None, None, None, None, 'FULNESS', 'FUL'),
        (0,    None, None, None, None, 'OUSNESS', 'OUS'),
        (0,    None, None, None, None, 'ALITI', 'AL'),
        (0,    None, None, None, None, 'IVITI', 'IVE'),
        (0,    None, None, None, None, 'BILITI', 'BLE'),
    ],
}


def apply(s: str, rule) -> Tuple[str, bool]:
    search_string = rule[5].lower()
    search_regex = re.escape(search_string) + r'$'
    replacement = rule[6].lower()
    stem_candidate = re.sub(search_regex, '', s)

    m = get_m(stem_candidate)
    if (rule[0] is not None) and (m <= rule[0]):
        return s, False

    if rule[2] and not has_vowel(stem_candidate):
        return s, False

    if not re.search(search_regex, s):
        return s, False

    return re.sub(search_regex, replacement, s), True


def apply_first_applicable_rule(s: str, rules: List):
    for rule in rules:
        result, is_rule_applied = apply(s, rule)
        if is_rule_applied:
            return result
    return s


def stem(s: str) -> str:
    s = apply_first_applicable_rule(s, rule_sets['1a'])
    s = apply_first_applicable_rule(s, rule_sets['1b'])
    s = apply_first_applicable_rule(s, rule_sets['1c'])
    s = apply_first_applicable_rule(s, rule_sets['2'])
    return s
