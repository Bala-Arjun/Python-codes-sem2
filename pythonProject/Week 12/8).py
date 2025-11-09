from turtle import *
window = getscreen()
speed(0)
pensize(5)
c=["purple","Green","Blue","yellow","red"]
def dashedlines():
    count=0

    for i in range(10):
        color(c[count%5])
        penup()
        forward(10)
        pendown()
        forward(10)
        count+=1
for i in range(120):
    dashedlines()
    penup()
    setpos(0,0)
    left(3)
done()
