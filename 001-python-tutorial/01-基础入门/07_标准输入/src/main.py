# -*- coding: utf-8 -*-
"""python 中的标准输入

1. input() 函数的返回值是字符串， 绝对不是整数
2. 要获得整数，使用 int(input) 函数转换一下数据类型

:author: lingwh
:date: 2026/6/8 14:46
"""


# 不带有提示的input()函数
# user_input = input()
# print(user_input)

# 带有提示的input()函数
#user_input = input('please input str:')
#print(v)

# 一个简单的案例
name = input('请输入姓名: ')
age =  int(input('请输入年龄: '))           # 注意这里的类型转换
salary = float(input('请输入月薪: '))       # 注意这里的类型转换
print(f'姓名：{name}，年龄：{age}，年薪：{salary * 12:.2f}')