# -*- coding: utf-8 -*-
"""python 中的字符串下标

:author: lingwh
:date: 2026/7/1 14:02
"""

# 定义字符串的几种方式
a = '12345'
b = "12345"
c = '''12345'''
d = """12345"""

# 字符串的下标,使用下标访问字符串中每一个字符
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
# 打印不存在的字串会报错,IndexError: string index out of ranget):
# print(a[5])