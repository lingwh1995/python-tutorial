# -*- coding: utf-8 -*-
"""python 中的列表嵌套

1. 什么是嵌套列表
   列表中的元素可以是任意类型，当然也可以是另一个列表，这就是嵌套列表。
2. 常见的嵌套列表
   最常见的是二维列表（列表的列表），常用来表示矩阵、表格等。
3. 注意事项
   嵌套列表中存放的是内层列表的引用，多个位置引用同一个内层列表时，修改其中一处，所有引用都会跟着变。

@author lingwh
@date 2026/10/19 9:58
"""
import random


def show(title, result) -> None:
    """
    统一输出格式，让输入和结果一目了然。
    """
    print(f'{title:<40} -> {result!r}')


# 示例数据
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
students = [
    ['Tom', 18, 90.5],
    ['Jerry', 17, 88.0],
]


# 1. 创建嵌套列表
print('\n--- 1. 创建嵌套列表 ---')

# 字面量直接写、列表推导式按行生成
show('matrix', matrix)
show('students', students)
# 普通元素和列表可以混着放
show("['a', [1, 2], 'b']", ['a', [1, 2], 'b'])

# 经典坑：[[0] * 3] * 3 中的三行是同一个内层列表的引用（浅拷贝）
lst_bad = [[0] * 3] * 3
show('lst_bad', lst_bad)
lst_bad[0][0] = 1
show('lst_bad', lst_bad)                        # 三行第一列全部变成 1

# 正确做法：列表推导式为每一行创建新的列表
lst_good = [[0] * 3 for _ in range(3)]
show('lst_good', lst_good)
lst_good[0][0] = 1
show('lst_good', lst_good)                      # 只有第一行变化


# 2. 访问嵌套元素
print('\n--- 2. 访问嵌套元素 ---')

# lst[i]      取出第 i 个元素（可能是内层列表）
# lst[i][j]   先取第 i 个内层列表，再取其中第 j 个元素，多级索引逐层深入
show('matrix', matrix)
show('matrix[0]', matrix[0])                     # 第一行，拿到的是内层列表
show('matrix[0][0]', matrix[0][0])               # 第一行第一列
show('matrix[2][1]', matrix[2][1])               # 第三行第二列
show('matrix[-1][-1]', matrix[-1][-1])           # 负索引同样适用：最后一行最后一列
show('students[0][0]', students[0][0])

# 嵌套可以更深，逐层索引即可
lst_deep = [1, [2, [3, 4]]]
show('lst_deep[1][1][0]', lst_deep[1][1][0])     # 3

# 索引越界会抛出 IndexError
try:
    show('matrix[3]', matrix[3])
except IndexError as e:
    show('matrix[3]', f'IndexError: {e}')


# 3. 遍历嵌套列表
print('\n--- 3. 遍历嵌套列表 ---')

for row in matrix:
    print(row)

print('-' * 3)

# 双层 for 循环：外层遍历行，内层遍历行中的元素
for row in matrix:
    for ele in row:
        print(ele, end=' ')
print()

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=' ')
print()

print('-' * 3)

# enumerate 可以同时拿到行号和行内容
for i, row in enumerate(matrix):
    print(f'第 {i} 行: {row}')


# 4. 修改嵌套元素
print('\n--- 4. 修改嵌套元素 ---')

score_table = [
    ['Tom', 90],
    ['Jerry', 88],
]
show('score_table', score_table)
# lst[i][j] = x   定位到内层列表再赋值
score_table[0][1] = 95
show('score_table[0][1] = 95', score_table)
# lst[i] = [...]  可以替换整行
score_table[1] = ['Spike', 60]
show("score_table[1] = ['Spike', 60]", score_table)


# 5. 嵌套列表的切片
print('\n--- 5. 嵌套列表的切片 ---')

show('matrix', matrix)
# 切片作用在外层：取出的是「行」，结果还是嵌套列表
show('matrix[0:2]', matrix[0:2])                 # 前两行
show('matrix[::-1]', matrix[::-1])               # 行序反转
# 切片作用在内层：取出的是行中的「元素」
show('matrix[0][0:2]', matrix[0][0:2])           # 第一行的前两个元素
show('[row[0] for row in matrix]', [row[0] for row in matrix])   # 推导式取第一列


# 6. 展平嵌套列表
print('\n--- 6. 展平嵌套列表 ---')

show('matrix', matrix)

lst_flat = []
# 双层 for 展平
for row in matrix:
    for ele in row:
        lst_flat.append(ele)
show('lst_flat', lst_flat)

# 列表推导式展平
lst_flat = [ele for row in matrix for ele in row]
show('lst_flat', lst_flat)

# sum(list, []) 也能展平，了解即可，可读性一般
show('sum(matrix, [])', sum(matrix, []))


# 7. 应用：矩阵转置（行列互换）
print('\n--- 7. 应用：矩阵转置 ---')

show('matrix', matrix)

# 双层列表推导式：外层遍历列号，内层逐行取出该列元素
matrix_transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# 推导式转置
show('matrix_transpose', matrix_transpose)

# zip(*matrix) 按列打包，效果相同
show('zip(*matrix)', [list(row) for row in zip(*matrix)])


# 8. 案例：随机分配办公室（将 8 个老师随机分配到 3 个教室）
print('\n--- 8. 案例：随机分配办公室 ---')
students = ['Tom', 'Jerry', 'Alice', 'Jack', 'Bob', 'John', 'David', 'Smith']
classroom = [[], [], []]
for student in students:
    classroom_id = random.randint(0, len(classroom) - 1)
    classroom[classroom_id].append(student)

print(classroom)