class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return self.name

class Order:
    def __init__(self, items):
        self.items = items

    def bill_amount(self):
        return sum(item.price for item in self.items)

    def __repr__(self):
        return f"Order Items: {self.items}, Bill Amount: {self.bill_amount()}"

class Restaurant:

    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []
        self.revenue = 0

    def order(self, items):
        added_item = []
        for item in items:
            if item in self.menu:
                added_item.append(item)
        if len(added_item) > 0:
            new_order = Order(added_item)
            self.orders.append(new_order)
        return self.orders

    def get_revenue(self):
        for order in self.orders:
            bill = order.bill_amount()
            self.revenue += bill
        return self.revenue
        

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    # Create Item objects with name and price
    steak = Item("Steak", 25)
    salad = Item("Salad", 10)
    fish = Item("Fish", 30)
    pizza = Item("Pizza", 40)
    # Create menu
    menu = [steak, salad, fish]
    # Create Restaurant object with name and menu list
    restaurant = Restaurant("Cool Beans", menu)
    # Create list of items to be ordered (note that pizza is not on the menu)
    order = [steak, steak, salad, pizza]
    # Place the order
    restaurant.order(order)
    # Place two more orders
    restaurant.order([steak, steak, steak, salad])
    restaurant.order([salad, pizza])
    # Get the revenue of the restaurant object
    print(restaurant.get_revenue())

