# -*- coding: utf-8 -*-
"""python 中的列表基础遍历

:author: lingwh
:date: 2026/8/17 22:03
"""


s = [1, 2, 3, 4, 5]
# len()函数
print('列表s的长度: %d' % len(s))

# 遍历列表，for-in 遍历
def foreach_list_1() -> None:
    for i in s:
        print(i)
    print('-' * 20)


# 遍历列表，for-in + range() + len() 遍历
def foreach_list_2() -> None:
    for i in range(len(s)):
        print(s[i])
    print('-' * 20)


# 遍历列表，while + len() 遍历
def foreach_list_3() -> None:
    i = 0
    while i < len(s):
        print(s[i])
        i += 1
    print('-' * 20)


# 遍历列表，for-in + enumerate() 遍历，同时获取下标和元素
def foreach_list_4() -> None:
    for index, value in enumerate(s):
        print(f'下标{index}: 元素{value}')
    print('-' * 20)


if __name__ == '__main__':
    foreach_list_1()
    foreach_list_2()
    foreach_list_3()
    foreach_list_4()
