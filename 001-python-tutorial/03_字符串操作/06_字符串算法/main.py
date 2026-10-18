# -*- coding: utf-8 -*-
"""python 中的字符串算法

:author: lingwh
:date: 2026/7/1 17:17
"""


def reverse_best(src_str: str) -> str:
    """切片写法
    推荐使用，最简洁、最快

    :param src_str: 待反转的字符串
    :return: 反转后的新字符串
    """
    return src_str[::-1]


def reverse_join(src_str: str) -> str:
    """列表拼接写法
    可读性好，适合教学，避免切片魔术语法

    :param src_str: 待反转的字符串
    :return: 反转后的新字符串
    """
    return "".join(reversed(src_str))


def reverse_loop(src_str: str) -> str:
    """循环写法
    可读性好，最好用 append() 替代 +=

    :param src_str: 待反转的字符串
    :return: 反转后的新字符串
    """
    chars = []
    for i in range(len(src_str) - 1, -1, -1):
        chars.append(src_str[i])
    return "".join(chars)


def print_even_index_char(src_str: str) -> None:
    """打印偶数索引的字符

    :param src_str: 原始字符串
    """
    for i in range(0, len(src_str), 2):
        print(src_str[i])


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
    file_name = 'a.txt'

    s_reverse = reverse_best(s)
    print(s_reverse)

    s_reverse = reverse_join(s)
    print(s_reverse)

    s_reverse = reverse_loop(s)
    print(s_reverse)

    print_even_index_char(s)

    validate_result = validate_suffix(file_name, '.txt')
    print(validate_result)