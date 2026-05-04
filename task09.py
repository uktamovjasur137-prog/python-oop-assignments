class User:

    def __init__(self, username: str, email: str, is_active: bool):
        self.username = username
        self.email = email
        self.is_active = is_active

    def activate(self):
        if self.is_active == False:
            self.is_active = True
            print(f'{self.username} faollashtirildi')

    def deactivates(self):
        if self.is_active == True:
            self.is_active = False
            print(f'{self.username} bloklandi')

u1 = u1 = User('Sami18', 'aliyevsami18@gmail.com', False)
u1.activate()