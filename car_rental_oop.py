class CarRental:
    def __init__(self,car_name,car_company,car_model,car_color,rent_per_day):
        self.car_name = car_name
        self.car_company = car_company
        self.car_model = car_model
        self.car_color = car_color
        self.rent_per_day = rent_per_day

    def display_car(self):
        print("\n****Car Details****")
        print("Car name: ",self.car_name)
        print("Car Company: ",self.car_company)
        print("Car Model: ",self.car_model)
        print("Car Color: ",self.car_color)
        
    
    def calculate_rent(self,days):
        total_rent = self.rent_per_day * days
        print("\n****Rental Bill****")
        print("Rental Days: ",days)
        print("Rent Per Day: ",self.rent_per_day)
        print("Total Rent: ",total_rent)

car_name = input("Enter Car Name: ")
car_company = input("Enter Car Company: ")
car_model = input("Enter Car Model: ")
car_color = input("Enter Car Color: ")
days = int(input("\nHow many days do you want to rent?: "))
rent_per_day = int(input("\nRent per day: "))

car1 = CarRental(car_name,car_company,car_model,car_color,rent_per_day)
car1.display_car()

car1.calculate_rent(days)