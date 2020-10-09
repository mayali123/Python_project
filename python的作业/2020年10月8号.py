# 93页3.2
time = 365
capacity = 1
b = 0
for i in range(1, time+1):
    if i % 7 not in [1, 2, 3]:
        capacity *= 1.01
print("连续学天%d，365天后的能力值为%f" % (365, capacity))

# 93页3.3
time = 365
num = [10, 15]
for k in num:
    capacity = 1
    b = 0
    for i in range(1, time+1):
        if i % (k+1) != 0:
            if (i-(k+1)*b) % 7 not in [1, 2, 3]:
                capacity *= 1.01
        else:
            b += 1
    print("连续学天%d，休息1天，365天后的能力值为%f" % (k, capacity))


# 93页3.4
st = input("请输入一个数：")
if st == st[::-1]:
    print("这是一个回文数")
else:
    print("这不是一个回文数")
