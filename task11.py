class Book:
    def __init__(self, title: str, author: str, is_read: bool):
        self.title = title
        self.author = author
        self.is_read = is_read

    def mark_as_read(self):
        if self.is_read == False:
            self.is_read = True
            print(f'{self.title} oqilgan deb belgilandi')

    def status(self):
        if self.is_read == False:
            print(f'{self.title} oqilmagan')

        else:
             print(f'{self.title} oqilgan')

b1 = Book('Harry Potter', 'Snape', False)
b1.mark_as_read()
b1.status()

