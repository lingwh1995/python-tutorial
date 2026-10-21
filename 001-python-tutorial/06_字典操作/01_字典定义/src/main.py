# -*- coding: utf-8 -*-
"""python 中字典的定义

1. 字典定义的格式
   格式1: 字典名 = {键1: 值1, 键2: 值2, ...}
   格式2: 字典名 = {}
   格式3: 字典名 = dict()
2. 字典进阶
   - 字典是键值对的集合，通过「键」存取数据，而不是索引
   - 键必须是不可变类型（字符串、数字、元组等），且不能重复，键重复时后面的值会覆盖前面的值
   - 值可以是任意类型，且允许重复
   - python 3.7 之后，字典会保留键值对的插入顺序
3. 字典与列表的区别
   列表通过索引访问元素，字典通过键访问元素，字典的键唯一且查找效率更高，二者都是可变类型，核心区别在于「存取方式」不同
   

@author lingwh
@date 2026/10/21 17:23
"""


# 定义字典的几种方式
dict_str_key = {'name': 'Tom', 'age': 18}                  # 键为字符串
dict_int_key = {1: 'a', 2: 'b'}                            # 键为整数
dict_tuple_key = {(0, 0): '原点', (1, 1): 'A点'}            # 键为元组（只有不可变类型才能作键）
dict_multi_value_type = {'name': 'Tom', 'age': 18, 'scores': [90, 80]}  # 值可以是多种不同类型
dict_multi_line = {                                        # 多行书写字典
    'name': 'Tom',
    'age': 18,
}
dict_empty_constructor = dict()                  # dict()构造器创建空字典
dict_empty_literal = {}                                    # 字面量方式创建空字典，是 dict() 的语法糖
dict_by_constructor_1 = dict(name='Tom', age=18)           # dict()构造器（关键字参数方式，键为字符串）
dict_by_constructor_2 = dict([('name', 'Tom'), ('age', 18)])  # dict()构造器（键值对可迭代对象方式）
dict_by_zip = dict(zip(['name', 'age'], ['Tom', 18]))      # dict() + zip() 组合生成字典
dict_comprehension = {i: i * i for i in range(1, 6)}       # 字典推导式生成字典
dict_fromkeys = dict.fromkeys(['a', 'b', 'c'], 0)          # fromkeys() 用相同的值初始化多个键
dict_repeat_key = {'name': 'Tom', 'name': 'Jerry'}         # 键重复时，后面的值覆盖前面的值，实际只保留一个键

print(f"dict_str_key = {dict_str_key}")
print(f"dict_int_key = {dict_int_key}")
print(f"dict_tuple_key = {dict_tuple_key}")
print(f"dict_multi_value_type = {dict_multi_value_type}")
print(f"dict_multi_line = {dict_multi_line}")
print(f"dict_empty_constructor = {dict_empty_constructor}")
print(f"dict_empty_literal = {dict_empty_literal}")
print(f"dict_by_constructor_1 = {dict_by_constructor_1}")
print(f"dict_by_constructor_2 = {dict_by_constructor_2}")
print(f"dict_by_zip = {dict_by_zip}")
print(f"dict_comprehension = {dict_comprehension}")
print(f"dict_fromkeys = {dict_fromkeys}")
print(f"dict_repeat_key = {dict_repeat_key}")

print(type(dict_str_key))
print(type(dict_int_key))
print(type(dict_tuple_key))
print(type(dict_multi_value_type))
