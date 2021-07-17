class Order:
    def __init__(self, quantity, price, order_time, expiry_date, owner):
        self.quantity = quantity
        self.price = price
        self.order_time = order_time
        self.expiry_date = expiry_date
        self.owner = owner

    def __eq__(self, other):
        return self.quantity == other.quantity and self.price == other.price
