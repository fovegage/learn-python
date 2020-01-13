class User:
    def __init__(self, uid):
        self.uid = uid

    def __repr__(self):
        return f'User{self.uid}'


a = User(34)
b = User(1)
c = User(99)
users = [a, b, c]
from operator import attrgetter

print(sorted(users, key=attrgetter('uid')))
