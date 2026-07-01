# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的顺序结构
@date 2026/6/15 10:43

一、顺序结构

1. for 循环结构
2. while 循环结构
3. do-while 循环结构

二、流程控制完整体系（三大结构协作实现完整程序逻辑）

1. 顺序结构 负责提供默认执行线
2. 分支结构 负责条件选择路径
3. 循环结构 负责重复执行代码
"""


# 顺序结构演示
print('第一步：定义两个数字')
a = 10
b = 20

print('第二步：计算两数之和')
sum_num = a + b

print('第三步：输出结果')
print(f'{a} + {b} = {sum_num}')