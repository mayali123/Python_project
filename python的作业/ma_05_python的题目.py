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
from turtle import *
pencolor("blue")
for i in range(99):
    setheading((i % 4)*90+90)
    forward(3+3*i)
done()
