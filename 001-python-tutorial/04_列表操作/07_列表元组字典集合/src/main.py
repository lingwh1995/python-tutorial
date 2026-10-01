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
    lst = [1, 2, 3]
    # 定义一个元素
    tpl = (1, 2, 3)
    # 定义一个字典
    d = {
        1: 'one',
        2: 'two',
    }
    # 定义一个集合
    st = {10, 20, 30, 40}

    print(f"lst = {lst}, type(lst) = {type(lst)}")
    print(f"tpl = {tpl}, type(tpl) = {type(tpl)}")
    print(f"d = {d}, type(d) = {type(d)}")
    print(f"st = {st}, type(st) = {type(st)}")


if __name__ == '__main__':
    test_container()