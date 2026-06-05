# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 数据类型
@date 2026/6/5 17:02

1. 定义变量和使用变量
     格式: 变量名 = 值
     使用: 变量名
2. 变量的数据类型
     不可变类型
       int       整型类型
         i = 10
       float     浮点类型
         f = 1.0
       str       字符串类型
         s = ''
         s = ' '
         s = 'hello'
         s = ""
         s = " "
         s = "hello"
         s = '''hello'''        # 特殊的字符串定义格式第一种
         s = \"""hello\"""      # 特殊的字符串定义格式第二种
       bool      布尔类型
         b = True
         b = False
       tuple     元组类型
         t = (1,2,3,"aaa")
       NoneType  空类型
         n = None
     可变类型
       list
         l = [10, 20, "张三", True]
       dict
         d = { "name":"zhangsan", "age":20 }
       set
         s = {1,2,3,3}  # 自动去重 {1,2,3}
     自定义类型
       class
3. 判断变量类型
     type(变量)
"""


# 定义变量
a = 1
b = 3.14
c = 'Hello Python!'
d = "Python 程序员!"
# 特殊的字符串定义格式第一种
e = '''三个单引号包裹'''
# 特殊的字符串定义格式第二种
f = """三个双引号包裹"""
g = True

# 打印变量
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# 使用type()判断变量类型
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))