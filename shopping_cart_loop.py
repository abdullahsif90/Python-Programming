print("Shopping Cart List ")

shopping_cart = []
items = int(input("Enter the items: "))

for i in range(items):
    name = input("Enter the name: ")
    shopping_cart.append(name)
print("The Shopping Cart is: ",shopping_cart)