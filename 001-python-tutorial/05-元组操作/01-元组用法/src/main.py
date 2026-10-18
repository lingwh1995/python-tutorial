# -*- coding: utf-8 -*-
"""python 中的元组用法

@author lingwh
@date 2026/10/14 15:29
"""

# 1. 封装函数的多个返回值
def calc(a:int, b:int) -> int:
    """使用元组封装函数的多个返回值

    Java 想返回多值，必须封装对象，Python 直接靠元组，非常简洁。
    :param a: 参数 a
    :param b: 参数 b
    :return: 返回值
    """
    s = a + b
    p = a * b
    return s, p  # 等价 return (s,p)

sum_val, product = calc(3,5) # 元组解包
print(sum_val, product)

# 2. 用于字典的 key
# 字典的 key 要求必须是可哈希类型，list 可变，不能当 key，元组里面全部元素不可变，就能作为字典 key。用坐标作为 key，适合存储二维坐标、经纬度这种成对固定组合。
points = {
    (10, 20): "A点",
    (30, 40): "B点"
}
print(points[(10, 20)])

# 3. 保护数据，防止意外修改
# 数据写死，不希望代码其他地方不小心修改，如 常量配置、坐标、RGB 颜色、月份、星期。如果用 list，别的地方一不小心写`week[0]=""`就改坏了；元组直接禁止修改，更安全。
week = ("周一", "周二", "周三", "周四", "周五", "周六", "周日")
rgb_red = (255, 0, 0)

# 4. 序列解包、并行赋值
# 并行赋值，底层元组
a, b, c = 10, 20, 30
# 交换变量（经典用法）
x, y = 1, 2
x, y = y, x
print(x, y) # 2, 1

# 5. 用作函数不定长参数 *args
def add(*args) -> int:
    """用作函数不定长参数

    *args 拿到的参数，类型就是元组
    """
    print(type(args)) # tuple
    return sum(args)

add(1, 2, 3, 4)

# 6. 作为集合 set 里面的元素
# set 的元素也要求可哈希。list 不能放进集合，元组可以。
s = set()
s.add( (1, 2) )

# 7. 数据库查询返回结果
# 很多 Python 数据库驱动（sqlite3 等）查询出来的每一行数据，默认是元组。一行记录，字段顺序固定，不会随意改动。

# 8. 什么时候用 tuple /list
# tuple：数据不会修改，打包一组固定数据、多返回值、字典 key、常量
# list：后续需要增、删、修改元素

# 元组不可变指不能替换里面对象，但内部列表 [2,3] 本身可变，可以 append，这种里面带可变对象的元组不能做字典 key。
t = (1, [2, 3])