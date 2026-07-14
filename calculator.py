def calculator(num1, num2, operation):
    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1 - num2 )
    elif operation == "*":
        print(num1 * num2)
    elif operation == "/":
        print(num1 / num2)
    else:
        print("Invalid operator ")

num1=int(input("Enter the first number: "))
num2=int(input("Enter the first number: "))
operation =input("Enter the operator (+,-,*,/): ")

calculator(num1,num2,operation)
