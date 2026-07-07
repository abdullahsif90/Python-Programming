print("This is the program for subject result")
marks=int(input("Enter the subject marks: "))
if(marks>100 or marks<0):
    print("Error! enter the correct marks")
elif(marks>=90 and marks<=100):
    print("You got A+ grade ")
elif(marks>=80 and marks<90):
    print("you got B+ grade ")
elif(marks>=70 and marks<80):
    print("You got C+ grade ")
elif(marks>=60 and marks<70):
    print("You got D+ grade ")
elif(marks>=50 and marks<60):
    print("You got D grade ")
else:
    print("You got F grade ")
    

