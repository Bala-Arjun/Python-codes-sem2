from turtle import *
pendown()
speed(0)
color("purple")
for i in range(360):
    pendown()
    for i in range(4):
        forward(90)
        left(90)
    penup()
    right(2)
done()