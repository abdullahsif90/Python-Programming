print("Employee Salary Collection")

employee_salaries =[]
employee =int(input("How many employees: "))
for i in range(employee):
    employee_salary = int(input(f"Enter the employee {i+1} salary: "))
    employee_salaries.append(employee_salary)

print("The salary is: ",employee_salaries)

print("The sum of salaries are: ",sum(employee_salaries))

print("The max salary is: ",max(employee_salaries))

print("The min salary is: ",min(employee_salaries))

print("The average is: ",sum(employee_salaries) / len(employee_salaries))
