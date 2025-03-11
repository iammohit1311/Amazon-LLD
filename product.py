import uuid

class Product:
    def __init__(self, name: str, price: float, stock: int, category: str):
        self.product_id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.reviews = []

    def update_stock(self, quantity):
        if quantity <= self.stock:
            self.stock -= quantity
            return True
        return False

    def add_review(self, user, rating, comment):
        self.reviews.append({"user": user.name, "rating": rating, "comment": comment})
