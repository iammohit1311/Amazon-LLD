from product import Product
from singleton import Singleton

class Inventory(Singleton):
    def __init__(self):
        if not hasattr(self, "products"):  # Prevent reinitialization
            self.products = {}

    def add_product(self, product: Product):
        self.products[product.product_id] = product

    def list_products(self):
        return [p.__dict__ for p in self.products.values()]
