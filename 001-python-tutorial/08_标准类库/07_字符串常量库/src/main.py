# -*- coding: utf-8 -*-
"""
@author think
@desc python 中的字符串常量库
@date 2026/6/9 10:49
"""

import string


def string_lib_test() :
    # 大小写英文字母常量
    ascii_letters = string.ascii_letters
    print(ascii_letters)
    # 数字0-9常量
    digits = string.digits
    print(digits)
    # 所有标点符号常量
    punctuation = string.punctuation
    print(punctuation)


if __name__ == "__main__":
    string_lib_test()




