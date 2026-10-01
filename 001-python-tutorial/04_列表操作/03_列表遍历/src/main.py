# -*- coding: utf-8 -*-
"""python 中的列表基础遍历

:author: lingwh
:date: 2026/8/17 22:03
"""


lst = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'sunqi']
# len()函数
print('列表 lst 的长度: %d' % len(lst))

# 遍历列表，for-in 遍历
def foreach_list_1() -> None:
    for name in lst:
        print(name)
    print('-' * 20)


# 遍历列表，for-in + range() + len() 遍历
def foreach_list_2() -> None:
    # 注意： range(len(lst)) 这里只计算一次
    for i in range(len(lst)):
        print(lst[i])
    print('-' * 20)


# 遍历列表，while + len() 遍历
def foreach_list_3() -> None:
    length = len(lst)
    i = 0
    while i < length:
        print(lst[i])
        i += 1
    print('-' * 20)


# 遍历列表，for-in + enumerate() 遍历，同时获取下标和元素
def foreach_list_4() -> None:
    for index, value in enumerate(lst):
        print(f'下标: {index}, 元素值: {value}')
    print('-' * 20)


if __name__ == '__main__':
    foreach_list_1()
    foreach_list_2()
    foreach_list_3()
    foreach_list_4()
