import turtle
def koch(size, n ):
    if n ==0 :
        turtle.fd(size)
    else:
        for i in [0,60,-120,60]:
            turtle.left(i)
            koch(size/3, n-1)
turtle.penup()
turtle.goto(-300,200)
turtle.pendown()
for i in range(3):
    koch(600,3)
    turtle.right(120)
turtle.hideturtle()
