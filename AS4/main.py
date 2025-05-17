from Restaurant import Restaurant

class Main:
    def __init__(self):
        self.resturant=Restaurant(" Makan Palace")
    def get_user_choice(self):
            print("Welcome to the Resturant Managment System:")
            print("choice an option:")
            print("1. add_Item ")
            print("2. view menu ")
            print("3. create new order ")
            print("4. List all orders")
            print("5. Exit")
            ch = int(input("Enter your choices: "))
            return ch
        
    def run(self):
            ch = self.get_user_choice()
            if ch == 1:
                name = input("Enter item name: ")
                try:
                 price = float(input("Enter item price: "))
                except ValueError:
                    print("Invalid price. Must be a number.")
                category = input("Enter item category: ")
                self.resturant.add_Item(name,price,category)                
            elif ch == 2:
                    self.resturant.view_Menu()
            elif ch == 3:
                    self.resturant.create_new_order()
            elif ch == 4:
                    self.resturant.list_orders()
                    print(self.resturant.list_orders())

            elif ch == 5:    
                print("Thank you for using the Restaurant Management System!")
            else:
                print("Invalid choice. Please try again.")
            ch = self.get_user_choice()


   
if __name__ =="__main__":
    main=Main()
    main.run()