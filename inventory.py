from product import Product

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product: Product):
        self.products[product.product_id] = product

    def list_products(self):
        return [p.__dict__ for p in self.products.values()]
