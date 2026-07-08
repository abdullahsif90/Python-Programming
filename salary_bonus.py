salary=int(input("Enter the monthly salary: "))
if(salary < 0):
    print("Error !")
elif salary < 50000:
    print("You got no bonus ")
elif salary >= 50000 and salary <= 69999:
    bonus = (salary * 10)/100
    final_salary = salary + bonus
    print("The salary after Bonus is: ", final_salary)
elif salary >= 70000 and salary <= 99999:
    bonus = (salary * 15)/100
    final_salary = salary + bonus
    print("The salary after Bonus is: ", final_salary)
else:
    bonus = (salary * 20)/100
    final_salary = salary + bonus
    print("The salary after Bonus is: ", final_salary)

