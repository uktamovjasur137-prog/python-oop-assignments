class Book:
    def __init__(self, title: str, author: str, is_read=False):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        if self.is_read == False:
            self.is_read = True

    def status(self):
        if self.is_read == False:
            print(f'{self.title} -- oqilmagan')
        else:
            print(f'{self.title} -- oqilgan')

b1 = Book("Harry Potter", "J.K. Rowling", True)
b2 = Book("Atomic Habits", "James Clear", False)
b3 = Book("The Alchemist", "Paulo Coelho", False)
b4 = Book("Rich Dad Poor Dad", "Robert Kiyosaki", False)
b5 = Book("Clean Code", "Robert Martin", False)

b2.mark_as_read()
b5.mark_as_read()


books = [b1, b2, b3, b4, b5]
for book in books:
    book.status()