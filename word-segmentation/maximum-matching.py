"""
  Chinese word segmentation with maximum matching algorithm.
"""

from typing import Tuple

f = open('zh-simp-wordlist.txt', 'r')
words = [line.split('\t')[0] for line in f.read().split('\n')]


def cut(s: str) -> Tuple[str]:
    segs = []
    seg_start = 0
    seg_length = 1

    while seg_start + seg_length < len(s) + 1:
        candidate = s[seg_start:seg_start + seg_length]
        next_candidate = s[seg_start:seg_start + seg_length + 1]

        is_max_matching = (next_candidate not in words) or \
                          (seg_start + seg_length == len(s))  # Last word
        if is_max_matching:
            segs.append(candidate)
            seg_start += seg_length
            seg_length = 1
        else:
            seg_length += 1

    return segs

test_data = [
    '小明硕士毕业于中国科学院计算所，后在日本京都大学深造',
    '我翻开历史一查这历史没有年代歪歪斜斜的每页上都写着仁义道德几个字我横竖睡不着仔细看了半夜才从字缝里看出字来满本都写着两个字是吃人',
    '',
    'What the hell'
]

for sentence in test_data:
    print(sentence, '\n', cut(sentence))
