class Product:

    def __init__(self, name: str, price: float, category: str, in_stock: bool):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
    
    def check_stock(self):
        if self.in_stock:
            print(f'{self.name} omborda bor')
        else:
            print(f'{self.name} hozirda tugagan')

p1 = Product('Airpods', 20, 'electronics', True)
p1.check_stock()