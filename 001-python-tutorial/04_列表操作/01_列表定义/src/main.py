# -*- coding: utf-8 -*-
"""python 中的列表定义

1. 定义列表的几种方式
2. 列表定义的格式
   格式1: 列表名 = [值1, 值2, 值3...]
   格式2: 列表名 = list()
3. 列表进阶
   - 列表可以同时存储多个元素，可以是不同类型的，也可以是同类型的元素
   - 实际开发中，为了方便统一操作，建议: 列表存储的多个元素是同类型
   - 列表的元素也是有索引的，且索引也是从 0(正向), -1(逆向) 开始的,
   - 列表和字符串一样，也是支持 "切片" 操作的，规则都一样: 列表名[起始索引:结束索引:步长]
4. 列表与字符串的区别
   列表是可变序列，可以直接修改内部元素，字符串不可变，二者核心区别

:author: lingwh
:date: 2026/7/27 18:18
"""


# 定义列表的几种方式
list_single = ['1', '2', '3', '4', '5']                 # 元素使用单引号
list_double = ["1", "2", "3", "4", "5"]                 # 元素使用双引号
list_int_literal = [1, 2, 3, 4, 5]                      # 整数元素字面量
list_multi_data_type = [10, 20.3, True, 'abc']          # 列表中存放多种不同类型的数据
list_multi_line = [                                     # 多行书写列表（类比三引号字符串）
    '1',
    '2',
    '3',
    '4',
    '5'
]
list_empty_constructor = list()                         # list()构造器创建空列表
list_empty_literal = []                                 # 字面量方式创建空列表，是 list() 的语法糖
list_by_constructor_1 = list('12345')              # list()构造器创建列表（列表中每个元素为字符串）
list_by_constructor_2 = list(range(5))             # list()构造器创建列表（列表中每个元素为整数）
list_comprehension_int = [i for i in range(1, 6)]       # 列表推导式生成列表
list_comprehension_str = [str(i) for i in range(1, 6)]  # 列表推导式生成列表
list_concat = ['1'] + ['2', '3', '4', '5']              # 通过拼接运算生成新列表
list_repeat = [0] * 5                                   # 通过重复运算生成新列表
list_unpack = [*'12345']                                # 解包可迭代对象生成列表

print(f"list_single = {list_single}")
print(f"list_double = {list_double}")
print(f"list_int_literal = {list_int_literal}")
print(f"list_multi_data_type = {list_multi_data_type}")
print(f"list_multi_line = {list_multi_line}")
print(f"list_empty_constructor = {list_empty_constructor}")
print(f"list_empty_literal = {list_empty_literal}")
print(f"list_by_constructor_1 = {list_by_constructor_1}")
print(f"list_by_constructor_2 = {list_by_constructor_2}")
print(f"list_comprehension_int = {list_comprehension_int}")
print(f"list_comprehension_str = {list_comprehension_str}")
print(f"list_concat = {list_concat}")
print(f"list_repeat = {list_repeat}")
print(f"list_unpack = {list_unpack}")