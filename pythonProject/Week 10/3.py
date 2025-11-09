try:
    class Person:
        def __init__(self, name):
            self.name = name


    p = Person("Bala")
    print(p.age)
except AttributeError as e:
    print(e)