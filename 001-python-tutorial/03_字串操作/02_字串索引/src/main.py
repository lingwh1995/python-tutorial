# -*- coding: utf-8 -*-
"""python 中的字符串索引

python 中的字符串索引分为正向索引和逆向索引
正向索引：从左往右（从前往后），编号从 0 开始
逆向索引：从右往左（从后往前），编号从 -1 开始（这是 python 独有）

:author: lingwh
:date: 2026/7/1 14:02
"""

# 定义字符串的几种方式
s1 = '12345'
s2 = "12345"
s3 = '''12345'''
s4 = """12345"""

# 字符串的索引,使用下标访问字符串中每一个字符
print(s1[0])
print(s1[1])
print(s1[2])
print('-' * 20)
print(s1[-1])
print(s1[-2])
print(s1[-3])
# 打印不存在的字串会报错， IndexError: string index out of ranget:
# print(s1[5])
