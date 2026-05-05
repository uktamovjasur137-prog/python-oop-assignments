class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print('Muvvafaqiyatli qoshildi')
        else:
            print('Notogri summa')


    def withdraw(self, amount: float):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print('Muvaffaqiyatli yechib olindi')
        else:
            print('Mablag yetarli emas')

    def show_balance(self):
        print(f"{self.owner} balans: {self.balance}")

b1 = BankAccount("Ali", 1000)
b2 = BankAccount("Vali", 2000)
b3 = BankAccount("Sami", 1500)

b1.deposit(400)
b1.withdraw(800)
b1.show_balance()
