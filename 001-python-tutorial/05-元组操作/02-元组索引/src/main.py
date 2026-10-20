# -*- coding: utf-8 -*-
""" python 中的元组索引

python 中的元组索引分为正向索引和逆向索引
正向索引：从左往右（从前往后），编号从 0 开始
逆向索引：从右往左（从后往前），编号从 -1 开始（这是 python 独有）
注意：元组是不可变序列，索引只能用于访问元素，不能用于修改元素

@author lingwh
@date 2026/10/20 18:08
"""

# 定义元组的几种方式
t1 = (1, 2, 3, 4, 5)
t2 = tuple('12345')
t3 = tuple(i for i in range(1, 6))
t4 = (0,) * 5   # 注意：单元素元组必须带尾逗号

# 使用索引访问元组中每一个元素
print(t1[0])
print(t1[1])
print(t1[2])
print('-' * 20)
print(t1[-1])
print(t1[-2])
print(t1[-3])
# 打印不存在的元素会报错， IndexError: tuple index out of range
# print(t1[5])
print('-' * 3)

# 使用索引修改元组中的元素会报错，元组是不可变序列
# TypeError: 'tuple' object does not support item assignment
try:
    t1[0] = 10
except TypeError as e:
    print(f'TypeError: {e}')
print('-' * 3)

# 确实需要修改时，先转列表，修改完再转回元组
lst1 = list(t1)
lst1[0] = 10
t1 = tuple(lst1)

# 打印元组
print(t1)
print(t2)
print(t3)
print(t4)
