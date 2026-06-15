# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的标准输入
@date 2026/6/8 14:46

特别注意

1. input() 函数的返回值是字符串， 绝对不是整数
2. 要获得整数，使用 int(input) 函数转换一下数据类型
"""


# 不带有提示的input()函数
# s = input()
# print(s)

# 带有提示的input()函数
#s = input('please input str:')
#print(s)

# 一个简单的案例
user_name = input('请输入姓名: ')
user_age =  int(input('请输入年龄: '))           # 注意这里的类型转换
user_salary = float(input('请输入月薪: '))       # 注意这里的类型转换
print(f'姓名：{user_name}，年龄：{user_age}， 年薪：{user_salary * 12:.2f}')