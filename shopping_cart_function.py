prices = []
item = int(input("How many items? "))
for i in range(item):
    item_price = int(input(f"Enter the price of item {i+1}: "))
    prices.append(item_price)

def total_bill(prices):
    total = 0
    for price in prices: # also for i in range(len(prices))
        total = total+price

    print("Total Bill: ",total)

    #  Discount for greater than 5000
    if total > 5000:
        discount = total * 10 / 100
        final_bill = total - discount
        print("Discount is: ",discount)
        print("Bill after discount: ",final_bill)
    else:
        print("No Discount")

total_bill(prices)