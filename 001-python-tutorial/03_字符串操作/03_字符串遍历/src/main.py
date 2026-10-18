# -*- coding: utf-8 -*-
"""python 中的字符串基础遍历

:author: lingwh
:date: 2026/7/1 14:02
"""


s = '12345'
# len()函数
print('字符串 s 的长度: %d' % len(s))


def foreach_str_1() -> None:
    """遍历字符串

    for-in 遍历
    """
    for i in s:
        print(i)
    print('-' * 20)


def foreach_str_2() -> None:
    """遍历字符串

    for-in + range() + len() 遍历
    """
    for i in range(len(s)):
        print(s[i])
    print('-' * 20)


def foreach_str_3() -> None:
    """遍历字符串

    while + len() 遍历
    """
    i = 0
    while i < len(s):
        print(s[i])
        i += 1
    print('-' * 20)


if __name__ == '__main__':
    foreach_str_1()
    foreach_str_2()
    foreach_str_3()