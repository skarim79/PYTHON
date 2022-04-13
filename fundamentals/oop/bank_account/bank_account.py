class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.account_balance = 0

    def deposit(self, amount):
        self.amount += amount
        return self

    def withdraw(self, amount):
        if self.account_balance >= 0:
            print ('Sufficient fund')
        else :
            print ('Insufficient fund, charging a 5$ fee')
            self.account_balance -= 0
        return self

    def display_account_info(self):
        print(f'account_balance:{self.account_balance}')

    def yield_interest(self):
        if self.account_balance >= 0:
            self.account_balance += (self.account_balance * self.int_rate)
        return self

checking = BankAccount()
saving = BankAccount()

checking.deposit(100).deposit(200).deposit(80).withdraw(50).yield_interest().display_account_info()
saving.deposit(200).deposit(100).withdraw(50).withdraw(70).withdraw(130).withdraw(30).yield_interest().display_account_info
