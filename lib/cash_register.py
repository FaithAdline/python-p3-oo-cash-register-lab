class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.last_transaction = 0
        self.discount = discount

    def add_item(self, item_name, price, quantity=1):
        for _ in range(quantity):
            self.items.append((item_name, price))
            self.total += price

    def calculate_total(self):
        return self.total

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "There is no discount to apply."

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item[1]
        else:
            self.total = 0


