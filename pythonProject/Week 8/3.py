class Employee:
    def set_name(self,name):
        self.name=name

    def set_id(self,id):
        self.id=id

    def set_salary(self, salary):
            self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def get_id(self):
        return self.id

n=int(input("Enter number of employees"))
l=[]
for i in range(n):
    e=Employee()
    name=  input("Enter name  :")
    id=    input("Enter id    :")
    salary=input("Enter salary:")
    e.set_name(name)
    e.set_salary(salary)
    e.set_id(id)
    l.append(e)
count=1
for emp in l:
    print(f"\nEmployee-{count} data")
    print("."*30)
    print("Name  :",emp.get_name())
    print("Id    :",emp.get_id())
    print("Salary:",emp.get_salary())
    print("."*30)
    count+=1


