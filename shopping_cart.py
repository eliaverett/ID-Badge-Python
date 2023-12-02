#I added a feature that if the user puts milk, it will say I cannot add that to the cart, I am lactose intolerant. 
print('Welcome to the Shopping Cart Program!\n')

class ShoppingCart:
    cart = []

    def is_lactose_intolerant(self, item):
        return item.lower() == "milk"

    def add_item(self, item, price):
        if self.is_lactose_intolerant(item):
            print("Sorry, you cannot put that, I am lactose intolerant.")
        else:
            try:
                self.cart.append({'name': item, 'price': price})
                print(f"{item} has been added to the cart")
            except AttributeError:
                self.cart = [{'name': item, 'price': price}]
                print(f"{item} has been added to the cart")

    def view_cart(self):
        try:
            print("The contents of the shopping cart are:")
            for i, item in enumerate(self.cart, start=1):
                print(f"{i}. {item['name']} - {item['price']:.2f}")
            print()
        except AttributeError:
            print("The cart is empty. \n")

    def remove_item(self, index):
        try:
            if 0 <= index < len(self.cart):
                removed_item = self.cart.pop(index)
                print(f"{removed_item['name']} has been removed from the cart. \n")
            else:
                print("Invalid index. Please enter a valid index. \n")
        except (AttributeError, ValueError):
            print("Error removing item from the cart. \n")

    def compute_total(self):
        try:
            total_price = sum(item['price'] for item in self.cart)
            print(f"The total amount in the cart is: ${total_price:.2f} \n")
        except AttributeError:
            print("The cart is empty. \n")

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
            price = float(input("What is the price of the item?"))
            shopping_cart.add_item(item, price)
        elif action == '2':
            shopping_cart.view_cart()
        elif action == '3':
            index = int(input("Enter the index of the item you want to remove: "))
            shopping_cart.remove_item(index - 1)
        elif action == '4':
            shopping_cart.compute_total()
        elif action == '5':
            shopping_cart.quit_program()
        else:
            print("Invalid action. Please enter a number between 1 and 5. \n")

if __name__ == '__main__':
    main()


