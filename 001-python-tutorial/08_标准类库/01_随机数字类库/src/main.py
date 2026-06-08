# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的随机数类库
@date 2026/6/8 17:32
"""

import random


def random_lib_test() :
    # 使用随机函数生成0-1之间的随机浮点数
    f = random.random()
    print(f)

    # 使用随机函数生成0-9之间的随机整数，左闭右闭，生成的随机整数范围是[0, 9]
    i = random.randint(0, 9)
    print(i)

    # 随机选一个元素
    print(random.choice([1, 2, 3]))

    # 打乱列表
    nums = [1, 2, 3, 4, 5]
    random.shuffle(nums)
    print(nums)


if __name__ == "__main__":
    random_lib_test()