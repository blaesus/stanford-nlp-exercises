"""
    Stemmer with Porter's Algorithm, as specified in
        http://snowball.tartarus.org/algorithms/porter/stemmer.html

    Most functions expect lowercase input.
"""

from typing import Tuple, List
import re
from rule_sets import rule_sets


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


def apply(s: str, rule) -> Tuple[str, bool]:
    search_string = rule[6].lower()
    search_regex = re.escape(search_string) + r'$'
    replacement = rule[7].lower()
    stem_candidate = re.sub(search_regex, '', s)

    m = get_m(stem_candidate)
    if (rule[0] is not None) and (m <= rule[0]):
        return s, False

    if rule[2]:
        should_proceed = False
        for letter in rule[2]:
            print('checking', stem_candidate, 'ends with', letter)
            if stem_candidate.endswith(letter.lower()):
                should_proceed = True
        if not should_proceed:
            return s, False

    if rule[3] and not has_vowel(stem_candidate):
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
    s = apply_first_applicable_rule(s, rule_sets['3'])
    s = apply_first_applicable_rule(s, rule_sets['4'])
    return s
