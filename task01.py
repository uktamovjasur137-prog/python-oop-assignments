class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car('BMW', 'M5', 2024)

print(car1.brand, car1.model, car1.year)