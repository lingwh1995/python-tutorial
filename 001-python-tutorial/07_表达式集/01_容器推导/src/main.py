# -*- coding: utf-8 -*-
"""python 中的容器推导式

1. 支持的容器
   python 的推导式支持下面容器：
   列表推导式：[expr for i in iter]
   集合推导式：{expr for i in iter}
   字典推导式：{k:v for ...}
2. 语法格式（以列表为例）
   # 基础语法
   [expr for i in iter]

   res = []
   for i in iter:
       res.append(expr)

   # 使用条件筛选结果作为列表元素
   [expr for i in iter if condition]

   res = []
   for i in iter:
       if condition:
           res.append(expr)

   # 使用三目运算结果作为列表元素
   [expr1 if condition else expr2 for i in iter]

   res = []
   for i in iter:
       if condition:
           val = expr1
       else:
           val = expr2
       res.append(val)
3. 注意事项
   - 容器推导式的表达式 expr 支持三目运算
   - 容器推导式是一次生成列表中所有的元素并把所有元素放在内存中，海量数据时占用巨大内存，甚至内存溢出、程序卡死

@author lingwh
@date 2026/10/26 10:12
"""


# 1.列表推导 [] list
# 基本格式
nums = [x for x in range(5)]
print(nums)
# 使用条件筛选结果作为列表元素
even_nums = [x for x in range(5) if x % 2 == 0]
print(even_nums)
# 使用表达式计算结果作为列表元素
squares = [x * x for x in range(5)]
print(squares)
# 使用三目运算结果作为列表元素
nums = [f'{x}-偶' if x % 2 == 0 else f'{x}-奇' for x in range(5)]
print(nums)
print('---')

# 2. 集合推导式 {} set
nums = [0, 1, 2, 2, 3, 3, 3, 4]
# 基本格式
nums = {x for x in nums}
print(nums)
# 使用条件筛选结果作为集合元素
even_nums = {x for x in nums if x % 2 == 0}
print(even_nums)
# 使用表达式计算结果作为集合元素
squares = {x * x for x in nums}
print(squares)
# 使用三目运算结果作为集合元素
nums = {f'{x}-偶' if x % 2 == 0 else f'{x}-奇' for x in nums}
print(nums)
print('---')

# 3. 字典推导式 {key: value} dict
# 基本格式
square_dict = {x: x * x for x in range(5)}
print(square_dict)
# 使用条件筛选结果作为字典元素的值
even_dict = {x: x * x for x in range(5) if x % 2 == 0}
print(even_dict)
# 使用表达式计算结果作为字典元素的值
even_value_dict = {x: (x % 2 == 0) for x in range(5)}
print(even_value_dict)
# 使用三目运算结果作为字典元素的值
num_dict = {x: '偶' if x % 2 == 0 else '奇' for x in range(5)}
print(num_dict)
# 交换变量
origin_dict = {"a": 1, "b": 2}
swap_dict = {v: k for k, v in origin_dict.items()}
print(swap_dict)