try:
    result = 2.789123**(int(input("enter number: ")))
    print(result)
except OverflowError as e:
    print(e,'overflow error')
