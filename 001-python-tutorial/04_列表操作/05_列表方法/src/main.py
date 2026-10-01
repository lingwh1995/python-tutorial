# -*- coding: utf-8 -*-
"""python 列表常用方法

:author: lingwh
:date: 2026/8/17 22:03
"""


# 前置知识：列表是可变对象，部分方法会直接修改原列表（如 append、extend、sort、reverse 等），
# 它们返回 None；而 sorted()、reversed() 等内置函数则返回新对象，不修改原列表。
# 注意区分：方法是「原地修改」，函数是「生成新对象」。

# 示例数据
lst = [1, 2, 3, 4, 5]            # 基础示例列表
lst_dup = [1, 2, 2, 3, 3, 3, 4]  # 含重复元素
lst_str = ['apple', 'banana', 'cherry']
lst_nested = [[1, 2], [3, 4]]    # 嵌套列表
lst_mixed = [1, 'a', 2, 'b']     # 混合类型


def show(title, result) -> None:
    """
        统一输出格式，让输入和结果一目了然。
    """
    print(f'{title:<35} -> {result!r}')


# 1. 长度
print('\n--- 1. 长度：len ---')

show('lst', lst)
show('lst_dup', lst_dup)
show('lst_str', lst_str)
show('lst_nested', lst_nested)
show('lst_mixed', lst_mixed)
print('-' * 3)

show("len(lst)", len(lst))
show("len(lst_dup)", len(lst_dup))
show("len(lst_str)", len(lst_str))
show("len(lst_nested)", len(lst_nested))
show("len(lst_mixed)", len(lst_mixed))


# 2. 查找
#   index(x)       返回第一个等于 x 的元素索引，找不到抛出 ValueError
#   index(x, i, j) 在切片 [i, j) 中查找 x 的索引

print('\n--- 2. 查找：index ---')

show('lst', lst)
print('-' * 3)

show("lst.index(3)", lst.index(3))               # 元index素 3 的索引
show("lst_dup.index(3)", lst_dup.index(3))       # 第一个 3 的索引

# index() 在找不到时会抛出 ValueError，演示如下
try:
    show("lst.index(6)", lst.index(6))
except ValueError as e:
    show("lst.index(6)", f'ValueError: {e}')

show("lst.index(3, 0, 4)", lst.index(3, 0, 4))   # 在切片 [0, 4) 中查找 3 的索引


# 3. 添加
#   append(x)     把单个元素追加到当前列表末尾，原地修改，返回 None
#   extend(iter)  可迭代对象里面的每一项追加到当前列表末尾，原地修改，返回 None
#   insert(i, x)  在下标 i 处插入 x，原地修改，返回 None

print('\n--- 3. 添加：append / extend / insert ---')

lst_append = [1, 2, 3]
show('lst_append（原）', lst_append)
lst_append.append(4)
show("lst_append.append(4)", lst_append)
lst_append.append([5, 6])   # append 会把列表作为一个整体追加
show("lst_append.append([5, 6])", lst_append)
print('-' * 3)

lst_extend = [1, 2, 3]
show('lst_extend（原）', lst_extend)
lst_extend.extend([4, 5, 6])   # extend 会把列表的每个元素按顺序取出来逐一追加到后面
show("lst_extend.extend([4, 5, 6])", lst_extend)
show("lst_extend.extend('ab')", (lst_extend.extend('ab'), lst_extend)[1])
lst_extend = ['apple', 'banana', 'cherry']
lst_extend.extend(['tom', 'jerry'])
show("lst_extend.extend(['tom', 'jerry'])", lst_extend)
show("lst_extend.extend('kim')", (lst_extend.extend('kim'), lst_extend)[1])
print('-' * 3)

lst_insert = [1, 2, 3]
show('lst_insert（原）', lst_insert)
lst_insert.insert(1, 'x')   # 正向索引：从左往右，在下标 1 处插入 'x'，如果索引超过列表长度，插入到列表中最后一个元素的位置
show("lst_insert.insert(1, 'x')", lst_insert)
lst_insert.insert(-1, 'y')  # 逆向索引：从右往左，在下标 1 处插入 'y'，如果索引超过列表长度，插入到列表中首个元素的位置
show("lst_insert.insert(-1, 'y')", lst_insert)


# 4. 删除
#   remove(x)   根据元素值删除且不返回任何值，找不到抛出 ValueError，是原地修改
#   pop(i)      根据索引删除并返回被删除的元素，不传索引会返回末尾元素，是原地修改
#   clear()     清空列表，原地修改
#   del lst[i]  根据索引删除元素不返回任何值，是原地修改
#   del 列表名   语句，从内存中删除列表

print('\n--- 4. 删除：remove / pop / clear / del ---')

lst_remove = [1, 2, 2, 3]
show('lst_remove（原）', lst_remove)
lst_remove.remove(2)   # 只删除第一个 2
show("lst_remove.remove(2)", lst_remove)
show('lst_remove（改后）', lst_remove)

# remove() 在找不到时会抛出 ValueError
try:
    lst_remove.remove(9)
except ValueError as e:
    show("lst_remove.remove(9)", f'ValueError: {e}')
print('-' * 3)

