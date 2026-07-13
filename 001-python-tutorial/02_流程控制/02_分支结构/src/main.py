# -*- coding: utf-8 -*-
"""python 中的分支结构

一、分支结构

1. 基础 if-else
2. 多分支 if-elif-else
3. 三元运算符（格式：值1 if 条件判断 else 值2）
4. 多分支 match-case（等价于其他语言switch-case，但功能强于switch-case）

二、流程控制完整体系（三大结构协作实现完整程序逻辑）

1. 顺序结构 负责提供默认执行线
2. 分支结构 负责条件选择路径
3. 循环结构 负责重复执行代码

:author: lingwh
:date: 2026/6/15 10:39
"""


# 1. 基础 if-else
i = 10
if i % 2 == 0:
    print('偶数')
else:
    print('奇数')
print('-' * 20)

# 2. 多分支 if-elif-else
score = 78
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')
print('-' * 20)

# 3. 三元运算符
age = 16
tip = '成年人' if age >= 18 else '未成年人'
print(tip)
i = 5
tip = '偶数' if i % 2 == 0 else '奇数'
print(tip)
print('-' * 20)

# 4. 多分支 match-case
# 基础等值匹配（等价 switch）
level = 'B'
match level:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('合格')
    case _:
        print('不合格')

# 带变量绑定
score = 65
match score:
    case 100:
        res = '满分'
    case s if s >= 90:  # 守卫条件（if判断）
        res = f'优秀{s}分'
    case s if s >= 60:
        res = f'及格{s}分'
    case _:
        res = '不及格'

# 解构匹配（列表 / 元组 / 字典 / 对象）
point = (2, 0)
match point:
    case (0, 0):
        print('原点')
    case (x, 0):
        print(f'X轴，x = {x}')
    case (0, y):
        print(f'Y轴，y = {y}')
    case (x, y):
        print(f'普通坐标({x},{y})')

# 字典匹配
user = {'name': 'Tom', 'role': 'admin'}
match user:
    case {'role': 'admin', 'name': n}:
        print(f'管理员：{n}')
    case {'role': 'user', 'name': n}:
        print(f'普通用户：{n}')