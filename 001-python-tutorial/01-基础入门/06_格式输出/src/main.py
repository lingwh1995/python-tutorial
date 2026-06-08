# -*- coding: utf-8 -*-
"""
@author lingwh
@desc python 中的格式化输出
@date 2026/6/5 17:37

python 中的格式化输出

1. % 占位符输出 ⭐⭐⭐
     语法格式
       单个变量 "字符串 % 变量"，多个变量用元组 % (a,b)
     %d  以整数输出
       %3d 输出时，数据占3个字符宽度
       %03d 输出时，数据占3个字符宽度，当数字不足三个字符时，前缀补0  python-001-basic
       %-3d 输出时，数据占3个字符宽度， 左对齐
     %f  以小数输出
       %.3f 小数点后保留位数是3位
     %s  以字符串输出
2. f_string输出 ⭐⭐⭐⭐⭐
     语法格式
       f'字符串 {数据}'
     注意事项
       f'字符串 {数据}' 是有返回值的
3. str.format 输出 ⭐⭐⭐
4. format_map 输出 ⭐
     应用场景
       适合批量字典数据

常用格式符号速查表

符号	        作用	        示例
:d	        十进制整数	f"{5:d}"
:f	        浮点数	    f"{3.14:.2f}"
:%	        百分比	    f"{0.75:.0%}" →75%
:,	        千位分隔	    f"{12345:,}" →12,345
<	        左对齐	    {x:<8}
>	        右对齐	    {x:>8}
^	        居中	        {x:^8}
0	        数字补零	    {3:05d} →00003
"""

# 1.1. 使用占位符输出一个值
age = 20
print('输出一个值: %d' % age)
# 1.2. 使用占位符输出多个值，两个包括两个以上的值要使用括号括起来
name = 'zhangsan'
score = 100
print('使用占位符输出两个值: 姓名: %s, 年龄: %d' % (name, age))
print('使用占位符输出三个值: 姓名: %s, 年龄: %d, 分数: %d' % (name, age, score))
# 1.3. 常用占位符输出示例
# %d 以整数输出
a = 1
b = 12345
pi = 3.14159
print('%d' % a)
# %5d 以整数输出，数据占5个字符宽度，当数字不足5个字符时，左补0
print('%5d' % a)
# %3d 以整数输出，数据占3个字符宽度，如果目标数据长度超过3则直接原样输出原始值
print('%3d' % b)
# %05d 以整数输出，且数据占5个字符宽度，当数字不足5个字符时，左补0
print('%05d' % a)
# %-5d 以整数输出，且数据占5个字符宽度，当数字不足5个字符时，右补空格
print('%-5d' % a)
# %f 以浮点数输出，四舍五入后保留六位小数
print('%f' % pi)
# %.3f 以浮点数输出，四舍五入后保留三位小数
print('%.3f' % pi)
# %.3f 以浮点数输出，四舍五入后保留三位小数
print('%.3f' % a)
print('-' * 50)

# 2. 使用 f-string 输出
# 基本使用
print(f'使用f-string输出: 姓名: {name}, 年龄: {age}, 分数: {score}')
# 获取 f_string 返回值
f_string_rt = f'使用f-string输出: 姓名: {name}, 年龄: {age}, 分数: {score}'
print('f_string返回值: %s' % f_string_rt)
# 直接运算
print(f"五年后年龄：{age + 5}")
# 调用方法
print(f"姓名大写：{name.upper()}")
# 精细格式控制（和 format 格式符通用）
pi = 3.14159
money = 99999.99
# .3f 以浮点数输出，四舍五入后保留三位小数
print(f"圆周率：{pi:.3f}")
# .1% 以百分比输出，四舍五入后保留1位小数（乘以100后保留n位小数）
print(f"通过率：{0.8658:.1%}")
# 整数千位分隔
print("整数千位分隔:{:,}".format(1234567))
# 整数千位分隔 + 小数四舍五入后保留两位
print(f"整数千位分隔 + 小数四舍五入后保留两位：{money:,.2f}")
# 对齐填充：宽度10，左/右/居中
print(f"姓名|{name:<10}|")  # 左对齐
print(f"姓名|{name:>10}|")  # 右对齐
print(f"姓名|{name:^10}|")  # 居中
# 补0数字
print(f"编号：{6:04d}")
# 二进制 / 十六进制
n = 10
print(f"二进制:{n:b}, 十六进制:{n:x}, 大写:{n:X}")
# 格式化打印多行
name = '小明'
info = f"""
====用户信息====
姓名：{name}
年龄：{18}
积分：{1000:,}
"""
print(info)
print('-' * 50)

# 3. 使用 str.format 输出
# 位置传参
print('使用str.format输出: 姓名: {}, 年龄: {}, 分数: {}'.format(name, age, score))
# 下标索引传参
print('使用str.format输出: 年龄: {1}, 姓名: {0}, 分数: {2}'.format(name, age, score))
# 关键字传参
print('使用str.format输出: 姓名: {n}, 年龄: {a}, 分数: {s}'.format(n=name, a=age, s=score))

name = 'lisi'
num = 3.1415926
# 调用方法
print("姓名大写：{}".format(name.upper()))       # 写法1：参数处提前调用方法（最常用）
print("姓名大写：{0.upper}".format(name))      # 写法2：用索引链式调用 .
print("姓名大写：{n.upper}".format(n=name))    # 写法3：关键字链式调用

# 保留2位小数
print("π = {:.2f}".format(num))
# 占8字符宽度，居中、补0
print("数字:{:0^8.2f}".format(num))
# 整数千位分隔
print("金额:{:,}".format(1234567))
print('-' * 50)

# 4. 使用 format_map 输出
user = {"name": "lisi", "age": 28, "score": 92}
print("姓名:{name}, 年龄:{age}, 分数:{score}".format_map(user))
