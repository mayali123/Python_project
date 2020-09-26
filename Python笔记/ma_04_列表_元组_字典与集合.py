# 列表_元组_字典与集合

# 列表和元组很像
# 元组但是 被创建之后不能修改了 列表可以修改
a = ("hello ", "world")

# 列表和元组的元素 可以任何 Python 类型 甚至是列表
ls = ["123", "hello ", 2, 2.3, True]     # 创建列表
ls1 = list()        # 创建一个空列表

# 可以使用 list() 将其他的数据类型转成 链表
print(list('cat'))
print(list(a))  # 将 元组转为 链表

# 字符串的内部函数 split() 进行分割 返回 链表
ls3 = '1/2/3/4'
print(type(ls3.split('/')))


# 使用[] 取值 和字符串一样
# 从左向右数 下标从 0 开始 和c语言一样
# python 还可以从右向左数 下标从 -1 开始 -2 -3 ...
print(ls)
print(ls[1])
ls[1] = '你好'
print(ls[1])

# 使用 [start:end:step] 对列表进行分割  start 默认为0  end 默认为最后一个 step默认为 1
# [start:end:step] 从 start 提取到 end - 1，每 step 个字符提取一个 如果step 为-1 则反向提取

# 内部函数 append(object) 在list尾部 添加一个元素
ls.append('False')
print(ls)

# +=是一个一个添加的
ls += 'NOT'
print(ls)

# 插入 del删除  del 不是list的内部函数  一定要注意
del ls[-3:]
print(ls)

# 用 list内部函数insert(index,object)  index位置 object元素

ls.insert(1, "hello world")
print(ls)

# del不是list的内部函数
# python 的内部语句
del ls[0]
print(ls)

# remove移除 特定的值
ls.remove('hello world')
print(ls)

# pop(index) 弹出指定index位置的的元素 index 从0开始
ls.pop(2)
print(ls)

# 字典 {key:value}  dictionary 字典
# dict() 可以将其他的数据类型转为 字典
# 字典的 key 不能相同

dic = {'1': '一', '2': '二'}

# 使用keys()获取所有的键  values()获取所有的值   itmes()获取所有的键和值
print(dic.keys())
print(dic.values())
print(dic.items())

# 通过[key]对 value进行修改
dic['1'] = 'one'
print(dic)
# update()合并 字典
di = {'3': '3'}
di.update(dic)
print(di)

