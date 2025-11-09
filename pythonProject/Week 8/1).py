class Student:
    # Class variable
    college_name = "MLR"
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age
    # Instance method: works with instance variables
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"College: {Student.college_name}")
    # Class method: works with class variables
    @classmethod
    def change_college(cls, new_clg_name):
        cls.college_name = new_clg_name
        print(f"College name changed to {cls.college_name}")
    # Static method: utility, not dependent on instance or class
    @staticmethod
    def is_valid_age(age):
        return 3 <= age <= 100
# Creating objects (instances) of the Student class
student1 = Student("bala", 15)
student2 = Student("test", 17)
# Calling instance method
student1.display_info()
print()
# Calling class method
Student.change_college("MLRIT")
print()
# Displaying info again to see updated class variable
student2.display_info()
print()
# Calling static method
print("Is 25 a valid age?", Student.is_valid_age(25))
print("Is 2 a valid age?", Student.is_valid_age(2))
