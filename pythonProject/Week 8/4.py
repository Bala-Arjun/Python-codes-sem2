class Student:
    def __init__(self,name,rno,email):
        self.name=name
        self.rno=rno
        self.email=email
    def display_details(self):
        print("Name   :",self.name)
        print("Roll no:",rno)
        print("Email  :",email)
name=input("Enter your name..")
rno=input("Enter your roll no..")
email=input("Enter your email..")
s=Student(name,rno,email)
print("Student details:")
print("_"*30)
s.display_details()
