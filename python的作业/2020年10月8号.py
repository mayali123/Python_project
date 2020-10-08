
st = input("请输入一个五位数：")
if st[:3] == st[:-4:-1]:
    print("这是一个回文数")
else:
    print("这不是一个回文数")


#time 连续学习的天数
time = 365
after_up = (1+0.01)**(time-3)
print('连续学'+str(time)+'天，持续学365天之后之后的能力值为'+str(after_up))


# time 连续学习的天数
time = 10
after_up = ((1+0.01)**(time-3))**(365//10)
remainder = 365 % 10
after_up += (1+0.01)**(remainder-3)
print('连续学'+str(time)+'天，持续学365天之后的能力值为'+str(after_up))
