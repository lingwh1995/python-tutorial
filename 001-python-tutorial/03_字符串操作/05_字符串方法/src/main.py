# -*- coding: utf-8 -*-
"""python 字符串常用方法

:author: lingwh
:date: 2026/7/1 15:30
"""


# 前置知识：字符串是不可变对象，所有字符串方法都不会修改原字符串，而是返回一个新的字符串。
# 例如 s.replace(...) 会返回替换后的新字符串，s 本身保持不变。

# 示例数据
s = 'pythonpython'          # 基础示例串
s_tab = 'p\tython,python,python,pytho n'  # 含制表符、逗号、空格
s_newline = 'pyth\non'      # 含换行符
filename = 'a.txt'          # 文件名
fruits = ['apple', 'banana', 'cherry']
s_words = 'pythonpython pythonpython'
s_align = 'python'
s_spaced = '     python     '
s_hello = 'hello'


def show(title, result) -> None:
    """
        统一输出格式，让输入和结果一目了然。
    """
    print(f'{title:<35} -> {result!r}')


# 1. 长度
print('\n--- 1. 长度：len ---')

show("len(s)", len(s))  # 字符串长度
show("len(s_tab)", len(s_tab))  # 包含制表符、逗号、空格
show("len(s_newline)", len(s_newline))  # 包含换行符
show("len(filename)", len(filename))  # 文件名长度
show("len(fruits)", len(fruits))  # 列表长度
show("len(s_words)", len(s_words))  # 包含空格的字符串长度
show("len(s_align)", len(s_align))  # 包含空格的字符串长度
show("len(s_spaced)", len(s_spaced))  # 包含空格的字符串长度
show("len(s_hello)", len(s_hello))  # 字符串长度


# 2. 查找
#   find()  找不到返回 -1（偏向索引查询）
#   index() 找不到会抛出 ValueError 异常（偏向强制要求必须存在）
#   rfind() / rindex() 与 find() / index() 的区别只是查找方向：
#       前者从右向左找，后者从左向右找；找到时返回的索引位置相同。

print('\n--- 2. 查找：find / index / rfind / rindex ---')

show('s', s)
print('-' * 3)

show("s.find('h')", s.find('h'))                 # 第一个 h 的索引
show("s.find('th')", s.find('th'))               # 子串 th 的索引
show("s.find('j')", s.find('j'))                 # 不存在，返回 -1
show("s.find('n')", s.find('n'))                 # 第一个 n 的索引
show("s.find('n', 1, 5)", s.find('n', 1, 5))     # 在切片 [1, 5) 中查找 n 的索引

show("s.index('n')", s.index('n'))

# index() 在找不到时会抛出 ValueError，演示如下
try:
    show("s.index('n', 1, 5)", s.index('n', 1, 5))
except ValueError as e:
    show("s.index('n', 1, 5)", f'ValueError: {e}')

show("s.rfind('n')", s.rfind('n'))               # 从右侧找第一个 n
show("s.rfind('n', 1, 5)", s.rfind('n', 1, 5))   # 从右侧开始，在切片 [1, 5) 中查找 n 的索引

show("s.rindex('n')", s.rindex('n'))

# rindex() 在找不到时同样会抛出 ValueError
try:
    show("s.rindex('n', 1, 5)", s.rindex('n', 1, 5))
except ValueError as e:
    show("s.rindex('n', 1, 5)", f'ValueError: {e}')


# 3. 替换
#   replace(old, new)        替换所有匹配项
#   replace(old, new, count) 最多替换 count 次

print('\n--- 3. 替换：replace ---')

show('s', s)
print('-' * 3)

show("s.replace('h', 'H')", s.replace('h', 'H'))
show("s.replace('python', 'PYTHON')", s.replace('python', 'PYTHON'))
show("s.replace('python', 'PYTHON', 1)", s.replace('python', 'PYTHON', 1))
show("original string s", s)


# 4. 计数
#   count(sub)             统计 sub 在字符串中出现的次数
#   count(sub, start, end) 统计 sub 在切片 [start, end) 中出现的次数

print('\n--- 4. 计数：count ---')

show('s', s)
print('-' * 3)

