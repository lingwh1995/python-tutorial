# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 实现石头剪刀布游戏
@date 2026/7/1 11:44
"""

import random


def guess_game():
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


if __name__ == '__main__':
    guess_game()