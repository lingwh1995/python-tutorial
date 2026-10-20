# -*- coding: utf-8 -*-
"""python 中的字符串基础遍历

:author: lingwh
:date: 2026/7/1 14:02
"""


def foreach_str_1(source: str) -> None:
    """遍历字符串

    for-in 遍历
    """
    for i in source:
        print(i)
    print('-' * 20)


def foreach_str_2(source: str) -> None:
    """遍历字符串

    for-in + range() + len() 遍历
    """
    for i in range(len(source)):
        print(source[i])
    print('-' * 20)


def foreach_str_3(source: str) -> None:
    """遍历字符串

    while + len() 遍历
    """
    i = 0
    while i < len(source):
        print(source[i])
        i += 1
    print('-' * 20)


if __name__ == '__main__':
    s = '12345'
    foreach_str_1(s)
    foreach_str_2(s)
    foreach_str_3(s)