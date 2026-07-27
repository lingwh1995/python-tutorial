# -*- coding: utf-8 -*-
"""python 中的字符串算法

:author: lingwh
:date: 2026/7/1 17:17
"""

s = 'abcde'
file_name = 'a.txt'


# 推荐：切片写法，最简洁、最快
def reverse_best(s) -> None:
    """切片写法，最简洁、最快"""
    return s[::-1]


# 可读性也不错（适合教学，避免切片魔术语法）
def reverse_join(s) -> None:
    """列表拼接写法，可读性好"""
    return "".join(reversed(s))


# 如果一定要用循环，用列表拼接替代 +=
def reverse_loop(s) -> None:
    """循环写法，可读性好"""
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return "".join(chars)


def print_even_index_char(s) -> None:
    """打印偶数索引的字符"""
    for i in range(0, len(s), 2):
        print(s[i])


def validate_suffix(file_name, suffix) -> bool:
    """判断文件是否以指定后缀结尾

    参数:
        file_name: 完整文件名（如 'hello.txt'）
        suffix: 文件扩展名（如 '.txt' 或 'txt'）

    返回:
        True 如果文件以指定后缀结尾，否则 False
    """
    file_name_part = file_name.split('.')
    return len(file_name_part) > 1 and file_name_part[-1] == suffix.lstrip('.')


if __name__ == '__main__':
    s_reverse = reverse_best(s)
    print(s_reverse)
    s_reverse = reverse_join(s)
    print(s_reverse)
    s_reverse = reverse_loop(s)
    print(s_reverse)
    print_even_index_char(s)
    result = validate_suffix(file_name, ".txt")
    print(result)