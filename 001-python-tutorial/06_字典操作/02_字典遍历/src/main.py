# -*- coding: utf-8 -*-
"""python 中字典的遍历

@author lingwh
@date 2026/10/21 17:56
"""

# 定义字典
student = {'name': 'Tom', 'age': 18, 'score': 95.8}

# 遍历字典方式一：获取字典的每个 key，并通过 key 获取 value
for key in student:
    print(key, student[key])
print('-' * 3)

# 遍历字典方式二：获取字典的每个 value
for key in student.keys():
    print(key, student[key])
print('-' * 3)

# 遍历字典方式三：获取字典的每个 value
for value in student.values():
    print(value)
print('-' * 3)

# 遍历字典方式四：获取字典的每个键值对
for item in student.items():
    print(item[0], item[1])
print('-' * 3)

# 遍历字典方式五：获取字典的每个键值对，并直接解包
for key,value in student.items():
    print(key, value)
print('-' * 3)

# 遍历字典方式六：获取字典的每个键值对，并通过 enumerate() 方法获取索引和键值对
for index, item in enumerate(student.items()):
    print(index, item[0], item[1])