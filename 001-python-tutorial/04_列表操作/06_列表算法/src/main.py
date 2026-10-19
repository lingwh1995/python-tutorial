# -*- coding: utf-8 -*-
"""python 中的列表算法

:author: lingwh
:date: 2026/8/17 22:03
"""


def reverse_best(source) -> list:
    """切片写法

    最简洁、最快
    """
    return source[::-1]


def reverse_reversed(source) -> list:
    """内置函数写法

    可读性也不错（适合教学，避免切片魔术语法）
    """
    return list(reversed(source))


def reverse_loop(source) -> list:
    """循环写法

    可读性好，注意用 append() 替代 +=
    """
    result = []
    for i in range(len(source) - 1, -1, -1):
        result.append(source[i])
    return result


def print_even_index_elem(source) -> None:
    """打印偶数索引的元素"""
    for i in range(0, len(source), 2):
        print(source[i])


def judge_elem_in_list(source, x) -> bool:
    """判断元素是否在列表中"""
    return x in source


def bubble_sort(source) -> list:
    """冒泡排序：原地排序，返回排序后的列表"""
    n = len(source)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if source[j] > source[j + 1]:
                source[j], source[j + 1] = source[j + 1], source[j]
    return source


def deduplicate(source) -> list:
    """列表去重，保留原顺序"""
    seen = set()
    result = []
    for item in source:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    sort_lst = [3, 1, 4, 1, 5, 9, 2, 6]

    reversed_lst = reverse_best(lst)
    print(reversed_lst)

    reversed_lst = reverse_reversed(lst)
    print(reversed_lst)

    reversed_lst = reverse_loop(lst)
    print(reversed_lst)

    print_even_index_elem(lst)

    is_exist = judge_elem_in_list(lst, 3)
    print(is_exist)

    print('排序前:', sort_lst)
    print('冒泡排序:', bubble_sort(sort_lst[:]))
    print('去重前:', [3, 1, 4, 1, 5, 9, 2, 6, 3])
    print('去重后:', deduplicate([3, 1, 4, 1, 5, 9, 2, 6, 3]))
