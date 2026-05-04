class Student:

    def __init__(self, name: str, age: int, grade: int):
        self.name = name
        self.age = age
        self.grade = grade

s1 = Student('Ali', 18, 9)

print(s1.name, s1.age, s1.grade)