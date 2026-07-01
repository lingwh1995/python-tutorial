# -*- coding: utf-8 -*-
"""
@author lingwh
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
3. 遵循 PEP 8 规范
     英文 https://peps.python.org/pep-0008/
     中文 https://peps.pythonlang.cn/pep-0008/
"""


# 1. 交换变量
# 非 Pythonic：引入临时变量
a, b = 10, 20
tmp = a
a = b
b = tmp
print('a = %d, b = %d' % (a, b))

# Pythonic：直接用元组解包
a, b = 10, 20
a, b = b, a
print('a = %d, b = %d' % (a, b))
print('-' * 20)

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
print('-' * 20)

# 3. 字符串拼接列表
items = ['Python', 'is', 'great']
# 非 Pythonic：循环累加（低效且难看）
s = ""
for item in items:
    s += item + " "

# Pythonic：用 join
s = " ".join(items)
print('-' * 20)

# 4. 文件读取
# 非 Pythonic：手动打开和关闭
f = open('file.txt', 'r')
content = f.read()
f.close()

# Pythonic：使用上下文管理器，自动关闭
with open('file.txt', 'r') as f:
    content = f.read()
print('-' * 20)

# 5. 条件赋值
x = 10
# 非 Pythonic：多行 if-else
if x > 0:
    sign = 'positive'
else:
    sign = 'non-positive'

# Pythonic：一行条件表达式
sign = 'positive' if x > 0 else 'non-positive'
print('-' * 20)

# 6. 检查空容器
items = []
# 非 Pythonic：显式检查长度
if len(items) == 0:
    print('没有数据')

# Pythonic：利用空序列的布尔特性
if not items:
    print('没有数据')
print('-' * 20)

# 7. 多列表同时遍历
a = [1, 2, 3]
b = ['x', 'y', 'z']
# 非 Pythonic：用下标索引
for i in range(len(a)):
    print(a[i], b[i])

# Pythonic：用 zip 打包
for num, ch in zip(a, b):
    print(num, ch)
print('-' * 20)

# 8. 列表推导式代替简单循环
# 非 Pythonic：普通 for 循环
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x*x)
print(squares)

# Pythonic：列表推导式
squares = [x*x for x in range(10) if x % 2 == 0]
print(squares)
print('-' * 20)

# 9. 真假判断（判断是否为真）
is_login = True
# 非 Pythonic：多余和 True 显式比较，代码冗余
if is_login == True:
    print(is_login)

# Pythonic：直接使用布尔变量本身做条件，简洁地道、符合 Python 编码风格
if is_login:
    print(is_login)
print('-' * 20)

# 10. 真假判断（判断是否为假）
# 非 Pythonic：多余和 False 显式比较，代码冗余
if is_login == False:
    print(is_login)

# Pythonic：直接用 not 取反
if not is_login:
    print(is_login)
print('-' * 20)

# 10. 判断是否为空
x = None
# 非 Pythonic：使用 == 与 None 比较， 语法完全合法，运行时不会报错，约定俗称的认为这是一种错误写法
if x == None:
    print(True)

# Pythonic：使用 is 进行判断
if x is None:
    print(True)