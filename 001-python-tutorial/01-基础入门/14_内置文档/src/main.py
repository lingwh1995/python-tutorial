# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的文档支持/pydoc
@date 2026/6/15 9:39

python 内置文档

1. 在命令行中进行查看
     查看内置模块
       python -m pydoc math / pydoc math
     查看自己脚本
       python -m pydoc test / pydoc test
     查看指定函数
       python -m pydoc math.sqrt / pydoc math.sqrt
2. 启动本地网页文档服务器
     随机端口启动
       python -m pydoc -b / pydoc -b
     指定端口启动
       python -m pydoc -p 8888 / pydoc -p 8888
3. 生成静态 HTML 文件
     为 test.py 生成 test.html
       python -m pydoc -w test pydoc -w test
     批量生成当前目录所有py文件html
       python -m pydoc -w . / pydoc -w .
"""

import pydoc
import math


# 完整写法
#pydoc.help(math)
pydoc.help(math.sqrt)
print('-' * 20)

# 简单写法
#help(math)
pydoc.help(math.sqrt)
print('-' * 20)

# 使用pydoc支持的格式进行注释 - 单行注释
def add(a, b):
    """两数相加"""
    return a + b


# 使用pydoc支持的格式进行注释 - 多行注释
def calc_area(radius):
    """计算圆形面积

    :param radius: 圆半径
    :type radius: float
    :return: 面积值
    :rtype: float
    """
    import math
    return math.pi * radius ** 2


# 使用 pydoc 查看自定义函数的文档 - 完整写法
pydoc.help(add)
pydoc.help(calc_area)
print('-' * 20)

# 使用 pydoc 查看自定义函数的文档 - 简单写法
help(add)
help(calc_area)
