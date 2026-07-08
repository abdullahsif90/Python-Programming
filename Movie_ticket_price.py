age=int(input("Enter the age: "))
if(age<0):
    print("Error! ")
elif(age>=0 and age <= 5):
    print("Hurrah you got free ticket ")
elif(age>=6 and age<=12):
    print("The ticket price is 200 ")
elif(age>= 13 and age <= 17 ):
    print("The ticket price is 350")
elif(age>=18 and age <=59):
    print("The ticket price is 500")
else:
    print("The ticket price is 250")
