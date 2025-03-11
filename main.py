from inventory import Inventory
from user import User
from product import Product

if __name__ == "__main__":
    inventory = Inventory()
    user = User("Alice", "alice@example.com", "password")

    product1 = Product("Laptop", 1000.0, 10, "Electronics")
    product2 = Product("Phone", 500.0, 20, "Electronics")

    inventory.add_product(product1)
    inventory.add_product(product2)

    user.add_to_cart(product1, 1)
    order = user.checkout()
    
    if order:
        order.process_payment("Credit Card")
        print("Order details:", order.__dict__)

    # Testing Singleton Behavior
    inventory2 = Inventory()
    print("Inventory is singleton:", inventory is inventory2)  # Should print True

    cart2 = Cart(user.user_id)
    print("Cart is singleton:", user.cart is cart2)  # Should print True
