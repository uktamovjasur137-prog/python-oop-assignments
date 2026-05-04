class User:

    def __init__(self, username: str, email: str, is_active: bool):
        self.username = username
        self.email = email
        self.is_active = is_active

u1 = User('Sami18', 'aliyevsami18@gmail.com', True)

print(f'username: {u1.username}, email: {u1.email}, is_active: {u1.is_active}')
