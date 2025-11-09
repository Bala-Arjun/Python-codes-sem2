from curses.textpad import rectangle
from turtle import *
window = getscreen()
speed(0)
pensize(5)
c=["Red","Black","Blue","Green"]
count=0
for i in range(12):
    color(c[count%4])
    circle(100)
    right(30)
    count+=1
done()
