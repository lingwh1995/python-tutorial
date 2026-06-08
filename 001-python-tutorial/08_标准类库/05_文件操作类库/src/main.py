# -*- coding: utf-8 -*-
"""
@author think
@desc python 中的文件操作类库
@date 2026/6/8 17:46
"""

import os


def os_lib_test() :
    # 获取当前工作目录
    wd = os.getcwd()
    print(wd)
    # 列出文件夹所有文件
    dirs = os.listdir("./")
    print(dirs)
    # 新建文件夹
    # os.mkdir("test")
    # 判断文件是否存在
    exist = os.path.exists("a.txt")
    print(exist)


if __name__ == "__main__":
    os_lib_test()
