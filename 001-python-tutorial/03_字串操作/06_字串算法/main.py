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


def count_sub_str_by_count(source: str, sub_str: str) -> int:
    """"使用内置的 count() 实现"""
    return source.count(sub_str)


def count_sub_str_by_split(source: str, sub_str: str) -> int:
    """"使用内置的 split() 实现"""
    return len(source.split(sub_str)) - 1


def count_sub_str_by_replace(source: str, sub_str: str) -> int:
    """"使用内置的 replace() 实现"""
    return (len(source) - len(source.replace(sub_str, ''))) // len(sub)


def count_sub_str_by_find_slice_1(source: str, sub_str: str) -> int:
    """使用内置的 find() + slice() 实现"""
    count = 0
    while source.find(sub_str) != -1:
        count += 1
        source = source[source.find(sub_str) + len(sub_str):]
    return count


def count_sub_str_by_find_slice_2(source: str, sub_str: str) -> int:
    """Count substring occurrences with find and string slice.

    Use str.find() to get match position, slice to skip matched content.
    Non‑overlapping matching.

    :param source: Original string for searching
    :param sub_str: Target substring to count
    :return: Number of matched substrings
    """
    count = 0
    pos = source.find(sub_str)
    while pos != -1:
        count += 1
        source = source[pos + len(sub_str):]
        pos = source.find(sub_str)
    return count


if __name__ == '__main__':
    s = '12345'
    print(reversed_by_slice(s))
    print(reversed_by_join(s))
    print(reversed_by_loop(s))
    print('-' * 3)

    print_even_index_char(s)
    print('-' * 3)

    filename = 'a.txt'
    print(validate_suffix(filename, '.txt'))
    print('-' * 3)

    s = 'python is a simple and popular programming language, python can runs on many different operating systems, would you consider using python?'
    sub = 'python'
    print(count_sub_str_by_count(s, sub))
    print(count_sub_str_by_split(s, sub))
    print(count_sub_str_by_replace(s, sub))
    print(count_sub_str_by_find_slice_1(s, sub))
    print(count_sub_str_by_find_slice_2(s, sub))