show("s.count('p')", s.count('p'))
show("s.count('p', 0, 6)", s.count('p', 0, 6))


# 5. 分割
#   split(sep)             按 sep 分割，返回列表
#   split(sep, maxsplit)   最多分割 maxsplit 次
#   split()                按任意空白字符分割
#   splitlines()           按行分割，效果同 split('\n')
#   partition(sep)         只分成三段：(前, sep, 后)，保留分隔符

print('\n--- 5. 分割：split / splitlines / partition ---')

show('s_tab', s_tab)
show('s_newline', s_newline)
show('filename', filename)
print('-' * 3)

show("type(s_tab.split(','))", type(s_tab.split(',')))
show("s_tab.split(',')", s_tab.split(','))
show("s_tab.split(',', 1)", s_tab.split(',', 1))
show("s_tab.split('th')", s_tab.split('th'))     # 分隔符会被丢弃
show("s_tab.split()", s_tab.split())             # 按任意空白分割
show("s_newline.split('\\n')", s_newline.split('\n'))
show("s_newline.splitlines()", s_newline.splitlines())

# partition 常用于拆分文件名
show("s.partition('th')", s.partition('th'))
show("filename.partition('.')", filename.partition('.'))


# 6. 连接
#   sep.join(iterable) 用 sep 把可迭代对象里的每个子元素连接起来
#   注意：join 的是字符串序列，常用于列表、元组、字符串本身

print('\n--- 6. 连接：join ---')

show('s', s)
show('fruits', fruits)
print('-' * 3)

show("'-'.join(s)", '-'.join(s))
show("'-'.join(fruits)", '-'.join(fruits))

# hello => ['h', 'e', 'l', 'l', 'o']
show("list(s_hello)", list(s_hello))
show("'-'.join(s_hello).split('-')", '-'.join(s_hello).split('-'))


# 7. 前缀与后缀判断
#   startswith(prefix) 是否以 prefix 开头
#   endswith(suffix)   是否以 suffix 结尾
#   二者都返回布尔值 True / False

print('\n--- 7. 前缀与后缀：startswith / endswith ---')

show('s', s)
print('-' * 3)

show("s.startswith('p')", s.startswith('p'))
show("s.startswith('py')", s.startswith('py'))
show("s.endswith('n')", s.endswith('n'))
show("s.endswith('on')", s.endswith('on'))


# 8. 大小写转换
#   upper()      全部转大写
#   lower()      全部转小写
#   title()      每个单词首字母大写
#   capitalize() 只有第一个单词首字母大写

print('\n--- 8. 大小写转换：upper / lower / title / capitalize ---')

show('s', s)
print('-' * 3)

show('s.upper()', s.upper())
show('s.lower()', s.lower())
show('s_words.title()', s_words.title())
show('s_words.capitalize()', s_words.capitalize())


# 9. 对齐
#   center(width, fillchar) 居中
#   ljust(width, fillchar)  左对齐
#   rjust(width, fillchar)  右对齐
#   默认 fillchar 为空格，可指定其他字符

print('\n--- 9. 对齐：center / ljust / rjust ---')

show('s_align', s_align)
print('-' * 3)

show('s_align.center(20)', f'|{s_align.center(20)}|')
show("s_align.center(20, '*')", f"|{s_align.center(20, '*')}|")
show('s_align.ljust(20)', f'|{s_align.ljust(20)}|')
show("s_align.ljust(20, '*')", f"|{s_align.ljust(20, '*')}|")
show('s_align.rjust(20)', f'|{s_align.rjust(20)}|')
show("s_align.rjust(20, '*')", f"|{s_align.rjust(20, '*')}|")


# 10. 去除空白
#   strip()   去除两端空白
#   lstrip()  去除左端空白
#   rstrip()  去除右端空白

print('\n--- 10. 去除空白：strip / lstrip / rstrip ---')

show('s_spaced', s_spaced)
print('-' * 3)

show('s_spaced.strip()', f'|{s_spaced.strip()}|')
show('s_spaced.lstrip()', f'|{s_spaced.lstrip()}|')
show('s_spaced.rstrip()', f'|{s_spaced.rstrip()}|')