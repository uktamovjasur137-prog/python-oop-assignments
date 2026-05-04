class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def show_info(self):
        print(f'{self.name} - {self.age}')

s1 = Student("Ali", 15)
s2 = Student("Vali", 16)
s3 = Student("Jasur", 14)
s4 = Student("Aziz", 17)
s5 = Student("Sardor", 15)

students = [s1, s2, s3, s4, s5]
result = max(students, key=lambda x: x.age)

result.show_info()