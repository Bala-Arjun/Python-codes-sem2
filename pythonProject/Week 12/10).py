from turtle import *
w=getscreen()
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
bgcolor("black")
speed(0)
for i in range(360):
    pencolor(colors[i % 6])
    forward(i)
    left(59)
done()
