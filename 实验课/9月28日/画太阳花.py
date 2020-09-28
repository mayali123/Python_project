from turtle import *
color("yellow")
begin_fill()
while True:
    forward(200)
    left(132)
    if abs(pos())<1:
        break
end_fill()
done()
