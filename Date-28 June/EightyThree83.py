class BankAccount:

    def __init__(self):
        self.balance =0
        self.__Private_Var=100

    def deposite(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def show_balance(self):
        print("My Balance is :",self.balance)

MyBalance = BankAccount()

MyBalance.deposite(200)
MyBalance.withdraw(100)
print(MyBalance.balance)



