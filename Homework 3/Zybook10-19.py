# Angelo Angel (2076005)

class ItemToPurchase:

    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        self.item_description = "none"

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


class ShoppingCart(ItemToPurchase):

    def __init__(self):
        super().__init__()
        self.customer_name = "none"
        self.current_date = "January 1, 2016"
        self.cart_items = []

    def add_item(self):
        self.cart_items = []
        pass

    def remove_item(self):
        pass

    def modify_item(self):
        pass

    def get_num_items_in_cart(self):
        pass

    def get_cost_of_cart(self):
        pass

    def print_total(self):
        pass

    def print_descriptions(self):
        pass


def print_menu(class_obj):
    customer = class_obj()
    return customer


if __name__ == "__main__":
    customer = ShoppingCart()
    customer.customer_name = input("Enter customer's name:\n")
    customer.current_date = input("Enter today's date:\n")
    print()

    print(f"Customer name: {customer.customer_name}")
    print(f"Today's date: {customer.current_date}")

    customer = print(ShoppingCart)
    print(customer)
