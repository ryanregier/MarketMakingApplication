import datetime
from Order import Order


class Market:
    buy, sell = [], []
    high, low = None, None

    def __init__(self, name, ticker, price, quantity, type_asset, asset_class, tradable, bid, ask):
        self.name = name
        self.ticker = ticker
        self.price = price
        self.quantity = quantity
        self.type_asset = type_asset
        self.asset_class = asset_class
        self.tradable = tradable
        self.bid = bid
        self.ask = ask

    def check_order(self, last_order, side):
        if side == "buy":
            for x in self.sell:
                if last_order == x:
                    return True
        else:
            for x in self.buy:
                if last_order == x:
                    return True
        return False

    def place_order(self, side, quantity, price, owner):
        time_entered = datetime.datetime.now()
        if side == "buy":
            new_order = Order(quantity, price, time_entered, None, owner)
            self.buy.append(new_order)
            self.check_order(new_order, "buy")
        else:
            new_order = Order(quantity, price, time_entered, None, owner)
            self.sell.append(new_order)
            self.check_order(new_order, "sell")

    def get_orderbook(self):
        return self.buy, self.sell
