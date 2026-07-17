# -*- coding: utf-8 -*-
"""python 实现石头剪刀布游戏

:author: lingwh
:date: 2026/7/1 11:44
"""

import random


def guess_game() -> None:
    """石头剪刀布猜拳游戏

    游戏规则:
    - 0: 石头
    - 1: 剪刀
    - 2: 布

    石头赢剪刀，剪刀赢布，布赢石头
   """
    while True:
        while True:
            player_shoot = int(input('请您出拳 (石头 0，剪刀 1，布 2):'))
            if player_shoot in (0, 1, 2):
                break
            print("您出错了，请重新出！")
        print('我方出的是: %d' % player_shoot)

        # 定义一个电脑变量，使用随机数获取状态
        robot_shoot = random.randint(0, 2)
        print('电脑出的是: %d' % robot_shoot)

        # 平局
        if player_shoot == robot_shoot:
            print('平局......')
        # 玩家赢
        elif ((player_shoot == 0) and (robot_shoot == 1)) or ((player_shoot == 1) and (robot_shoot == 2)) or ((player_shoot == 2) and (robot_shoot == 0)):
            print('您赢了......')
        # 电脑赢
        else:
            print('电脑赢......')


def get_total_while() -> None:
    """使用 while 循环计算 1 ~ 100 的累加和并打印结果"""
    total = 0
    num = 1
    while num <= 100:
        total += num
        num += 1
    print(f"1~100累加和(while): {total}")


def get_total_for() -> None:
    """使用 for 循环计算 1 ~ 100 的累加和并打印结果"""
    total = 0
    for num in range(1, 101):
        total += num
    print(f"1~100累加和(for): {total}")


def print_multiplication_table() -> None:
    """打印99乘法表"""
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{j} * {i} = {i * j}', end='\t')
        print('')


def print_multiplication_table() -> None:
    """打印左下三角 99 乘法表"""
    # 外层控制行数
    for row in range(1, 10):
        line_parts = []
        # 内层控制每行算式
        for col in range(1, row + 1):
            line_parts.append(f"{col} * {row} = {col * row}")
        # 拼接整行再一次性打印，减少IO操作，效率更高
        print("\t".join(line_parts))


if __name__ == '__main__':
    # guess_game()
    # get_total_while()
    # get_total_for()
    print_multiplication_table()
