# -*- coding: utf-8 -*-
"""python 中的字符串算法

:author: lingwh
:date: 2026/7/1 17:17
"""


def reversed_by_slice(source: str) -> str:
    """切片写法
    最推荐使用，最简洁、最快

    :param source: 待反转的字符串
    :return: 反转后的新字符串
    """
    return source[::-1]


def reversed_by_join(source: str) -> str:
    """列表拼接写法
    可读性好，适合教学，避免切片魔术语法

    :param source: 待反转的字符串
    :return: 反转后的新字符串
    """
    return "".join(reversed(source))


def reversed_by_loop(source: str) -> str:
    """循环写法
    可读性好，使用 append() 构建字符列表

    :param source: 待反转的字符串
    :return: 反转后的新字符串
    """
    chars = []
    for i in range(len(source) - 1, -1, -1):
        chars.append(source[i])
    return "".join(chars)


if __name__ == '__main__':
    s = '12345'
    print(reversed_by_slice(s))
    print(reversed_by_join(s))
    print(reversed_by_loop(s))
    print('-' * 3)