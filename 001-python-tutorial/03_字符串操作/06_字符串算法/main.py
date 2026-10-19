# -*- coding: utf-8 -*-
"""python 中的字符串算法

:author: lingwh
:date: 2026/7/1 17:17
"""


def reverse_best(source: str) -> str:
    """切片写法
    推荐使用，最简洁、最快

    :param source: 待反转的字符串
    :return: 反转后的新字符串
    """
    return source[::-1]

def reverse_join(source: str) -> str:
    """列表拼接写法
    可读性好，适合教学，避免切片魔术语法

    :param source: 待反转的字符串
    :return: 反转后的新字符串
    """
    return "".join(reversed(source))

def reverse_loop(source: str) -> str:
    """循环写法
    可读性好，使用 append() 构建字符列表

    :param source: 待反转的字符串
    :return: 反转后的新字符串
    """
    chars = []
    for i in range(len(source) - 1, -1, -1):
        chars.append(source[i])
    return "".join(chars)

def print_even_index_char(source: str) -> None:
    """打印偶数索引的字符

    :param source: 原始字符串
    """
    for i in range(0, len(source), 2):
        print(source[i])

def validate_suffix(file_name: str, suffix: str) -> bool:
    """判断文件名是否以指定后缀结尾

    :param file_name: 完整文件名（如 'hello.txt'）
    :param suffix: 文件扩展名（如 '.txt' 或 'txt'）
    :return: 文件以指定后缀结尾返回 True，否则 False
    """
    file_name_part = file_name.split('.')
    return len(file_name_part) > 1 and file_name_part[-1] == suffix.lstrip('.')

if __name__ == '__main__':
    s = '12345'
    filename = 'a.txt'

    reversed_s = reverse_best(s)
    print(reversed_s)

    reversed_s = reverse_join(s)
    print(reversed_s)

    reversed_s = reverse_loop(s)
    print(reversed_s)

    print_even_index_char(s)

    is_match = validate_suffix(filename, '.txt')
    print(is_match)