f=open("text","r")
n=int(input("enter no of lines: "))
for i in range (n,1,-1):
    c=f.readline(n)
    print(c,end="")
    if c == '':
        break
