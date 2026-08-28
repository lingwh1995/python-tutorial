# -*- coding: utf-8 -*-
"""python 中的列表基础遍历

:author: lingwh
:date: 2026/8/17 22:03
"""


name_list = ['zhangsan', 'lisi', 'wangwu', 'zhaoliu', 'sunqi']
# len()函数
print('列表 name_list 的长度: %d' % len(name_list))

# 遍历列表，for-in 遍历
def foreach_list_1() -> None:
    for name in name_list:
        print(name)
    print('-' * 20)


# 遍历列表，for-in + range() + len() 遍历
def foreach_list_2() -> None:
    # 注意： range(len(name_list)) 这里只计算一次
    for i in range(len(name_list)):
        print(name_list[i])
    print('-' * 20)


# 遍历列表，while + len() 遍历
def foreach_list_3() -> None:
    length = len(name_list)
    i = 0
    while i < length:
        print(name_list[i])
        i += 1
    print('-' * 20)


# 遍历列表，for-in + enumerate() 遍历，同时获取下标和元素
def foreach_list_4() -> None:
    for index, value in enumerate(name_list):
        print(f'下标: {index}, 元素值: {value}')
    print('-' * 20)


if __name__ == '__main__':
    foreach_list_1()
    foreach_list_2()
    foreach_list_3()
    foreach_list_4()
