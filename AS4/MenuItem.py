class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def get_info(self):
        return f"{self.name} - ${self.price:.2f} ({self.category})"