# -*- coding: utf-8 -*-
"""python 中的列表元组字典集合

@author lingwh
@date 2026/8/28 14:12
"""


def test_container() -> None:
    """
        列表: []
        元组: ()
        字典: {键值对}
        集合: {单值, 单值...}
    """
    # 定义一个列表
    list_1 = [1, 2, 3]
    # 定义一个元素
    tuple_1 = (1, 2, 3)
    # 定义一个字典
    dict_1 = {
        1: 'one',
        2: 'two',
    }
    # 定义一个集合
    set_1 = {10, 20, 30, 40}

    print(f"list_1 = {list_1}, type(list_1) = {type(list_1)}")
    print(f"tuple_1 = {tuple_1}, type(tuple_1) = {type(tuple_1)}")
    print(f"dict_1 = {dict_1}, type(dict_1) = {type(dict_1)}")
    print(f"set_1 = {set_1}, type(set_1) = {type(set_1)}")


if __name__ == '__main__':
    test_container()