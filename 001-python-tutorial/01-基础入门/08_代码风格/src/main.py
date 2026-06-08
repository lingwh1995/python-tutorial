# -*- coding: utf-8 -*-
"""
@author think
@desc python 代码风格
@date 2026/6/5 17:57

1. 遵循 python 之禅
     Beautiful is better than ugly.
     Explicit is better than implicit.
     Simple is better than complex.
     Complex is better than complicated.
     Flat is better than nested.
     Sparse is better than dense.
     Readability counts.
     Special cases aren't special enough to break the rules.
     Although practicality beats purity.
     Errors should never pass silently.
     Unless explicitly silenced.
     In the face of ambiguity, refuse the temptation to guess.
     There should be one-- and preferably only one --obvious way to do it.
     Although that way may not be obvious at first unless you're Dutch.
     Now is better than never.
     Although never is often better than *right* now.
     If the implementation is hard to explain, it's a bad idea.
     If the implementation is easy to explain, it may be a good idea.
     Namespaces are one honking great idea -- let's do more of those!
2. 遵循 pythonic 风格，用 python 原生语法，贴近自然英文，少循环少临时变量，代码短、可读性强
"""

import this

print("--------------------------------------------------------------")
# 1. 交换变量
a = 10
b = 20

# 非 Pythonic：引入临时变量
tmp = a
a = b
b = tmp

# Pythonic：直接用元组解包
a, b = b, a
print("a = %d, b = %d" % (a, b))

# 2. 同时获取索引和值
names = ['Alice', 'Bob', 'Charlie']

# 非 Pythonic：手动维护索引
i = 0
while i < len(names):
    print(i, names[i])
    i += 1

# Pythonic：用 enumerate
for i, name in enumerate(names):
    print(i, name)

# 3. 字符串拼接列表
items = ['Python', 'is', 'great']

# 非 Pythonic：循环累加（低效且难看）
s = ""
for item in items:
    s += item + " "

# Pythonic：用 join
s = " ".join(items)

# 4. 文件读取

# 非 Pythonic：手动打开和关闭
f = open('file.txt', 'r')
content = f.read()
f.close()

# Pythonic：使用上下文管理器，自动关闭
with open('file.txt', 'r') as f:
    content = f.read()

# 5. 条件赋值
x = 10
# 非 Pythonic：多行 if-else
if x > 0:
    sign = 'positive'
else:
    sign = 'non-positive'

# Pythonic：一行条件表达式
sign = 'positive' if x > 0 else 'non-positive'

# 6. 检查空容器
items = []

# 非 Pythonic：显式检查长度
if len(items) == 0:
    print("没有数据")

# Pythonic：利用空序列的布尔特性
if not items:
    print("没有数据")

# 7. 多列表同时遍历
a = [1, 2, 3]
b = ['x', 'y', 'z']

# 非 Pythonic：用下标索引
for i in range(len(a)):
    print(a[i], b[i])

# Pythonic：用 zip 打包
for num, ch in zip(a, b):
    print(num, ch)

# 8. 列表推导式代替简单循环
# 非 Pythonic：普通 for 循环
squares = []

for x in range(10):
    if x % 2 == 0:
        squares.append(x*x)

# Pythonic：列表推导式
squares = [x*x for x in range(10) if x % 2 == 0]
print("--------------------------------------------------------------")

