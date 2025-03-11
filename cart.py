from order import Order

class Cart:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.items = {}

    def add_item(self, product, quantity):
        if product.stock >= quantity:
            self.items[product] = self.items.get(product, 0) + quantity
        else:
            print("Insufficient stock!")

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]

    def checkout(self):
        if not self.items:
            print("Cart is empty!")
            return None
        
        total_price = sum(product.price * quantity for product, quantity in self.items.items())
        order = Order(self.user_id, self.items, total_price)
        
        for product, quantity in self.items.items():
            product.update_stock(quantity)
        
        self.items.clear()
        return order
