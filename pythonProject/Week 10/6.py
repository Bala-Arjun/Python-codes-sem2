while True:
    try:
        base=float(input('enter the base: '))
        power=int(input("enter the power: "))
        quotient=int(input("enter the quotient: "))
        x=(base**power)/quotient
        print(x)
    except OverflowError as e:
        print('error:',e)
    except ZeroDivisionError as e:
        print('error:',e)