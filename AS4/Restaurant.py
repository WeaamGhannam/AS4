from Order import Order
from MenuItem import MenuItem

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {
            "tea": MenuItem("tea", 3, "Drinks"),
            "coffe": MenuItem("coffe", 5, "Drinks"),
            "capatcheno": MenuItem("capatcheno", 4, "Drinks"),
            "checkin": MenuItem("checkin", 20, "Meals"),
            "shawarma": MenuItem("shawarma", 20, "Sandwiches"),
            "fish": MenuItem("fish", 30, "Fish"),
            "salad": MenuItem("salad", 10, "Appetizers"),
            "potatoes": MenuItem("potatoes", 10, "Appetizers"),
            "pastries": MenuItem("pastries", 30, "Meals")
        }
        self.orders = []

    def add_Item(self, name, price, category):
        self.menu[name.lower()] = MenuItem(name, price, category)
        print(f"✅  added {name} to order list .\n")

    def view_Menu(self):
        if not self.menu:
            print("⚠️ empty menu .")
        else:
            print("\n📋 menu:")
            for item in self.menu.values():
                print(" -", item.get_info())
            print()

    def create_new_order(self):
        order = Order()
        print("Enter item names to add to the order. Type 'done' when finished.")        
        while True:
            item_name = input("item: ").strip().lower()
            if item_name == "done":
                break
            if item_name in self.menu:
                item = self.menu[item_name]
                order.add_item(item.getName(), item.getPrice())
                print(f"✅  added {item_name}.")
            else:
                print("Item not found in menu.")

        if order.items:
            self.orders.append(order)
            print("Order created successfully.")
        else:
            print("No items added. Order not saved.")

    def list_orders(self):
        if not self.orders:
            print("📭 No items added\n")
        else:
            print("📦  list orders:")
            for i, order in enumerate(self.orders, 1):
                print(f"{i}. {Order.info()}")
            print()
