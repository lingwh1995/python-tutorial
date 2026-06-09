# -*- coding: utf-8 -*-
"""
@author think
@desc python 中的正则表达式类库
@date 2026/6/9 10:52
"""

import re


def re_lib_test() :
    # 提取数字 ['123','45']
    res = re.findall(r"\d+", "abc123def45")
    print(res)

    # 替换 → bbb
    s = 'aaa'
    re.sub("a", "b", s)
    print(s)


if __name__ == "__main__":
    re_lib_test()




