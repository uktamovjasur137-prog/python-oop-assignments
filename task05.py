class Product:

    def __init__(self, name: str, price: float, category: str, in_stock=True):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

p1 = Product('banan', 12.5, 'oziq-oqvat', False)
p2 = Product('olma', 8.5, 'oziq-ovqat')

print(f'name: {p1.name}, price: {p1.price}')
print(f'name: {p2.name}, price: {p2.price}')