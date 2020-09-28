from turtle import *
length=float(input("请输入用一个长度:"))
pensize(2)
pencolor("blue")
for i in range(3):
    setheading(-(120*i)+30)
    forward(length)
penup()
goto(length*2*(3**(1/2))/3, 0)
pendown()
for i in range(3):
    setheading(-(120 * i) - 150)
    forward(length)
done()
