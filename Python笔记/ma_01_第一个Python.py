# hello world

print("hello world", end='')  # print("",end='\n') 默认换行 可以用, end=''  使其不换行
print("你好世界 你好python")

# python 不可以用 -- ++   可以用 += -= /= *=
i = 3
i *= 3
print("i=%d" % i)

# 这是单行注释
'''
 这是多行注释 
'''
""""
 这个也是多行注释
"""
#  Python基本元素：数字(int,bool,float)、字符串和变量  没有 c 语言的double 其他基本上一样

# python的运算符和c语言 基本一样
# + 加 -减  *乘 /除  %取余
#
#  //取整   **幂   这个和c语言没有

# print("%d %d"%(num,num_2))  这里不要 写, 不像c语言 printf("%d %d",num,num_2);

# 可以用 type() 查看以个变量的类型

# 变量命名问题:  不能以数字开头  可用 数字 和 字母 下划线  和 汉字（最好不要用）
好好 = 12  # 可以用中文命名 变量
num = 13
num_2 = 2
print(type(好好))
print(好好)

# 0b 开头 二进制的数 0o八进制的数 0x十六进制的数
print("%s" % bin(num))  # 输出二进制的数
print("%s" % oct(num))  # 输出八进制的数
print("%s" % hex(num))  # 输出十六进制的数

# or
print("{:b}".format(num))  # 输出二进制的数
print("{:o}".format(num))  # 输出八进制的数
print("{:x}".format(num))  # 输出十六进制的数 输出 d
# 加一个 :#可以输出 进制
print("{:#x}".format(num))   # 输出 0xd


# 强制转换  python 是int(num)   c语言是 (int)num
# python 还有 str(num) float(num)


# python int类 无范围  c语言有范围  为-2^31<=i<=2^31-1

# python 字符串可以用 "" ''来引出 c语言字符串""  字符用''
# python 还可以用''' '''(其实 他就是字符串 之所以可以当 注释 只不过他没有赋值给一个变量 所以就可以当注释用)
st = '''你好世界 '''
print("st=%s" % st)

# 转义字符和c语言一样  \t tab制表符 \n 换行 \' 输出' \" 输出"  等
print("hello\tworld")
print("\"你好\"")

st2 = "hello world"
st2 = st2 + st
print(st2)          # c语言也可以用 字符串的名字直接输出 printf(str)
c = 40
print(c)            # python也可以直接输出int型和float型和bool型 c语言不行

# 对字符串也可以进行 乘法操作
st = st2 * 3  # st2 * 3 =st2 + st2 +st2
print(st)

# 用[]  取字符串的字符
# 从左向右数 下标从 0 开始 和c语言一样
# python 还可以从右向左数 下标从 -1 开始 -2 -3 ... c语言不能这样


# 使用 [start:end:step] 对字符串进行分割  start 默认为0  end 默认为最后一个 step默认为 1
# [start:end:step] 从 start 提取到 end - 1，每 step 个字符提取一个 如果step 为-1 则反向提取
st3 = 'hello'
print("%s" % st3[::-1])
print(st3[0:4])

# 可以用 len() 看字符串的长度 和 c语言的strlen()一样
print(len(st3))


# 用字符串(其实是一个类 类自己有函数 用 . 使用自带的函数)自带的函数 split() 分割
print(st2.split())
# 用join()合并
ls = ['12', '3', '2']
print(','.join(ls))

# 在输出的字符串前加一个r 可以直接输出
print(r"str\n")