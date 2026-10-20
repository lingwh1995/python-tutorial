# -*- coding: utf-8 -*-
"""python 中的列表基础遍历

:author: lingwh
:date: 2026/8/17 22:03
"""


def foreach_list_1(source: list) -> None:
    """遍历列表
    for-in 遍历
    """
    for value in source:
        print(value)
    print('-' * 20)


def foreach_list_2(source: list) -> None:
    """遍历列表
    for-in + range() + len() 遍历
    注意： range(len(lst)) 这里只计算一次
    """
    for i in range(len(source)):
        print(source[i])
    print('-' * 20)


def foreach_list_3(source: list) -> None:
    """遍历列表
    while + len() 遍历
    """
    length = len(source)
    i = 0
    while i < length:
        print(source[i])
        i += 1
    print('-' * 20)


def foreach_list_4(source: list) -> None:
    """遍历列表
    for-in + enumerate() 遍历，同时获取下标和元素
    """
    for index, value in enumerate(source):
        print(f'下标: {index}, 元素值: {value}')
    print('-' * 20)


if __name__ == '__main__':
    chars = ['a', 'b', 'c', 'd', 'e']
    foreach_list_1(chars)
    foreach_list_2(chars)
    foreach_list_3(chars)
    foreach_list_4(chars)
