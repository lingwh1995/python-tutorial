# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的数学类库
@date 2026/6/8 17:32
"""

import math


def math_lib_test() :
    # 圆周率
    print(math.pi)

    # 开平方
    print(math.sqrt(16))

    # 向下取整
    print(math.floor(3.9))

    # 向上取整
    print(math.ceil(3.1))

    # 正弦
    print(math.sin(math.pi / 2))

    # 自然对数
    print(math.log(10))


if __name__ == "__main__":
    math_lib_test()