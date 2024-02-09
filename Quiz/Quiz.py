class User:

    def __init__(self, user_id, username):
        print("New user being created")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("LOFT", "Ahmet")
user_2 = User("LOFTILY", "AhmetYG")

print(user_1.id)
print(user_1.username)

user_1.follow(user_2)