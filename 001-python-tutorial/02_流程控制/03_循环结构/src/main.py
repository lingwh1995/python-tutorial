# -*- coding: utf-8 -*-
"""python 中的循环结构

一、循环结构

循环结构基础
1. for 循环结构 - 适用于循环次数已知
2. while 循环结构 - 适用于循环次数未知

循环结构高级
1. 列表推导式（List Comprehensions）
     列表推导式是 Python 中一种非常强大且优雅的生成列表的方式。它允许使用简短的语法根据现有的可迭代对象创建一个新的列表，通常可以用一行代码替
     代多行的for 循环。列表推导式不仅代码简洁，而且在 Python 内部是通过 C 语言优化的，执行速度通常比等价的 for 循环更快。
2. 生成器表达式（Generator Expressions）
     生成器表达式是列表推导式的惰性求值版本。它在语法上与列表推导式非常相似，唯一的区别在于它使用圆括号 () 而非方括号 []。生成器表达式不会立即
     生成一个包含所有结果的列表，而是返回一个生成器（generator）对象，该对象会根据需要逐个地产生结果。这种惰性计算的特性使得生成器表达式在处理
     大规模数据或无限序列时非常有用，因为它可以显著节省内存，常与 sum()、max()、min() 等配合使用。
3. 内置函数
     Python 提供了许多内置函数（如 sum()、max()、all()、any() 等），它们由 C 语言实现，通常比手写的 for 循环更高效。在可能的情况下，应优先
     使用这些内置函数或标准库工具（如 itertools 模块）来替代显式循环，以减少解释器开销。

二、流程控制完整体系（三大结构协作实现完整程序逻辑）

1. 顺序结构 - 负责提供默认执行线
2. 分支结构 - 负责条件选择路径
3. 循环结构 - 负责重复执行代码

三、循环控制跳转语句
     break - 终止循环
     continue - 跳过本次循环

:author: lingwh
:date: 2026/6/15 10:43
"""

import time
import psutil
import os


def get_rss_mb() -> None:
    pid = os.getpid()
    mem = psutil.Process(pid).memory_info().rss
    return round(mem / 1024 / 1024, 2)


"""
    循环结构基础
"""
# 1. for 循环结构
# 遍历列表
fruits = ['苹果', '香蕉', '橘子']
for fruit in fruits:
    print(fruit)
print('-' * 20)

# 遍历字符串
for char in 'Python':
    print(char)
print('-' * 20)

# 使用 range() - [0, 5)
for i in range(5):
    print(i)

# 使用 range() - [2, 10)，步长为3
# range(stop)              - 生成从 0 到 stop-1 的整数
# range(start, stop)       - 生成从 start 到 stop-1 的整数
# range(start, stop, step) - 生成从 start 到 stop-1，步长为 step 的整数
for i in range(2, 10, 3):
    print(i)
print('-' * 20)

# 打印99乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}×{i}={i*j}\t", end="")
    print()  # 每行结束换行

# 遍历字典
student = {'name': '张三', 'age': 20, 'score': 90}

# 遍历字典 - 遍历键
for key in student.keys():
    print(key)

# 遍历字典 - 遍历值
for value in student.values():
    print(value)

# 遍历字典 - 遍历键值对（最常用）
for key, value in student.items():
    print(f'{key}: {value}')
print('-' * 20)

# enumerate - 同时获取索引和值
for index, fruit in enumerate(fruits):
    print(f'{index} - {fruit}')
print('-' * 20)

# zip - 并行遍历多个列表（遍历轮数由元素个数最少的列表决定）
names = ['Alice', 'Bob', 'Candy']
scores = [90, 85, 68]
for name, score in zip(names, scores):
    print(f'{name} 的分数是 {score}')
print('-' * 20)

# for-else 子句
nums = [2,4,6,8]
target = 5

for num in nums:
    if num == target:
        print(f"找到数字{target}")
        break
else:
    print(f"列表里没有{target}")
print('-' * 20)


# 2. while 循环结构
# 求1到100的和
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print("1到100的和:", total)
print('-' * 20)

