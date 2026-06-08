# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的复合赋值
@date 2026/6/8 16:14
"""

# 普通赋值
a = 10
print('a = %d' % a)

# 一次赋值多个变量
b, s = 20, '我是一个字符串'
print('b = %d' % b)
print('s = %s' % s)

# 常见复合赋值
a += b
# a = a + b
print('a = %d' % a)

a -= b
# a = a - b
print('a = %d' % a)

a *= b
# a = a * b
print('a = %d' % a)

# 位运算复合赋值
a &= b
# a = a & b
print('a = %d' % a)

a ^= b
# a = a ^ b
print('a = %d' % a)