try:
    f=open("idk", "r")
except FileNotFoundError as e:
    print(e)
finally:
    print("...finally block executed...")