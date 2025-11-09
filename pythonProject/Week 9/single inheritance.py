class Parent:
    def show(self):
        print("This is the parent class")

class Child1(Parent):
    def child1_func(self):
        print("This is child 1")

class Child2(Parent):
    def child2_func(self):
        print("This is child 2")

c1 = Child1()
c2 = Child2()
c1.show()
c1.child1_func()
c2.show()
c2.child2_func()
