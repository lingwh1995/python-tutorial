# -*- coding: utf-8 -*-
"""python 中的列表定义

1. 定义列表的几种方式
2. 列表是可变序列，可以直接修改内部元素；字符串不可变，二者核心区别

:author: lingwh
:date: 2026/7/27 18:18
"""


# 定义列表的几种方式
list_single = ['1', '2', '3', '4', '5']             # 元素使用单引号
list_double = ["1", "2", "3", "4", "5"]             # 元素使用双引号
list_multi_line = [                                 # 多行书写列表（类比三引号字符串）
    '1',
    '2',
    '3',
    '4',
    '5'
]
list_by_constructor = list('12345')                 # list()构造器创建列表
list_empty_literal = []                             # 字面量方式创建空列表
list_empty_constructor = list()                     # list()构造器创建空列表
list_comprehension = [str(i) for i in range(1, 6)]  # 列表推导式生成列表
list_concat = ['1'] + ['2', '3', '4', '5']          # 通过拼接运算生成新列表
list_unpack = [*'12345']                            # 解包可迭代对象生成列表

print(f"list_single = {list_single}")
print(f"list_double = {list_double}")
print(f"list_multi_line = {list_multi_line}")
print(f"list_by_constructor = {list_by_constructor}")
print(f"list_empty_literal = {list_empty_literal}")
print(f"list_empty_constructor = {list_empty_constructor}")
print(f"list_comprehension = {list_comprehension}")
print(f"list_concat = {list_concat}")
print(f"list_unpack = {list_unpack}")
