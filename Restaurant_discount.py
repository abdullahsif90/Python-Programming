bill=int(input("Enter the bill amount: "))

if(bill <= 0):
    print("Error ")
elif bill < 3000 :
    discount = 0
    print("Discount: ",discount)
    print("Your bill: ", bill)
elif bill >= 3000 and bill <= 6999:
    discount = (bill * 10)/100
    total_bill = bill - discount
    print("Discount:", discount)
    print("Your bill after discount is: ",total_bill)
elif bill >= 7000 and bill <= 9999:
    discount = (bill * 15)/100
    total_bill = bill - discount
    print("Discount:", discount)
    print("Your bill after discount is: ",total_bill)
else:
    discount = (bill * 20)/100
    total_bill = bill - discount
    print("Discount:", discount)
    print("Your bill after discount is: ",total_bill)

