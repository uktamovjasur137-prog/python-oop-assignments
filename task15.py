class Product:

    def __init__(self, name: str, price: float, in_stock: bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock

p1 = Product("iPhone 13", 999, True)
p2 = Product("AirPods", 199, True)
p3 = Product("MacBook", 1500, False)
p4 = Product("Samsung TV", 800, True)
p5 = Product("PlayStation 5", 700, False)

products = [p1, p2, p3, p4, p5]

total = 0
for product in products:
    if product.in_stock == True:
        total += product.price

print(f'Umumiy narx: {total}')