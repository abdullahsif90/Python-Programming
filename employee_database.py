employee = {}

employee_id=input("Enter the Employee ID: ")

name = input("Enter the Name: ")

department = input("Enter the Department: ")

salary = int(input("Enter the Monthly Salary: "))

experience =float(input("Enter the Experience: "))

if(experience >=5):
    print("You are Senior Employee ")
else:
    print("You are Junior Employee")
    

employee["ID:"] = employee_id
employee["Name:"] = name
employee["Department:"] = department
employee["Monthly Salary:"] = salary
employee["Experience:"] = experience
print("Employee Record")

print(employee)
yearly_salary = salary * 12
print("Yearly Salary: ",yearly_salary)