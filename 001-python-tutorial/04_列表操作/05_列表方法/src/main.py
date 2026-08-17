# -*- coding: utf-8 -*-
"""python 列表常用方法

:author: lingwh
:date: 2026/8/17 22:03
"""


# 前置知识：列表是可变对象，部分方法会直接修改原列表（如 append、extend、sort、reverse 等），
# 它们返回 None；而 sorted()、reversed() 等内置函数则返回新对象，不修改原列表。
# 注意区分：方法是「原地修改」，函数是「生成新对象」。

# 示例数据
s = [1, 2, 3, 4, 5]              # 基础示例列表
s_dup = [1, 2, 2, 3, 3, 3, 4]    # 含重复元素
s_str = ['apple', 'banana', 'cherry']
s_nested = [[1, 2], [3, 4]]      # 嵌套列表
s_mixed = [1, 'a', 2, 'b']       # 混合类型


def show(title, result) -> None:
    """
        统一输出格式，让输入和结果一目了然。
    """
    print(f'{title:<35} -> {result!r}')


# 1. 长度
print('\n--- 1. 长度：len ---')

show('s', s)
show('s_dup', s_dup)
show('s_str', s_str)
show('s_nested', s_nested)
show('s_mixed', s_mixed)
print('-' * 3)

show("len(s)", len(s))
show("len(s_dup)", len(s_dup))
show("len(s_str)", len(s_str))
show("len(s_nested)", len(s_nested))
show("len(s_mixed)", len(s_mixed))


# 2. 查找
#   index(x)       返回第一个等于 x 的元素索引，找不到抛出 ValueError
#   index(x, i, j) 在切片 [i, j) 中查找 x 的索引

print('\n--- 2. 查找：index ---')

show('s', s)
print('-' * 3)

show("s.index(3)", s.index(3))               # 元素 3 的索引
show("s_dup.index(3)", s_dup.index(3))       # 第一个 3 的索引

# index() 在找不到时会抛出 ValueError，演示如下
try:
    show("s.index(6)", s.index(6))
except ValueError as e:
    show("s.index(6)", f'ValueError: {e}')

show("s.index(3, 0, 4)", s.index(3, 0, 4))   # 在切片 [0, 4) 中查找 3 的索引


# 3. 添加
#   append(x)     在末尾追加单个元素，原地修改，返回 None
#   extend(iter)  在末尾追加可迭代对象的所有元素，原地修改，返回 None
#   insert(i, x)  在下标 i 处插入 x，原地修改，返回 None

print('\n--- 3. 添加：append / extend / insert ---')

s_append = [1, 2, 3]
show('s_append（原）', s_append)
s_append.append(4)
show("s_append.append(4)", s_append)
s_append.append([5, 6])   # append 会把列表作为一个整体追加
show("s_append.append([5, 6])", s_append)
print('-' * 3)

s_extend = [1, 2, 3]
show('s_extend（原）', s_extend)
s_extend.extend([4, 5, 6])   # extend 会把列表的每个元素逐一追加
show("s_extend.extend([4, 5, 6])", s_extend)
show("s_extend.extend('ab')", (s_extend.extend('ab'), s_extend)[1])
print('-' * 3)

s_insert = [1, 2, 3]
show('s_insert（原）', s_insert)
s_insert.insert(1, 'x')   # 在下标 1 处插入 'x'
show("s_insert.insert(1, 'x')", s_insert)


# 4. 删除
#   remove(x)   删除第一个等于 x 的元素，找不到抛出 ValueError，原地修改
#   pop()       删除并返回末尾元素（默认），pop(i) 删除并返回下标 i 的元素，原地修改
#   clear()     清空列表，原地修改
#   del lst[i]  语句，删除下标 i 的元素
#   del lst[i:j] 语句，删除切片

print('\n--- 4. 删除：remove / pop / clear / del ---')

s_remove = [1, 2, 2, 3]
show('s_remove（原）', s_remove)
s_remove.remove(2)   # 只删除第一个 2
show("s_remove.remove(2)", s_remove)
show('s_remove（改后）', s_remove)

# remove() 在找不到时会抛出 ValueError
try:
    s_remove.remove(9)
except ValueError as e:
    show("s_remove.remove(9)", f'ValueError: {e}')
print('-' * 3)

