units=int(input("Enter the electricty units: "))
if(units <=0):
    print("Error! ")
elif units > 0 and units <= 100:
    bill = units * 5
    print("The electricity bill is: ",bill)
elif units > 101 and units <= 200:
    bill = units * 8
    print("The electricity bill is: ",bill)
elif units > 200 and units <= 300:
    bill = units * 10
    print("The electricity bill is: ",bill)
else:
    bill = units * 12
    print("The electricity bill is: ",bill)