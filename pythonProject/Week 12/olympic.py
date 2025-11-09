from turtle import *
window =getscreen()
speed(0)
bgcolor("white")
title("Olympic Rings")
pensize(5)
colors = ["blue", "black", "red", "yellow", "green"]
positions = [(-120, 0), (0, 0), (120, 0), (-60, -50), (60, -50)]
for i in range(5):
    penup()
    goto(positions[i])
    pendown()
    color(colors[i])
    circle(50)
done()