s_pop = [1, 2, 3, 4]
show('s_pop（原）', s_pop)
show("s_pop.pop()", s_pop.pop())             # 删除并返回末尾元素
show('s_pop（改后）', s_pop)
show("s_pop.pop(0)", s_pop.pop(0))           # 删除并返回下标 0 的元素
show('s_pop（改后）', s_pop)
print('-' * 3)

s_del = [1, 2, 3, 4, 5]
show('s_del（原）', s_del)
del s_del[0]
show("del s_del[0]", s_del)
del s_del[1:3]
show("del s_del[1:3]", s_del)
print('-' * 3)

s_clear = [1, 2, 3]
show('s_clear（原）', s_clear)
s_clear.clear()
show("s_clear.clear()", s_clear)


# 5. 修改
#   lst[i] = x   按下标修改元素
#   lst[i:j] = iterable   按切片修改，长度可不一致

print('\n--- 5. 修改：按下标 / 按切片 ---')

s_mod = [1, 2, 3, 4, 5]
show('s_mod（原）', s_mod)
s_mod[0] = 'a'
show("s_mod[0] = 'a'", s_mod)
s_mod[1:3] = ['x', 'y', 'z']   # 切片修改，长度可不一致
show("s_mod[1:3] = ['x','y','z']", s_mod)


# 6. 排序
#   sort(key=None, reverse=False)  原地排序，返回 None
#   sorted(iter, key=None, reverse=False)  内置函数，返回新列表，不修改原列表

print('\n--- 6. 排序：sort / sorted ---')

s_sort = [3, 1, 4, 1, 5, 9, 2, 6]
show('s_sort（原）', s_sort)
show("sorted(s_sort)", sorted(s_sort))             # 不修改原列表
show('s_sort（sorted 后）', s_sort)
s_sort.sort()
show("s_sort.sort()", s_sort)                      # 原地排序
show('s_sort（sort 后）', s_sort)
print('-' * 3)

s_sort2 = [3, 1, 4, 1, 5]
show("s_sort2.sort(reverse=True)", (s_sort2.sort(reverse=True), s_sort2)[1])
show('s_str', s_str)
show("sorted(s_str, key=len)", sorted(s_str, key=len))


# 7. 反转
#   reverse()      原地反转，返回 None
#   reversed(lst)  内置函数，返回迭代器，不修改原列表

print('\n--- 7. 反转：reverse / reversed ---')

s_rev = [1, 2, 3, 4, 5]
show('s_rev（原）', s_rev)
show("list(reversed(s_rev))", list(reversed(s_rev)))   # 不修改原列表
show('s_rev（reversed 后）', s_rev)
s_rev.reverse()
show("s_rev.reverse()", s_rev)                          # 原地反转
show('s_rev（reverse 后）', s_rev)


# 8. 计数
#   count(x)  统计 x 在列表中出现的次数

print('\n--- 8. 计数：count ---')

show('s_dup', s_dup)
print('-' * 3)

show("s_dup.count(2)", s_dup.count(2))
show("s_dup.count(3)", s_dup.count(3))
show("s_dup.count(9)", s_dup.count(9))


# 9. 复制
#   copy()    返回列表的浅拷贝（仅复制最外层，嵌套对象仍是引用）
#   list(lst) 构造函数也能产生浅拷贝
#   lst[:]    切片也能产生浅拷贝

print('\n--- 9. 复制：copy / list() / 切片 ---')

s_copy = [1, 2, [3, 4]]
show('s_copy（原）', s_copy)
s_copy1 = s_copy.copy()
s_copy2 = list(s_copy)
s_copy3 = s_copy[:]
show("s_copy.copy()", s_copy1)
show("list(s_copy)", s_copy2)
show("s_copy[:]", s_copy3)
# 浅拷贝：修改嵌套对象会影响原列表
s_copy1[2].append(5)
show("s_copy1[2].append(5) 后 s_copy", s_copy)      # 原列表也被改了
show("s_copy1[2].append(5) 后 s_copy1", s_copy1)


# 10. 统计与成员判断
#   sum(lst)   求和（元素需为数字）
#   max(lst)   最大值
#   min(lst)   最小值
#   x in lst   判断 x 是否在列表中
#   x not in lst  判断 x 是否不在列表中

print('\n--- 10. 统计与成员判断：sum / max / min / in ---')

show('s', s)
print('-' * 3)

show("sum(s)", sum(s))
show("max(s)", max(s))
show("min(s)", min(s))
show("3 in s", 3 in s)
show("6 in s", 6 in s)
show("6 not in s", 6 not in s)
