class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        print(f'balance: {self.balance}')
    
    def get_balance(self):
        return self.balance

b1 = BankAccount("Ali", 1000)
b2 = BankAccount("Vali", 2000)
b3 = BankAccount("Jasur", 1500)
b4 = BankAccount("Aziz", 500)
b5 = BankAccount("Sardor", 3000)

users = [b1, b2, b3, b4, b5]
total = 0
for user in users:
    total += user.balance

print(f'Umumiy summa: {total}')