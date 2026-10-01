# -*- coding: utf-8 -*-
"""python 中的列表定义

1. 定义列表的几种方式
2. 列表定义的格式
   格式1: 列表名 = [值1, 值2, 值3...]
   格式2: 列表名 = lst()
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
lst_single = ['1', '2', '3', '4', '5']                 # 元素使用单引号
lst_double = ["1", "2", "3", "4", "5"]                 # 元素使用双引号
lst_int_literal = [1, 2, 3, 4, 5]                      # 整数元素字面量
lst_multi_data_type = [10, 20.3, True, 'abc']          # 列表中存放多种不同类型的数据
lst_multi_line = [                                     # 多行书写列表（类比三引号字符串）
    '1',
    '2',
    '3',
    '4',
    '5'
]
lst_empty_constructor = lst()                          # lst()构造器创建空列表
lst_empty_literal = []                                 # 字面量方式创建空列表，是 lst() 的语法糖
lst_by_constructor_1 = lst('12345')                    # lst()构造器创建列表（列表中每个元素为字符串）
lst_by_constructor_2 = lst(range(5))                   # lst()构造器创建列表（列表中每个元素为整数）
lst_comprehension_int = [i for i in range(1, 6)]       # 列表推导式生成列表
lst_comprehension_str = [str(i) for i in range(1, 6)]  # 列表推导式生成列表
lst_concat = ['1'] + ['2', '3', '4', '5']              # 通过拼接运算生成新列表
lst_repeat = [0] * 5                                   # 通过重复运算生成新列表
lst_unpack = [*'12345']                                # 解包可迭代对象生成列表

print(f"lst_single = {lst_single}")
print(f"lst_double = {lst_double}")
print(f"lst_int_literal = {lst_int_literal}")
print(f"lst_multi_data_type = {lst_multi_data_type}")
print(f"lst_multi_line = {lst_multi_line}")
print(f"lst_empty_constructor = {lst_empty_constructor}")
print(f"lst_empty_literal = {lst_empty_literal}")
print(f"lst_by_constructor_1 = {lst_by_constructor_1}")
print(f"lst_by_constructor_2 = {lst_by_constructor_2}")
print(f"lst_comprehension_int = {lst_comprehension_int}")
print(f"lst_comprehension_str = {lst_comprehension_str}")
print(f"lst_concat = {lst_concat}")
print(f"lst_repeat = {lst_repeat}")
print(f"lst_unpack = {lst_unpack}")