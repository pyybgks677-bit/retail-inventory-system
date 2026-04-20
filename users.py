# user.py
class User:
    def __init__(self):
        # A simple "user database"
        self.users = {"anita": "1234", "austin": "456password"}
    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False
