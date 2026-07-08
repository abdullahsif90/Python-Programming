print("BMI Calculator")

weight = float(input("Enter the weight in kilograms: "))
height = float(input("Enter the height in meters: "))

if (weight <= 0 or height <= 0):
    print("Error! Invalid weight or height.")

else:
    bmi = weight / (height ** 2)

    print("Your BMI is:", bmi)

    if (bmi < 18.5):
        print("Category: Underweight")

    elif (bmi >= 18.5 and bmi <= 24.9):
        print("Category: Normal Weight")

    elif (bmi >= 25 and bmi <= 29.9):
        print("Category: Overweight")

    else:
        print("Category: Obese")