print("Restaurant Order System")
order=[]


orders=int(input("How many orders? "))
for i in range(orders):
    order_name=input(f"Enter the order no {i+1}: ")
    order.append(order_name)

# print("Your Order is: ",order)

print("\n Your Order:") # also write this

for i in range(len(order)):
    print(f"{i+1}. {order[i]}")
