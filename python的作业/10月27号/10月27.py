# 教科书121页 4.1
import random
num = random.randint(0, 9)
i = 0
while 1:
    guess_num = int(input("请猜一个在0~9的数:"))
    i += 1
    if guess_num == num:
        print("预测{}次，你猜中了！".format(i))
        break
    elif guess_num > num:
        print("遗憾，太大了")
    elif guess_num < num:
        print("遗憾，太小了")

# 教科书121页 4.3
def my_gcd(a, b):  # 使用辗转相除法
    while b != 0:
        t = a % b
        a = b
        b = t
    return a

def my_lcm(a, b):
    c = my_gcd(a, b)
    return a * b / c


if __name__ == "__main__":
    print(my_lcm(3, 4))

# 教科书121页 4.4
import random
random.seed(1)
num = random.randint(0, 100)
i = 0
while 1:
    guess_num = int(input("请猜一个在0~100的数:"))
    i += 1
    if guess_num == num:
        print("预测{}次，你猜中了！".format(i))
        break
    elif guess_num > num:
        print("遗憾，太大了")
    elif guess_num < num:
        print("遗憾，太小了")


# 教科书121页 4.6
import random
no_change_num = 0
change_num = 0
for j in range(1000000):
    ls = [0, 1, 0]
    random.shuffle(ls)
    # print(ls)
    guess_num = random.randint(0, 2)
    # 不改变选择
    if ls[guess_num] == 1:
        no_change_num += 1
    else:
        # 改变
        # 如果他开始选的是0 那么主持人公布一个门后是羊的
        # 那么 如果他改变的话 他就一定可以选到车
        # 反知 如果他选的是 1 那么太改的话 那么门后一定是羊
        change_num += 1
print(no_change_num)
print(change_num)
