class ItemNotFound(Exception):
    pass


class ShoppingCart:

    def __init__(self, tax_rate=0.05):
        self.cart = {}
        self.tax_rate = tax_rate

    def add_item(self, item_name: str, price: float, quantity: int=1, discount: float=0):
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
        else:
            self.cart[item_name] = {'price': price, 'quantity': quantity, 'discount': discount}

    def remove_item(self, item_name):
        if item_name in self.cart:
            del self.cart[item_name]
        else:
            raise ItemNotFound()

    def update_quantity(self, item_name, quantity):
        if item_name in self.cart:
            self.cart[item_name]['quantity'] = quantity
        else:
            raise ItemNotFound()

    def total_price(self):
        total = 0
        for item, details in self.cart.items():
            price_after_discount = details['price'] * (1 - details['discount'])
            total += price_after_discount * details['quantity']

        total += total * self.tax_rate
        return total

    def display_cart(self):
        total_price = 0
        for item, details in self.cart.items():
            item_total = details['price'] * details['quantity']
            total_price += item_total
            print(f"{item}: {details['quantity']} @ {details['price']} each. Total: {item_total}")
        print(f"Total cart value: {total_price}")

# Example usage:
cart = ShoppingCart()
cart.add_item('Laptop', 1000, 1, discount=0.1)
cart.add_item('Mouse', 50, 2)
print(f"Total price: {cart.total_price()}")
