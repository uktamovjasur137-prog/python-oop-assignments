class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        summa = float(input('Pul miqdori: '))
        if summa > 0:
            self.balance += summa
            print(f"Yangi balans: {self.balance}")
        else:
            print('Notogri amal')
    
    def withdraw(self):
        summa = float(input('Pul miqdori: '))
        if summa <= self.balance:
            self.balance -= summa
            print(f"Yangi balans: {self.balance}")
        else:
            print("Balans yetarli emas")

b1 = BankAccount('Ali', 2000)
b1.deposit()
