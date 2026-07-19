class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_details(self):
        print("\n===== Mobile Information =====")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

    def discount(self, percent):
        discount_amount = self.price * percent / 100
        self.price -= discount_amount
        print("\nDiscount Applied Successfully!")
        print("Updated Price:", self.price)


# User Input
brand = input("Enter Mobile Brand: ")
model = input("Enter Mobile Model: ")
price = float(input("Enter Mobile Price: "))

# Object Creation
m1 = Mobile(brand, model, price)

# Show Details
m1.show_details()

# Discount
percent = float(input("\nEnter Discount Percentage: "))
m1.discount(percent)