import random
random.seed(1)
num = random.randint(0, 100)
i = 0
while 1:
    st = eval(input("请猜一个在0~100的数:"))
    while st%1!=0:
        print('输入内容必须为整数！')
        st = eval(input("请猜一个在0~100的数:"))
    guess_num = st
    i += 1
    if guess_num == num:
        print("预测{}次，你猜中了！".format(i))
        break
    elif guess_num > num:
        print("遗憾，太大了")
    elif guess_num < num:
        print("遗憾，太小了")
