# -*- coding: utf-8 -*-
"""
@author think
@desc python 中的时间休眠类库
@date 2026/6/9 10:56
"""

import time


def time_lib_test() :
    # 时间戳
    timestamp = time.time()
    print(timestamp)
    # 暂停2秒
    time.sleep(2)
    print('hello')


if __name__ == "__main__":
    time_lib_test()