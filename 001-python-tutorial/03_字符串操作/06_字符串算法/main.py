# -*- coding: utf-8 -*-
"""python 中的字符串算法

:author: lingwh
:date: 2026/7/1 17:17
"""


def reverse_best(s: str) -> str:
    """切片写法

    推荐使用，最简洁、最快
    :param s: 待反转的字符串
    :return: 反转后的新字符串
    """
    return s[::-1]


def reverse_join(s: str) -> str:
    """列表拼接写法

    可读性好，适合教学，避免切片魔术语法
    :param s: 待反转的字符串
    :return: 反转后的新字符串
    """
    return "".join(reversed(s))


def reverse_loop(s: str) -> str:
    """循环写法

    可读性好，最好用 append() 替代 +=
    :param s: 待反转的字符串
    :return: 反转后的新字符串
    """
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return "".join(chars)


def print_even_index_char(s: str) -> None:
    """打印偶数索引的字符

    :param s: 原始字符串
    """
    for i in range(0, len(s), 2):
        print(s[i])


def validate_suffix(file_name: str, suffix: str) -> bool:
    """判断文件是否以指定后缀结尾

    :param file_name: 完整文件名（如 'hello.txt'）
    :param suffix: 文件扩展名（如 '.txt' 或 'txt'）
    :return: 文件以指定后缀结尾返回 True，否则 False
    """
    file_name_part = file_name.split('.')
    return len(file_name_part) > 1 and file_name_part[-1] == suffix.lstrip('.')


if __name__ == '__main__':
    s = '12345'
    file_name = 'a.txt'
    s_reverse = reverse_best(s)
    print(s_reverse)
    s_reverse = reverse_join(s)
    print(s_reverse)
    s_reverse = reverse_loop(s)
    print(s_reverse)
    print_even_index_char(s)
    validate_result = validate_suffix(file_name, ".txt")
    print(validate_result)