class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Yangi balans: {self.balance}")
        else:
            print('Notogri amal')
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Yangi balans: {self.balance}")
        else:
            print("Balans yetarli emas")

b1 = BankAccount('Ali', 2000)
b1.deposit()
