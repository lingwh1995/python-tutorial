# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的类型转换
@date 2026/6/8 16:23

类型转换

1. int()    字符串形式的整数/float类型的小数 -> 转成整数类型（可能会丢失精度，慎用）
2. float()  字符串形式的小数/int类型的整数 -> 转成小数类型
3. str()    整数/小数 -> 字符串类型
4. bool()   具体值 ->布尔类型（0 → False，非0 → True）
5. eval()   相当于去掉引号，是什么就是什么
              例如: '10' → 10, '10.3' → 10.3, 'True' → True, 'name' → name变量, 没有这个变量, 就报错
6. chr()    数字编码 -> 阿拉伯数字/字母
7. ord()    阿拉伯数字/字母 -> Unicode 编码数字
"""


a = '1'
b = '2'
print(a + b)

# 1. int()
print(int(10.3))
print(int('20'))
# print(int('10.3'))  # 报错
print('-' * 20)

# 2. float()
print(float(10))
print(float('20.3'))
print(float('111'))
print('-' * 20)

# 3. str()
print(str(10))
print(str(10.3))
print('-' * 20)

# 4. 演示 bool()
print(bool(0))
print(bool(1))
print(bool(1.2))
print(bool('张三'))
print('-' * 20)

# 5. eval()
print(eval('10.3'))
print(eval('22'))
print(eval('True'))

name = 'zhangsan'
print(eval('name')) # 相当于去掉 'name'的引号，name就不是字符串了，而是 变量名

print(type(eval('10.3')))
print(type(eval('22')))
print(type(eval('True')))
print('-' * 20)

# 6. chr()
print(chr(48))
print(chr(65))
print(chr(97))
print('-' * 20)

# 7. ord()
print(ord('0'))
print(ord('A'))
print(ord('a'))
print('-' * 20)