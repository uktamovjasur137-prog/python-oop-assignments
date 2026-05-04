class Movie:

    def __init__(self, title: str, genre: str, duration: int, rating: float):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.rating = rating

m1 = Movie('Avatar', 'action', 140, 8.9)

print(f'Name: {m1.title}, genre: {m1.genre}, duration: {m1.duration} minutes, rating: {m1.rating}')