class Student:
    def __init__(self, name, age, roll, dept):
        self.name = name
        self.age = age
        self.roll_no = roll
        self.department = dept

    def display_info(self):
        print("\n***** Student Information *****")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Department:", self.department)


# User Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
roll = input("Enter your Roll No: ")
dept = input("Enter your Department: ")

# Object Creation
s1 = Student(name, age, roll, dept)

# Display Information
s1.display_info()