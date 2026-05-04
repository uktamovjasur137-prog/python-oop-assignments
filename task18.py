class Product:

    def __init__(self, name: str, price: float, category: str, in_stock=True):
        self.name = name
        self.price = price
        self.category = category

    def info(self):
        print(f'{self.name} -- {self.price}$')

p1 = Product("iPhone 13", 999, "Electronics")
p2 = Product("AirPods", 199, "Electronics")
p3 = Product("MacBook", 1500, "Electronics")
p4 = Product("Shoes", 120, "Fashion")
p5 = Product("Watch", 300, "Accessories")
p6 = Product("TV", 800, "Electronics")

products = [p1, p2, p3, p4, p5, p6]

result = max(products, key=lambda x: x.price)

result.info()