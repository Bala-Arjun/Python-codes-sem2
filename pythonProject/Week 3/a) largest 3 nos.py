def larg(a,b,c):
    if a > b and a > c:
        print("a greatest")
    if b > c and b > a:
        print("b greatest")
    if c > a and c > b:
        print("c greatest")
a=float(input("enter 1st no"))
b=float(input("enter 2nd no"))
c=float(input("enter 3rd no"))
larg(a,b,c)
