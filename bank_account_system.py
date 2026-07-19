class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    def debit(self, amount):
        self.balance -= amount 
        print("Rs.",amount,"was debited")
        print("Total Balance: ",self.get_balance())
    def credit(self,amount):
        self.balance += amount 
        print("Rs.",amount,"was credited")
        print("Total Balance: ",self.get_balance())
    def get_balance(self):
        return self.balance

acc1=Account(2000,1123453)
print("You Balance is: ",acc1.balance)
print("Your Account No is: ",acc1.account_no)
acc1.debit(1000)
acc1.credit(1000)

        