# 验证用户输入的密码
# password = "123456"
# user_input = ""
# while user_input != password:
#     user_input = input("请输入密码: ")
# print("密码正确，程序继续。")
# print('-' * 20)

# 死循环
# while 1:
#     print("死循环")
# while True:
#     print("死循环")

# while循环 性能优化
# 不推荐：每次循环都计算列表长度
data = [1, 2, 3, 4, 5]
i = 0
while i < len(data):
    print(data[i], end='\t')
    i += 1
print()

# 推荐：预先计算长度
data = [1, 2, 3, 4, 5]
n = len(data)
i = 0
while i < n:
    print(data[i], end='\t')
    i += 1
print()
print('-' * 20)

# 使用 while 模拟 do-while 循环结构
# while True:
#     # do-while核心：先执行一次（至少显示1次菜单给用户）
#     print("\n" + "-"*30)
#     print("📚 学生管理系统 v1.0")
#     print("-"*30)
#     print("1. 新增学生信息")
#     print("2. 查询学生成绩")
#     print("3. 退出系统")
#     print("-"*30)
#     choice = input("请输入你的选择（1-3）：")
#
#     # 执行业务逻辑
#     match choice:
#         case '1':
#             print("\n  进入 [新增学生信息] 模块...")
#             break
#         case '2':
#             print("\n 进入 [查询学生成绩] 模块...")
#             break
#         case "3":
#             print("\n 退出系统，欢迎下次使用！")
#             break
#         case _:
#             print("\n 输入错误，请输入1-3之间的选项！")

# 3. break 和 continue
for i in range(5):
    print(i, end='\t')
    if i == 2:
        break
print()

for i in range(5):
    print(i, end='\t')
    if i == 2:
        continue
print()

print('-' * 20)
"""
    循环结构高级
"""
# 1. 列表推导式（List Comprehensions）
# 不使用列表推导式
squares = []
for x in range(10):
    squares.append(x*x)
print(squares)

# 使用列表推导式
squares = [x*x for x in range(10)]
print(squares)
even_squares = [x*x for x in range(10) if x % 2 == 0]
print(even_squares)

# 嵌套循环推导
combinations = [m+n for m in ['A', 'B', 'C'] for n in ['X', 'Y', 'Z']]
print(combinations)

# 字典推导
nums = [1, 2, 3, 4, 5]
square_dict = {num: num*num for num in nums}
print(square_dict)

# 解包推导
points = [(1, 2), (3, 4), (5, 6)]
sums = [x + y for x, y in points]
print(sums)

# 选取大于5的奇数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [x for x in numbers if x > 5 and x % 2 != 0]
print(result)

# 生成前10个Fibonacci数
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print(fib)
print('-' * 20)


# 2. 生成器表达式（Generator Expressions）
# 前置采样
print('列表推导式 与 生成器表达式 开始前置采样......')
mem_before = get_rss_mb()
t_start = time.perf_counter()

# 列表推导式
sum_of_squares = sum([x*x for x in range(1, 1000000)])
# 生成器表达式
#sum_of_squares = sum(x*x for x in range(1, 1000000))
print(sum_of_squares)

# 后置采样
print('列表推导式 与 生成器表达式 开始后置采样......')
t_end = time.perf_counter()
mem_after = get_rss_mb()

# 统计结果
print('列表推导式 与 生成器表达式 开始统计结果......')
print(f'运行时长：{t_end - t_start:.2f} s')
print(f'运行前内存：{mem_before} MB')
print(f'运行后内存：{mem_after} MB')
print(f'内存增加：{mem_after - mem_before} MB')
print('-' * 20)


# 3. 内置函数
nums = [1, 2, 3, 4, 5]
# 手动求和
total = 0
for num in nums:
    total += num
# 使用内置 sum() 更高效
total = sum(nums)
print(total)

# 手动求最大值
max_val = 0
for num in nums:
    if num > max_val:
        max_val = num
# 使用内置 max() 更高效
max_val = max(nums)
print(max_val)