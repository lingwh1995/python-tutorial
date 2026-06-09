# -*- coding: utf-8 -*-
"""
@author think
@desc python 中的日期事件类库
@date 2026/6/8 17:41
"""

from datetime import datetime,date


def datetime_lib_test() :
    # 当前时间
    now = datetime.now()
    print(now.year, now.month, now.day)
    # 格式化输出
    now_format = now.strftime("%Y-%m-%d %H:%M:%S")
    print(now_format)


if __name__ == "__main__":
    datetime_lib_test()

