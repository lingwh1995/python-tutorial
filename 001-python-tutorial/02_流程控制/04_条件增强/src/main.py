# -*- coding: utf-8 -*-
"""python （流程控制中的）条件表达式部分增强

1. python 支持表达式的链式写法
2. python 中简单条件表达式不用加括号，只有下面两种情况才推荐加括号
     多行条件（续行场景） - 当条件很长需要拆分成多行时，用括号包裹是 PEP 8 推荐的写法，比用反斜杠 \ 续行更优雅：
     明确逻辑运算优先级 - 当条件中同时存在 and 和 or 时，用括号明确运算顺序

:author: lingwh
:date: 2026/7/10 10:34
"""

# python 独有链式写法，等价于其他语言中 18 <= age and age < 30
age = 20
if 18 <= age < 30:
    print('18 <= age < 30 这是python语言独有的链式的写法...')

# 简单条件表达式中直接省略括号，其他语言中条件表达式必须写成 (age > 18)，python语言中直接使用 age > 18
if (age > 18):
    print("用户已经成年......")

# 条件表达式使用括号的情况一： 多行条件需要续行时，使用括号包裹多行条件比用反斜杠 \ 续行更优雅
has_discount = True
score = 80
if (18 <= age < 30
        and has_discount
        and score >= 60):
    print("审核通过")

# 条件表达式使用括号的情况二： 明确逻辑运算优先级
if (age < 18 or age >= 60) and has_discount:
    print("享受优惠")