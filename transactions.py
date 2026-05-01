class Transaction:
    def __init__(self, user_id, product_id, quantity, transaction_type):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity
        self.transaction_type = transaction_type  # 'purchase' or 'sale'

    def process(self, product):
        if self.transaction_type == 'purchase':
            product.stock += self.quantity
        elif self.transaction_type == 'sale':
            if product.stock >= self.quantity:
                product.stock -= self.quantity
            else:
                return "Not enough stock"
        return "Transaction successful"