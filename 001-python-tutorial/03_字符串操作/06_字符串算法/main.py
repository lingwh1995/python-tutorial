# -*- coding: utf-8 -*-
"""python 中的字符串算法

:author: lingwh
:date: 2026/7/1 17:17
"""


s = 'abcde'

# 推荐：切片写法，最简洁、最快
def reverse_best(s) -> None:
    return s[::-1]

# 可读性也不错（适合教学，避免切片魔术语法）
def reverse_join(s) -> None:
    return ''.join(reversed(s))

# 如果一定要用循环，用列表拼接替代 +=
def reverse_loop(s) -> None:
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return ''.join(chars)


if __name__ == '__main__':
    s_reverse = reverse_best(s)
    print(s_reverse)
    s_reverse = reverse_join(s)
    print(s_reverse)
    s_reverse = reverse_loop(s)
    print(s_reverse)