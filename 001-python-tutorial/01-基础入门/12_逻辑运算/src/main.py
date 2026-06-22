# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的逻辑运算
@date 2026/6/22 18:13
"""

# 0为False，非0为True
if(0):
    print('输出这行说明 0 代表 True')
else:
    print('输出这行说明 0 代表 False')
print('-' * 20)

# 基础逻辑运算
# and（逻辑与） - 全真才真，一假则假
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print('-' * 20)
# or （逻辑或） - 一真就真，全假才假
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print('-' * 20)
# not（逻辑非） - 真假反转
print(not True)
print(not False)
print('-' * 20)

# 运算优先级 - 逻辑运算符的优先级从高到低为 not > and > or
# 没有括号：先计算 not，再计算 and，最后计算 or
result = not True and False or True
print(result)
# 有括号：先计算括号内的 and
result = not (True and False) or True
print(result)
# 有括号：先计算括号内的 or
result = not True and (False or True)
print(result)
print('-' * 20)

# 短路求值
# and 短路 - 左边为假，右边的 print 不会执行
0 and print("0 and 这行代码不会被执行")
# and 短路 - 左边为真，才会计算右边
5 and print("5 and 这行代码会被执行")

# or 短路 - 左边为真，右边的 print 不会执行
5 or print("5 or  这行代码不会被执行")

# or 短路 - 左边为假，才会计算右边
0 or print("0 or  这行代码会被执行")