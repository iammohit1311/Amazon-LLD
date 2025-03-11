import uuid

class Order:
    def __init__(self, user_id: str, items: dict, total_price: float):
        self.order_id = str(uuid.uuid4())
        self.user_id = user_id
        self.items = items
        self.total_price = total_price
        self.status = "Pending"

    def process_payment(self, payment_method: str):
        print(f"Processing {payment_method} payment for {self.total_price}")
        self.status = "Paid"
