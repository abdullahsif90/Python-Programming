class Shopping_cart:
    def __init__(self,product_name,price):
        self.product_name = product_name
        self.price = price
    def show_details(self):
        print("\n Shopping Cart")
        print("Product Name: ",self.product_name)
        print("Price: ",self.price)
    def add_tax(self,percent):
        tax_amount = self.price * percent / 100
        self.price += tax_amount
        print("\nTax Added")
        print("After Tax Price: ",self.price)
    def discount_apply(self,percent):
        discount_amount = self.price * percent / 100
        self.price -= discount_amount
        print("\nDiscount Applied")
        print("After discount price: ",self.price)
    
    def final_price(self):
        print("\nFinal Price: ",self.price)
    
product_name = input("Enter the Product Name: ")
price = int(input("Enter the Price: "))
cart = Shopping_cart(product_name,price)
cart.show_details()

tax =float(input("Enter the Tax Percentage: "))
cart.add_tax(tax)

discount=float(input("Enter the discount percentage: "))
cart.discount_apply(discount)


cart.final_price()
