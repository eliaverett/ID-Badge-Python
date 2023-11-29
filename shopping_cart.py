print('Welcome to the Shopping Cart Program!\n')

class ShoppingCart:
    def add_item(self, item):
        try:
            self.cart.append(item)
        except AttributeError:
            self.cart = [item]
        print(f"'[item] has been added to the cart")

    def view_cart(self):
        try:
            print("The contents of the shopping cart are:")
            for item in self.cart:
                print(item)
            print()
        except AttributeError:
            print("The cart is empty. \n")
    
    def remove_item(self, item):
        try:
            self.cart.remove(item)
            print(f"'{item}' has been removed from the cart. \n")
        except (AttributeError, ValueError):
            print(f"'{item} is not in the cart. \n")
    
    def compute_total(self):
        try:
            total_item = len(self.cart)
        except AttributeError:
            total_items = 0
        print(f"The total number of items in the cart is: {total_items} \n")

    def quit_program(self):
        print("Thank you, Goodbye.")
        exit()

def main():
    shopping_cart = ShoppingCart()

    while True:
        print('Please select one of the following:')
        print("1. Add item")
        print("2. View cart")
        print("3. Remove item")
        print("4. Compute total")
        print("5. Quit")

        action = input("Please enter an action: ")

        if action == '1':
            item = input("What item would you like to add?")
            shopping_cart.add_item(item)
        elif action == '2':
            shopping_cart.view_cart()
        elif action == '3':
            item = input("What item would you like to remove?")
            shopping_cart.remove_item(item)
        elif action == '4':
            shopping_cart.compute_total()
        elif action == '5':
            shopping_cart.quit_program()
        else:
            print("Invalid action. Please enter a number between 1 and 5. \n")

if __name__ == '__main__':
    main()

