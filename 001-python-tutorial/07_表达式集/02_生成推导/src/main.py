# -*- coding: utf-8 -*-
"""python 的生成器表达式

1. 生成器表达式概述
   - 生成器表达式也属于推导式的一种
   - 返回值是生成器对象，生成器对象是可迭代对象 (iterable)，可以传给 list()、set()、tuple() 转换成对应容器。
2. 生成器表达式特性
   - 惰性求值，按需产出，不会一次计算出所有结果，只在用要的时候才生成一个元素，用完就丢弃，内存开销极低。
3. 生成器表达式应用场景
   - 超大序列、无限序列
     比如读取超大日志文件、逐行解析，或者理论上无限的数据流，根本不可能全部放进列表。列表推导直接 GG，生成器可以处理。
   - 读取大文件，一行一行处理，不一次性把整个文件读进内存
     (line.strip() for line in open("big.txt"))
   - 只遍历一次时，不需要二次读取
     这种场景我们只遍历一次数据，没必要花内存代价存完整列表，如 sum(x for x in range(10_000_000))
   - 管道流式处理
     可以把多个生成器串起来，做数据流水线：一个生成器输出，作为下一个生成器的输入，全程流式、低内存。
4. 语法格式
   # 基础语法
   (expr for i in iter)
   def gen():
       for i in iter:
           yield expr
   g = gen()

   # 使用条件筛选结果作为生成器对象元素
   (expr for i in iter if condition)
   def gen():
       for i in iter:
           if condition:
               yield expr
   g = gen()

   # 使用三目运算结果作为生成器对象元素
   (expr1 if condition else expr2 for i in iter)
   def gen():
       for i in iter:
           if condition:
               val = expr1
           else:
               val = expr2
           yield val
   g = gen()

@author lingwh
@date 2026/10/26 11:06
"""


# 生成器表达式 () generator
# 基本格式
nums = (x for x in range(5))
print(list(nums))

# 使用条件筛选结果作为生成器元素
even_nums = (x for x in range(5) if x % 2 == 0)
print(list(even_nums))

# 使用表达式计算结果作为生成器元素
squares = (x * x for x in range(5))
print(list(squares))

# 使用三目运算结果
nums = (f'{x}-偶' if x % 2 == 0 else f'{x}-奇' for x in range(5))
print(list(nums))
print('---')

# 遍历生成器对象
# 1. for 循环遍历
nums = (x for x in range(5))
# 第一次遍历能取到值
for item in nums:
    print(item)
# 第二次遍历取不到值
for item in nums:
    print(item)
print('---')

# 2. while 循环遍历
nums = (x for x in range(5))
while True:
    try:
        val = next(nums)
        print(val)
    except StopIteration:
        break
print('---')

# 3. while 循环遍历
nums = (x for x in range(5))
while True:
    val = next(nums, None)
    if val is None:
        break
    print(val)

# 4. enumerate 同时拿索引
nums = (x ** 2 for x in range(5))
for idx, val in enumerate(nums):
    print(idx, val)