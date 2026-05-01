# product.py
class Product:
    def __init__(self, id, name, stock=0):
        self.id = id
        self.name = name
        self.__stock = stock  # private stock for encapsulation

    def purchase(self, amount):
        if amount > 0:
            self.__stock += amount
            return True
        return False

    def sell(self, amount):
        if 0 < amount <= self.__stock:
            self.__stock -= amount
            return True
        return False

    def get_stock(self):
        return self.__stock
