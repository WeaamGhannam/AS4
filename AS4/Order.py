class Order:
    def __init__(self):
        self.items = []
        self.total = 0.0

    def add_item(self, name, price):
        self.items.append((name, price))
        self.total += price

    def info(self):
        item_str = ", ".join([f"{name} (${price:.2f})" for name, price in self.items])
        return f"Items: {item_str} | Total: ${self.total:.2f}"
    def total(self):
      total = sum(self.menu[item] for item in self.items)
      print(f"total price:=${total}")

    
                     