class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_salary(self):
        print("\n===== Employee Salary Information =====")
        print("Employee Name:", self.name)
        print("Current Salary:", self.salary)

    def increase_salary(self, amount):
        self.salary += amount
        print("\nSalary Updated Successfully!")
        print("New Salary:", self.salary)


# User Input
name = input("Enter Employee Name: ")
salary = int(input("Enter Current Salary: "))

# Create Object
e1 = Employee(name, salary)

# Display Current Salary
e1.show_salary()

# Increase Salary
amount = int(input("\nEnter Salary Increase Amount: "))
e1.increase_salary(amount)