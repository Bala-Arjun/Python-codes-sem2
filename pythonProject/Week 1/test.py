x=str(input("enter c or f "))
f=5
c=5
if x=='c':
    print("enter c value")
    c=float(input())
    f=9/5*c+32
    print(f)
else:
    print("enter f value")
    f=int(input())
    c=5/9*(f-32)
    print(c)