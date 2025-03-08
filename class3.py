MAX_COUNT = 2

class User:
    def __init__(self, id: int, nickname: str):
        self.id = id
        self.nickname = nickname
    
class Server:
    def __init__(self):
        self.users = {}

    def __add__(self, other):
        return len(self.users) + len(other.users)

    def add_user(self, user: User):
        if user.id in self.users or len(self.users) == MAX_COUNT:
            return
        self.users[user.id] = user

    def del_user(self, user:User):
        if user.id not in self.users:
            return
        self.users.pop(user.id)

    def show_users(self):
        print('Users:\n')
        for user in self.users.values():
            print(f'id={user.id} name={user.nickname}')

if __name__ == '__main__':
    a = User(114, 'Nagibator')
    b = User(456, 'Otchim')
    c = User(789, 'TyEZZka')
    v = User(141, 'AThtrty')
    m = User(142, 'AGtyer3')
    n = User(131, 'Agerth')

    server = Server()
    server.add_user(a)
    server.add_user(b)
    server.add_user(c)
    server.del_user(b)
    server.add_user(c)
    server.del_user(b)
    server.show_users()
    server1 = Server()
    server1.add_user(v)
    server1.add_user(n)
    server1.add_user(m)
    server1.del_user(n)
    server1.add_user(m)
    server1.del_user(n)
    server1.show_users()
    print(server + server1)
    