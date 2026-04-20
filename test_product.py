# test_product.py
import unittest
from products import Product

class TestProduct(unittest.TestCase):
    def test_purchase(self):
        success_purchase = Product("Mobile", 10)
        success_purchase.purchase(5)
        self.assertEqual(success_purchase.get_stock(),15)

    def test_sell(self):
        success_sell = Product("Laptop", 5)
        success_sell.sell(10)
        self.assertEqual(success_sell.get_stock(), 5)