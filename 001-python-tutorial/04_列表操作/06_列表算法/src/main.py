# -*- coding: utf-8 -*-
"""python 中的列表算法

:author: lingwh
:date: 2026/8/17 22:03
"""


s = [1, 2, 3, 4, 5]
nums = [3, 1, 4, 1, 5, 9, 2, 6]


# 推荐：切片写法，最简洁、最快
def reverse_best(lst) -> list:
    """切片写法，最简洁、最快"""
    return lst[::-1]


# 可读性也不错（适合教学，避免切片魔术语法）
def reverse_reversed(lst) -> list:
    """内置函数写法，可读性好"""
    return list(reversed(lst))


# 如果一定要用循环，用列表拼接替代 +=
def reverse_loop(lst) -> list:
    """循环写法，可读性好"""
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result


def print_even_index_elem(lst) -> None:
    """打印偶数索引的元素"""
    for i in range(0, len(lst), 2):
        print(lst[i])


def judge_elem_in_list(lst, x) -> bool:
    """判断元素是否在列表中"""
    return x in lst


def bubble_sort(lst) -> list:
    """冒泡排序：原地排序，返回排序后的列表"""
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def deduplicate(lst) -> list:
    """列表去重，保留原顺序"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == '__main__':
    s_reverse = reverse_best(s)
    print(s_reverse)
    s_reverse = reverse_reversed(s)
    print(s_reverse)
    s_reverse = reverse_loop(s)
    print(s_reverse)
    print_even_index_elem(s)
    result = judge_elem_in_list(s, 3)
    print(result)
    print('排序前:', nums)
    print('冒泡排序:', bubble_sort(nums[:]))
    print('去重前:', [3, 1, 4, 1, 5, 9, 2, 6, 3])
    print('去重后:', deduplicate([3, 1, 4, 1, 5, 9, 2, 6, 3]))
