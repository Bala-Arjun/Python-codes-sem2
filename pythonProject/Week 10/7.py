while True:
    try:
        a = [1, 2, 3]
        x = int(input("Enter a number: "))
        result = 100 / x
        print(a[x])
    except (ValueError, ZeroDivisionError, IndexError) as e:
        print(e)
    else:
        print(f"the value at index is : {a[x]} and the result is :{result}")
