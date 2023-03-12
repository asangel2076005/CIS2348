class ItemToPurchase:

    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def get_item_cost(self):
        item_cost = self.item_price * self.item_quantity
        return item_cost

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${self.get_item_cost():.0f}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}.")


class ShoppingCart:

    def __init__(self, customer_name="none", date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item_exist = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_name:
                del self.cart_items[i]
                item_exist = True
                break
        if not item_exist:
            print("Item is not found in card. Nothing removed")

    def modify_item(self, item):
        item_exist = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                del self.cart_items[i]
                item_exist = True
                break
        if not item_exist:
            print("Item is not found in card. Nothing modified")

    def get_num_items_in_cart(self):
        quantity = 0
        for i in range(len(self.cart_items)):
            quantity = quantity + self.cart_items[i].item_quantity
        return quantity

    def get_cost_of_cart(self):
        cost = 0
        for i in range(len(self.cart_items)):
            cost = cost + self.cart_items[i].item_price * self.cart_items[i].item_quantity
        return cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of items: {self.get_num_items_in_cart()}")
            print()
            print("Item Descriptions")
            for i in range(len(self.cart_items)):
                print(f"{self.cart_items[i].item_name} {self.cart_items[i].item_quantity} @ "
                      f"${self.cart_items[i].item_price} = "
                      f"${self.cart_items[i].item_price * self.cart_items[i].item_quantity}")

    def print_description(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for i in range(len(self.cart_items)):
            self.cart_items[i].print_item_description()


def print_menu(customer_cart):
    cart = customer_cart
    menu = (
        "\nMenu\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )
    user_choice = ""

    while user_choice != "q":
        print(menu)
        user_choice = input("Choose an option:\n")
        while (
                user_choice != "a" and user_choice != "r" and user_choice != "c" and user_choice != "i" and user_choice != "o" and user_choice != "q"
        ):
            user_choice = input("Choose an option:\n")

        if user_choice == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = int(input('Enter the item price:\n'))
            quantity = int(input('Enter the item quantity:\n'))
            purchase_item = ItemToPurchase(name, price, quantity, description)
            cart.add_item(purchase_item)


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    date_today = input("Enter today's date:\n")
    print()
    customer = ShoppingCart(customer_name, date_today)
    print_menu(customer)
