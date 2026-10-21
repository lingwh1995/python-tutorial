# -*- coding: utf-8 -*-
"""python 中的列表案例

@author lingwh
@date 2026/10/21 10:26
"""


def get_lucky_nums_by_loop() -> list:
    """生成幸运数字（循环实现）
    使用循环实现：输入任意数字，并生成 1 到该数字的列表，如输入 15 时生成列表 [1, 2, 3, 4, 5, ... 15]，从中选取能被 6 整除的数放入新列表
    """
    while True:
        try:
            max_limit = int(input('请输入数字：'))
            break   # 如果输入的是数字，就停止输入
        except ValueError as e:
            print(f'ValueError：输入不是合法的数字！{e}')
    nums = []
    for i in range(1, max_limit + 1):
        nums.append(i)
    lucky_nums = []
    for i in range(1, len(nums)):
        if nums[i] % 6 == 0:
            lucky_nums.append(nums[i])
    return lucky_nums


def get_lucky_nums_by_comprehension() -> list:
    """生成幸运数字（列表推导式实现）
    使用列表推导式实现：输入任意数字，并生成 1 到该数字的列表，如输入 15 时生成列表 [1, 2, 3, 4, 5, ... 15]，从中选取能被 6 整除的数放入新列表
    """
    while True:
        try:
            max_limit = int(input('请输入数字：'))
            break   # 如果输入的是数字，就停止输入
        except ValueError as e:
            print(f'ValueError：输入不是合法的数字！{e}')
    nums = [i for i in range(1, max_limit + 1)]
    lucky_nums = [nums[i] for i in range(1, len(nums)) if nums[i] % 6 == 0]
    return lucky_nums


if __name__ == '__main__':
    lucky_nums_by_loop = get_lucky_nums_by_loop()
    print(lucky_nums_by_loop)

    lucky_nums_by_comprehension = get_lucky_nums_by_comprehension()
    print(lucky_nums_by_comprehension)