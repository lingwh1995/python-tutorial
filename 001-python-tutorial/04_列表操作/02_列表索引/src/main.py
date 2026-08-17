# -*- coding: utf-8 -*-
"""python 中的列表索引

python 中的列表索引分为正向索引和逆向索引
正向索引：从左往右（从前往后），编号从 0 开始
逆向索引：从右往左（从后往前），编号从 -1 开始（这是 python 独有）

:author: lingwh
:date: 2026/8/17 22:03
"""

# 定义列表的几种方式
a = [1, 2, 3, 4, 5]
b = list('12345')
c = [i for i in range(1, 6)]
d = [0] * 5

# 列表的索引,使用下标访问列表中每一个元素
print(a[0])
print(a[1])
print(a[2])
print('-' * 20)
print(a[-1])
print(a[-2])
print(a[-3])
# 打印不存在的元素会报错， IndexError: list index out of range
# print(a[5])