lst_pop = [1, 2, 3, 4]
show('lst_pop（原）', lst_pop)
show("lst_pop.pop()", lst_pop.pop())             # 删除并返回末尾元素
show('lst_pop（改后）', lst_pop)
show("lst_pop.pop(0)", lst_pop.pop(0))           # 删除并返回下标 0 的元素
show('lst_pop（改后）', lst_pop)
print('-' * 3)

lst_del = [1, 2, 3, 4, 5]
show('lst_del（原）', lst_del)
del lst_del[0]
show("del lst_del[0]", lst_del)
del lst_del[1:3]
show("del lst_del[1:3]", lst_del)
print('-' * 3)

lst_clear = [1, 2, 3]
show('lst_clear（原）', lst_clear)
lst_clear.clear()
show("lst_clear.clear()", lst_clear)


# 5. 修改
#   lst[i] = x   按下标修改元素
#   lst[i:j] = iterable   按切片修改，长度可不一致

print('\n--- 5. 修改：按下标 / 按切片 ---')

lst_mod = [1, 2, 3, 4, 5]
show('lst_mod（原）', lst_mod)
lst_mod[0] = 'a'
show("lst_mod[0] = 'a'", lst_mod)
lst_mod[1:3] = ['x', 'y', 'z']   # 切片修改，长度可不一致
show("lst_mod[1:3] = ['x','y','z']", lst_mod)


# 6. 排序
# sort(key=None, reverse=False)          原地排序，会修改原列表，返回 None，reverse True -> 降序，False -> 升序
# sorted(iter, key=None, reverse=False)  返回新列表，不修改原列表，reverse True -> 降序，False -> 升序

print('\n--- 6. 排序：sort / sorted ---')

lst_sort = [3, 1, 4, 1, 5, 9, 2, 6]
show('lst_sort', lst_sort)
show("sorted(lst_sort)", sorted(lst_sort, reverse=True))             # 不修改原列表
show('lst_sort（sorted 后）', lst_sort)
#lst_sort.sort()                # 原地升序排序
#lst_sort.sort(reverse=True)    # 原地降序排序
lst_sort.sort(reverse=False)    # 原地升序排序
show('lst_sort（sort 后）', lst_sort)
print('-' * 3)

lst_sort2 = [3, 1, 4, 2, 5]
show("lst_sort2.sort(reverse=True)", (lst_sort2.sort(reverse=True), lst_sort2)[1])
show('lst_str', lst_str)

lst_sort3 = ['aaaaa', 'bbb', 'cc', 'd', 'eeeee']
show("sorted(lst_sort3, key=len)", sorted(lst_sort3, key=len))
show('lst_sort3', lst_sort3)


# 7. 反转
#   reverse()      原地反转，返回 None
#   reversed(lst)  内置函数，返回迭代器，不修改原列表

print('\n--- 7. 反转：reverse / reversed ---')

lst_rev = [1, 2, 3, 4, 5]
show('lst_rev（原）', lst_rev)
show("list(reversed(lst_rev))", list(reversed(lst_rev)))   # 不修改原列表
show('lst_rev（reversed 后）', lst_rev)
lst_rev.reverse()
show("lst_rev.reverse()", lst_rev)                          # 原地反转
show('lst_rev（reverse 后）', lst_rev)


# 8. 计数
#   count(x)  统计 x 在列表中出现的次数

print('\n--- 8. 计数：count ---')

show('lst_dup', lst_dup)
print('-' * 3)

show("lst_dup.count(2)", lst_dup.count(2))
show("lst_dup.count(3)", lst_dup.count(3))
show("lst_dup.count(9)", lst_dup.count(9))


# 9. 复制
#   copy()    返回列表的浅拷贝（仅复制最外层，嵌套对象仍是引用）
#   list(lst) 构造函数也能产生浅拷贝
#   lst[:]    切片也能产生浅拷贝

print('\n--- 9. 复制：copy / list() / 切片 ---')

lst_copy = [1, 2, [3, 4]]
show('lst_copy（原）', lst_copy)
lst_copy1 = lst_copy.copy()
lst_copy2 = list(lst_copy)
lst_copy3 = lst_copy[:]
show("lst_copy.copy()", lst_copy1)
show("list(lst_copy)", lst_copy2)
show("lst_copy[:]", lst_copy3)
# 浅拷贝：修改嵌套对象会影响原列表
lst_copy1[2].append(5)
show("lst_copy1[2].append(5) 后 lst_copy", lst_copy)      # 原列表也被改了
show("lst_copy1[2].append(5) 后 lst_copy1", lst_copy1)


# 10. 统计与成员判断
#   sum(lst)   求和（元素需为数字）
#   max(lst)   最大值
#   min(lst)   最小值
#   x in lst   判断 x 是否在列表中
#   x not in lst  判断 x 是否不在列表中

print('\n--- 10. 统计与成员判断：sum / max / min / in ---')

show('lst', lst)
print('-' * 3)

show("sum(lst)", sum(lst))
show("max(lst)", max(lst))
show("min(lst)", min(lst))
show("3 in lst", 3 in lst)
show("6 in lst", 6 in lst)
show("6 not in lst", 6 not in lst)
