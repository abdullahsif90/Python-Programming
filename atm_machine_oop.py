class ATM:
    def __init__(self,balance):
        self.balance = balance

    def check_balance(self):
        print("\nCurrent Balance: ",self.balance)
    
    def deposit_amount(self,amount):
        self.balance += amount
        print("\nAmount Deposit Successfully ")
        print("Updated Balance: ",self.balance)
    
    def withdraw_amount(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("\nWithdraw Successfully")
            print("Remaining Balance: ",self.balance)
        else:
            print("Insufficient Balance")

balance = int(input("Enter the initial balance: "))
balance1 = ATM(balance)
balance1.check_balance()

amount = int(input("\nEnter deposit amount: "))
balance1.deposit_amount(amount)

withdraw = int(input("\nEnter Withdraw amount: "))
balance1.withdraw_amount(withdraw)

balance1.check_balance()
