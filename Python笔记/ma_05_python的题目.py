# # python书P56的2.7
# from turtle import *
# pensize(2)
# pencolor("blue")
# for i in range(3):
#     setheading(-(120*i)+30)
#     forward(100)
# penup()
# goto(100*2*(3**(1/2))/3, 0)
# pendown()
# for i in range(3):
#     setheading(-(120 * i) - 150)
#     forward(100)
# done()

# python书P57的2.8
# from turtle import *
# pencolor("blue")
# for i in range(99):
#     setheading((i % 4)*90+90)
#     forward(3+3*i)
# done()

# a = int(input())
# num = 0
# if a == 0:
#     num = 1
# else:
#     while a >= 1:
#         num_1 = 1
#         i = 1
#         while i <= a:
#             num_1 *= i
#             i += 1
#         num += num_1
#         a -= 1
# print(num)

# st = input().split(" ")
# a = int(st[0])
# st1 = st[1]
# str_len = len(st1)
# for i in range(str_len):
#     if int(st1[i]) != 0:
#         print("%d*%d^%d+" % (int(st1[i]), a, str_len-i-1), end='')
# print('\b')

# st = input().split(" ")
# a = int(st[0])
# b = int(st[1])
# print(a+b)
# print("Hello, World!")

def is_palindrome(st_num):
    if int(st_num) < 10:
        return 0
    k = 1
    for index in range(len(st_num)):
        if st_num[index] != st_num[len(st_num)-1-index]:
            k = 0
            break
    return k


st = int(input())
st1 = int(input(), st)
num = st1
j = 0
str_n = str(num)
while j <= 30 and not is_palindrome(str_n):
    num += int(str_n[::-1])
    j += 1
    str_n = str(num)

if j > 30:
    print("Impossible!")
else:
    print("STEP=%d" % j)
