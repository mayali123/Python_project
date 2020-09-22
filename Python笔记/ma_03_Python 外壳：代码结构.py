# 可以用 连接符 \ 增加可读性
st = "hello " + \
    " world"
print(st)

# 分支语句 if else elif
# python if语句  if 条件语句:   c语言 if(条件语句)    elif 是 else if的结合
if 0:
    print(st)
else:
    print("你好世界")
#  c语言的比较操作符(如 != == > < >= <=)python也有  python 还多了一个 in 属于
if 'h' in ['H', 'h']:
    print('h')

# python  用 and or not 分别代替 c语言的 && || !
# python if语句 其他用法 和c语言一样
if 1 or not 1:
    print(True)
else:
    print(False)

# 循环  python 的循环语句 只有 for while  没有 c语言中的do while 循环
# python 的while   和c语言基本上一样
# python的 while 条件语句:  c语言 while(条件语句)
# 退出循环 break continue 和 c语言一样
i = 2
while i >= 0:
    print('hhh')
    if i == 1:
        break
    i -= 1

# python 的 for  和 c语言 for 非常不同  python 的for 一般和 in 一起用 实现迭代
# in 后面 可以是 列表、字符串、元组、字典、集合等
# 元组 或者 列表 在一次迭代过程产生一项，而字符串迭代会产生一个字符
# 对一个字典 进行迭代将返回字典中的键 字典{"键":"值","键":"值"...}
# 也可以通过 字典名.values() 对值进行迭代  也可以用 .items()返回键值对
# 字典也是一个类 类有内部函数 用.函数名 调用
ls = ['hhhh', 'llll', 'nihao']          # 列表
dr = {"12": "2", "33": "22"}            # 字典
for a in dr.items():
    print(a)
    # print(type(a))


# python 的else 可以和 while for 一起用  c语言不可以 感觉这个不常用
cheeses = ["HE"]
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:  # 没有break表示没有找到奶酪
    print('This is not much of a cheese shop, is it?')

# range(start,end,step) 和分片[]有点像 start 默认值为0 step默认值为1
# step=-1 可以反向取值
for i in range(20, 2, -1):
    print(i, end=' ')
