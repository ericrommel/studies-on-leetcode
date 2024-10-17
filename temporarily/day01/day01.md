from temporarily.day01.shopping_cart import ShoppingCartfrom temporarily.day01.shopping_cart import ShoppingCartfrom temporarily.day01.shopping_cart import ShoppingCart

# Day 1: Shopping Cart Problem + Data Structures Review


## 1. Understand the Shopping Cart Problem:
    - This is a system design problem where you’ll need to build a shopping cart. It tests your understanding of basic
      data structures and object-oriented design. You can implement a simple version of a shopping cart using a
      class-based design in Python. Ensure it covers the following operations:
        - Add item (with name, price, quantity)
        - Remove item
        - Update quantity
        - Display cart with total value
        - Apply discounts (optional)

Here's a simple structure to start with, as you’ll likely need to explain your design during the interview:

- [Shopping Cart problem](shopping_cart.py)


## 2. Review Basic Data Structures:

Python has four primary built-in data structures that you should be very familiar with: Lists, Sets, Dictionaries, and Tuples.
Understanding their properties, use cases, and time complexities is crucial, especially in coding interviews where choosing the right data structure can optimize your solution.


### 2.1 Lists
- Definition: List are ordered, mutable (changeable), and allow duplicate elements.
- Key Operations:
  - Access element: list[index] -> O(1)
  - Insert element: list.append() -> O(1) for adding to the end
  - Insert element at index: list.insert(index, element) -> O(n) (shift elements)
  - Delete element: list.remove(element) or del list[index] -> O(n)
  - Search for element: element in list -> O(n)
- Common Use Case: Lists are great when need to maintain order and have fast access to elements by index. However, they are less efficient for searching unless the list is sorted.

Example:
```python
items = ['Laptop', 'Phone', 'Mouse']
if 'Laptop' in items:  # O(n)
    print('Laptop is in the cart.')
```


### 2.2 Sets
- Definition: Sets are unordered collections of unique elements.
- Key Operations:
  - Add element: set.add() -> O(1)
  - Remove element: set.remove() or set.discard() -> O(1)
  - Check if element exists: element in set  -> O(1)
  - Union, intersection, difference: O(len(set)) (depends on the number of elements)
- Common Use Cases: Sets are ideal for membership tests and unique item storage when order doesn't matter. They provide O(1) time complexity for add, remove, and lookup operations.

Example:
```python
cart_items = set()
cart_items.add('Laptop')
cart_items.add('Mouse')
cart_items.add('Laptop')  # This will not add 'Laptop' again, as sets are unique
```


### 2.3 Dictionaries
- Definition: Dictionaries are collections of key-value pairs. They are unordered and mutable.
- Key Operations:
  - Insert/update key-value pair: dict[key] = value -> O(1)
  - Remove key-value pair: del dict[key] -> O(1)
  - Lookup value by key: dict[key] or key in dict -> O(1)
- Common Use Cases: Dictionaries are extremely useful when you need fast lookups, especially when mapping one value to another (like item names to quantities or prices in the shopping cart).

Example:
```python
cart = {'Laptop': 1000, 'Mouse': 50}
if 'Laptop' in cart:  # O(1)
    print('Laptop price:', cart['Laptop'])
```


### 2.4 Tuples
- Definition: Tuples are ordered and immutable (unchangeable) collections.
- Key Operations:
  - Access element: tuple[index] -> O(1)
  - Concatenate tuples: tuple1 + tuple2  -> O(n)
  - Check if element exists: element in tuple -> O(n)
- Common Use Cases: Tuples are useful for fixed collections of elements where you don't need to modify the data (e.g., coordinates, fixed records)

Example:
```python
item = ('Laptop', 1000)
print(item[0])  # Laptop
```


### 2.5 Time Complexity Summary

    | Data Structure | Access | Insert | Delete | Search |
    |----------------|--------|-----------------|--------|
    | List           | O(1)   | O(1)   | O(n)   | O(n)   |
    | Set            | N/A    | O(1)   | O(1)   | O(1)   |
    | Dictionary     | O(1)   | O(1)   | O(1)   | O(1)   |
    | Tuple          | O(1)   | N/A    | N/A    | O(n)   |


### 2.6 Key Takeaways
- Use `lists` when you need order and index access
- Use `sets` when you need unique elements and fast membership tests
- Use `dictionaries` when you need key-value pairs with fast lookups
- Use `tuples` when you need fixed, unchangeable collections


## 3. Practice Object-Oriented Design
Object-oriented design questions test your ability to design scalable and maintainable systems. For the shopping cart problem, consider additional features that could be part of an extended design. This is a great opportunity to demonstrate your understanding of concepts like inheritance, encapsulation, and polymorphism.


### 3.1 Encapsulation
Encapsulation refers to bundling data (attributes) and methods that operate on the data into a single unit (a class). You can apply encapsulation to control how internal state is accessed and modified.
Example:
```python
class ShoppingCart:
    def __init__(self):
        self._items = {}

    def add_items(self, item_name, price, quantity=1):
        if item_name in self._items:
            self._items[item_name]['quantity'] += quantity
        else:
            self._items[item_name] = {'price': price, 'quantity': quantity}
        
    def get_total(self):
        return sum(details['price'] * details['quantity'] for details in self._items.values())
```


### 3.2 Inheritance
Inheritance allows you to create a class that inherits attributes and methods from another class. This is useful when extending the shopping cart system.
Example:
```python
class DiscountedCart(ShoppingCart):
    def apply_discount(self, discount_rate):
        for item in self._items:
            self._items[item]['price'] *= (1 - discount_rate)
```


### 3.3 Polymorphism
Polymorphism allows you to use methods that have the same name but behave differently depending on the object they're called on. This can be useful for applying different pricing strategies.
Example:
```python
# Polymorphism: Both classes have `apply_discount` but behave differently
class DiscountedCart(ShoppingCart):
    def apply_discount(self, discount_rate):
        for item in self._items:
            self._items[item]['price'] *= (1 - discount_rate)

class BulkDiscountCart(ShoppingCart):
    def apply_discount(self, item_name, bulk_threshold, discount_rate):
        if self._items[item_name]['quantity'] > bulk_threshold:
            self._items[item_name]['price'] *= (1 - discount_rate)
```


### 3.4 Additional Features to Consider
In an interview, you may be asked to extend the shopping cart design with more complex features:
- Discount Systems: Apply percentage discounts, bulk discounts, or coupon codes.
- Tax Calculators: Implement a feature that calculates tax based on cart value and location.
- Inventory Management: Track available stock and prevent adding items that are out of stock.

Example:
```python
class ShoppingCart:
    def __init__(self, tax_rate=0.08):
        self.cart = {}
        self.tax_rate = tax_rate

    def get_total_with_tax(self):
        total = sum(details['price'] * details['quantity'] for details in self.cart.values())
        return total * (1 + self.tax_rate)
```
