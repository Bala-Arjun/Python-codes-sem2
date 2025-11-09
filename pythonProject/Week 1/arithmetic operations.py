def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
while True:
    print("1=Add","2=Sub","3=mul","4=div","5=exit")
    choice=int(input("enter choice"))
    if choice==5:
        break
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    if choice==1:
        add(a,b)
    if choice==2:
        sub(a,b)
    if choice==3:
        mul(a,b)
    if choice==4:
        div(a,b)

