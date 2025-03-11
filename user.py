import uuid
from cart import Cart
from order import Order

class User:
    def __init__(self, name: str, email: str, password: str):
        self.user_id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.password = password  # In real applications, use password hashing
        self.cart = Cart(self.user_id)
        self.orders = []

    def add_to_cart(self, product, quantity):
        self.cart.add_item(product, quantity)

    def checkout(self):
        order = self.cart.checkout()
        if order:
            self.orders.append(order)
            return order
        return None
