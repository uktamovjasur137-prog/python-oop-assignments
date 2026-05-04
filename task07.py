class Movie:

    def __init__(self, title: str, genre: str, duration: int, rating: float):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

    def show_summary(self):
        print(f'{self.title} - {self.genre} janridagi film. Reyting: {self.rating}/10')

m1 = Movie('Inception', 'fantastika', 220, 8.5)

m1.show_summary()