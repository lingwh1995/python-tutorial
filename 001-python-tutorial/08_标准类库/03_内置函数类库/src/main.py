# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的内置类库
@date 2026/6/8 16:30
"""


def builtins_lib_test():
    # 绝对值
    print(abs(-9))

    # 四舍五入保留n位
    print(round(3.1415, 2))

    # a 的 b 次方
    print(pow(2, 3))

    # 求最大值和最小值函数
    nums = [1, 2, 3, 4, 5]
    # 最大值
    print(max(nums))
    print(max(1, 5, 3))
    # 最小值
    print(min(nums))

    # 可迭代对象 求和
    print(sum(nums))

    # 获取列表长度
    print(len(nums))

    # 类型转换
    i = 100
    s = '200'
    # 字符串转数字
    print(str(i))
    # 数字转字符串
    print(int(s))

    # 生成整数序列
    # 格式 1：range (stop)
    r = range(5)
    print(list(r))
    # 格式 2：range (start, stop)
    r = range(2, 8)
    print(list(r))
    # 格式 3：range(start, stop, step)
    r = range(1, 9, 2)
    print(list(r))

    # 转换可迭代对象
    # 元组 → 列表
    t = (1, 2, 3)
    print(list(t))
    # 字符串 → 列表
    s = 'hello'
    print(list(s))
    # 区间 → 列表
    r = range(1, 6)
    print(list(r))
    # 生成器 -> 列表
    gen = (x * 2 for x in range(3))
    print(list(gen))

    # 排序
    nums = [5, 9, 3, 1, 7]
    # 升序
    asc = sorted(nums)
    print(asc)
    # 降序
    desc = sorted(nums, reverse=True)
    print(desc)
    # 原列表不变
    print(nums)


if __name__ == "__main__":
    builtins_lib_test()