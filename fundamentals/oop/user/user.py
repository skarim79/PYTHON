class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdraw(self, amount):
        self.account_balance -= amount

    def make_transfer(self, amount, name):
        self.account_balance -= amount
        name.account_balance = name.account_balance + amount 

peter = User('peter','peter@gmail.com')
john = User('john','john@gmail.com')
bob = User('bob','bob@gmail.com')

peter.make_deposit(100)
peter.make_deposit(100)
peter.make_deposit(100)
peter.make_withdraw(80)
print(peter.account_balance)

john.make_deposit(200)
john.make_deposit(200)
john.make_withdraw(50)
john.make_withdraw(50)
print(john.account_balance)

bob.make_deposit(200)
bob.make_withdraw(80)
bob.make_withdraw(100)
bob.make_withdraw(60)
print(bob.account_balance)

john.make_transfer(100, bob)
print(bob.account_balance)
print(john.account_balance)
