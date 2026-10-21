# -*- coding: utf-8 -*-
"""python 中元组的方法

1. 元组是不可变序列，不支持增、删、改，所以元组的方法只有两个：count() 和 index()，其余如 len()、sorted()、sum() 等都是内置函数，不是元组独有。
2. 注意区分：列表的 sort() / reverse() 是原地修改，元组没有这些方法， 元组只能用 sorted()、reversed() 来排序和反转，返回值为列表类型

@author lingwh
@date 2026/10/20 17:42
"""

# 示例数据
t = (1, 2, 3, 4, 5)              # 基础示例元组
t_dup = (1, 2, 2, 3, 3, 3, 4)    # 含重复元素
t_str = ('apple', 'banana', 'cherry')
t_mixed = (1, 'a', 2, 'b')       # 混合类型


def show(title, result) -> None:
    """
    统一输出格式，让输入和结果一目了然。
    """
    print(f'{title:<40} -> {result!r}')


show('t', t)
show('t_dup', t_dup)
show('t_str', t_str)
show('t_mixed', t_mixed)


# 1. 长度
#   len(t) 统计元组中元素的个数

print('\n--- 1. 长度：len ---')

show("len(t)", len(t))
show("len(t_dup)", len(t_dup))
show("len(t_str)", len(t_str))
show("len(t_mixed)", len(t_mixed))


# 2. 查找
#   index(x)       返回第一个等于 x 的元素索引，找不到抛出 ValueError
#   index(x, i, j) 在切片 [i, j) 中查找 x 的索引
#   index(x, i)    在切片 [i, 末尾] 中查找 x 的索引

print('\n--- 2. 查找：index ---')

show('t', t)
show("t.index(3)", t.index(3))                   # 元素 3 的索引
show("t_dup.index(3)", t_dup.index(3))           # 只返回第一个 3 的索引

# index() 在找不到时会抛出 ValueError，演示如下
try:
    show("t.index(6)", t.index(6))
except ValueError as e:
    show("t.index(6)", f'ValueError: {e}')

show("t.index(3, 0, 4)", t.index(3, 0, 4))       # 在切片 [0, 4) 中查找 3 的索引
show("t.index(5, 0)", t.index(5, 0))             # 在切片 [0, 末尾] 中查找 5 的索引


# 3. 计数
#   count(x)  统计 x 在元组中出现的次数

print('\n--- 3. 计数：count ---')

show('t_dup', t_dup)
print('-' * 3)

show("t_dup.count(2)", t_dup.count(2))
show("t_dup.count(3)", t_dup.count(3))
show("t_dup.count(9)", t_dup.count(9))


# 4. 统计与成员判断
#   sum(t)     求和（元素需为数字）
#   max(t)     最大值
#   min(t)     最小值
#   x in t     判断 x 是否在元组中
#   x not in t 判断 x 是否不在元组中

print('\n--- 4. 统计与成员判断：sum / max / min / in ---')

show('t', t)
print('-' * 3)

show("sum(t)", sum(t))
show("max(t)", max(t))
show("min(t)", min(t))
show("3 in t", 3 in t)
show("6 in t", 6 in t)
show("3 not in t", 3 not in t)
show("6 not in t", 6 not in t)


# 5. 排序
#   元组没有 sort() 方法（不可变，无法原地排序）
#   sorted(t, key=None, reverse=False)  返回排好序的「列表」，原元组不变

print('\n--- 5. 排序：sorted ---')

t_sort = (3, 1, 4, 1, 5, 9, 2, 6)
show('t_sort', t_sort)
show("sorted(t_sort)", sorted(t_sort))                              # 默认升序，返回列表
show("sorted(t_sort, reverse=True)", sorted(t_sort, reverse=True))  # reverse=True 降序
show('t_sort', t_sort)                                              # sorted 后，原元组未变
print('-' * 3)

# 想得到元组结果，再套一层 tuple()
show("tuple(sorted(t_sort))", tuple(sorted(t_sort)))
print('-' * 3)

# key 参数：按「key 函数处理后的值」排序，原元组同样不受影响
t_len = ('aaaaa', 'bbb', 'cc', 'd', 'eeeee')
show('t_len', t_len)
show("sorted(t_len, key=len)", sorted(t_len, key=len))                              # 按长度升序
show("sorted(t_len, key=len, reverse=True)", sorted(t_len, key=len, reverse=True))  # 按长度降序
show('t_len', t_len)


# 6. 反转
#   元组没有 reverse() 方法（不可变）
#   reversed(t) 内置函数，返回迭代器，不修改原元组

print('\n--- 6. 反转：reversed ---')

show('t', t)
show("list(reversed(t))", list(reversed(t)))    # 转成列表查看结果
show("tuple(reversed(t))", tuple(reversed(t)))  # 想保持元组类型就套一层 tuple()
show('t', t)                                    # 原元组未变


# 7. 元组 <-> 列表 转换
#   tuple(lst) 列表转元组
#   list(t)    元组转列表（元组不可修改，需要改内容时先转列表，改完再转回来）

print('\n--- 7. 转换：tuple / list ---')

show("t", t)
show("list(t)", list(t))
show("tuple([1, 2, 3])", tuple([1, 2, 3]))
show("tuple('abc')", tuple('abc'))         # 字符串也能转，逐字符拆分

t_change = (1, 2, 3)
lst_change = list(t_change)
lst_change[0] = 'a'
show("list(t_change)", lst_change)
show("tuple(lst_change)", tuple(lst_change))