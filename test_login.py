# test_login.py
import unittest
from users import User

class TestLogin(unittest.TestCase):
    def test_successlogin(self):
        success_login = User()
        result = success_login.login("anita", "1234")
        self.assertTrue(result)

    def test_wrong_username(self):
        wrong_username = User()
        result = wrong_username.login("megico", "1234")
        self.assertFalse(result)

    def test_wrong_password(self):
        wrong_password = User()
        result = wrong_password.login("megico", "123456")
        self.assertFalse(result)
