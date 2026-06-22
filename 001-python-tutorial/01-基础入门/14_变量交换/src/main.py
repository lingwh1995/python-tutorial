# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的变量交换/两数交换/两字符串交换
@date 2026/6/14 20:38
"""


# 1. 方式1： 引入临时变量
a = '牛奶'
b = '可乐'
print('a = %s, b = %s' % (a, b))

temp = a
a = b
b = temp
print('a = %s, b = %s' % (a, b))
print('-' * 20)

# 2. python独有的解构方式
a = '牛奶'
b = '可乐'
print('a = %s, b = %s' % (a, b))

a, b = b, a
print('a = %s, b = %s' % (a, b))
print('-' * 20)

# 3. 算术运算
a = 10
b = 20
print('a = %d, b = %d' % (a, b))

a = a + b
b = a - b
a = a - b
print('a = %d, b = %d' % (a, b))
print('-' * 20)

# 4. 位运算 一个数字被异或两次，该数字值保持不变 a ^ b ^ b = a
a = 10
b = 20
print('a = %d, b = %d' % (a, b))

a = a ^ b   # a = a ^ b
b = a ^ b   # b = a ^ b = a ^ b ^ b = a
a = a ^ b   # a = a ^ b = a ^ b ^ a = b
print('a = %d, b = %d' % (a, b))
print('-' * 20)