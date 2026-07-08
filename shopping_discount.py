print("Shopping Bill Calculator")

shopping_amount = int(input("Enter the shopping amount: "))

if shopping_amount < 0:
    print("Error! Invalid shopping amount.")

elif shopping_amount >= 5000:
    discount = (shopping_amount * 20) / 100
    final_bill = shopping_amount - discount

    print("Discount: ", discount)
    print("Final Bill: ", final_bill)

elif shopping_amount >= 3000 and shopping_amount <= 4999:
    discount = (shopping_amount * 15) / 100
    final_bill = shopping_amount - discount

    print("Discount: ", discount)
    print("Final Bill: ", final_bill)

elif shopping_amount >= 1000 and shopping_amount <= 2999:
    discount = (shopping_amount * 10) / 100
    final_bill = shopping_amount - discount

    print("Discount: ", discount)
    print("Final Bill: ", final_bill)

else:
    print("No Discount")
    print("Final Bill: ", shopping_amount)