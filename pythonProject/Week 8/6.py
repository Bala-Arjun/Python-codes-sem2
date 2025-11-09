class Student:
    def __init__(self,name,email,mobile,branch):
        self.name=name
        self.email=email
        self.mobile=mobile
        self.branch=branch
s1=Student("Ram","ram@gmail.com","8125251050","CSE")
s2=Student("Sita","Sita@gmail.com","8125251060","CSE")
print(s1.__dict__)
delattr(s1,'name')
print(s1.__dict__)
