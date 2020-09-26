# -*- coding = utf-8 -*-
# @Time :  19:40
# @Author :mayali123
# @File : ma_06_函数和文件操作.py
# @Software : PyCharm

# 函数的基本操作
# 使用def定义一个函数 def 函数名(参数):
def add(a, b):
    return a+b


print(add(1, 2))
# python 和c语言不同的地方
# 可以返回多个参数
def add_reduce(a, b):
    return a+b, a-b


# a, b = add_reduce(2, 1)
# print(a, b)
#
#
def print_line():
    print("-"*30)


def print_line_num(num):
    i = 0
    while i < num:
        print_line()
        i += 1


print_line_num(2)


def add(a, b, c):
    return a+b+c


print(add(1, 23, 4))
def average(a, b, c):
    return add(a, b, c)/3


print(average(1, 2, 3))

# 局部变量 和全局变量

a = 100  # 全局变量


def test():
    print("第一个a=%d" % a)


def test1():
    global a  # 使用全局变量
    print("第二个a=%d" % a)
    a = 300
    print("第二个a=%d" % a)


test()
test1()

print("外面的a=%d" % a)