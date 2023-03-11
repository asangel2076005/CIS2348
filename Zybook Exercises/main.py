# first create Item class
class ItemToPurchase:
    # constructor with parameters
    def __init__(self, name="none", price=0, quantity=0, description="none"):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description

    def print_item_description(self):
        print(self.item_name + ": " + self.item_description)


# second create ShoppingCart class
class ShoppingCart:
    # constructor with parameters
    def __init__(self, name="none", date="January 1, 2016"):
        self.customer_name = name
        self.current_date = date
        self.cart_items = []

    # getters
    def get_customer_name(self):
        return self.customer_name

    def get_current_date(self):
        return self.current_date

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        # variable to check if item is found
        item_found = False
        # loop through cart_items
        for i in range(len(self.cart_items)):
            # if item is found
            if self.cart_items[i].item_name == item_name:
                # remove item
                del self.cart_items[i]
                # set item_found to true
                item_found = True
                # break out of loop
                break
        # if item is not found
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        # variable to check if item is found
        item_found = False
        # loop through cart_items
        for i in range(len(self.cart_items)):
            # if item is found
            if self.cart_items[i].item_name == item.item_name:
                # modify item
                self.cart_items[i] = item
                # set item_found to true
                item_found = True
                # break out of loop
                break
        # if item is not found
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        # variable to hold total quantity
        total_quantity = 0
        # loop through cart_items
        for i in range(len(self.cart_items)):
            # add quantity to total_quantity
            total_quantity += self.cart_items[i].item_quantity
        # return total_quantity
        return total_quantity

    def get_cost_of_cart(self):
        # variable to hold total cost
        total_cost = 0
        # loop through cart_items
        for i in range(len(self.cart_items)):
            # add cost to total_cost
            total_cost += self.cart_items[i].item_price * \
                self.cart_items[i].item_quantity
        # return total_cost
        return total_cost

    def print_total(self):
        # if cart is empty
        if len(self.cart_items) == 0:
            # output message
            print("SHOPPING CART IS EMPTY")
        else:
            # output customer name and date
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            # output message
            print("Number of Items: " + str(self.get_num_items_in_cart()))
            # output message
            print("")
            # print the name and cost of each item in cart
            for i in range(len(self.cart_items)):
                print(self.cart_items[i].item_name + " " + str(self.cart_items[i].item_quantity) + " @ $" + str(
                    self.cart_items[i].item_price) + " = $" + str(self.cart_items[i].item_price * self.cart_items[i].item_quantity))
            # output message
            print("")

    def print_descriptions(self):
        # output message
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        # output message
        print("")
        # output message
        print("Item Descriptions")
        # loop through cart_items
        for i in range(len(self.cart_items)):
            # print item description
            self.cart_items[i].print_item_description()


if __name__ == "__main__":
    # create some items to add to cart
    item1 = ItemToPurchase("Chocolate Chips", 2, 1,
                           "Chocolate Chips description")
    item4 = ItemToPurchase("Flour", 5, 1, "Flour description")
    item2 = ItemToPurchase("Sugar", 3, 1, "Sugar description")
    item3 = ItemToPurchase("Eggs", 4, 1, "Eggs description")
    # create a shopping cart
    cart = ShoppingCart("John", "January 2, 2016")
    # add items to cart
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.add_item(item4)

    # print total of cart
    cart.print_total()
    # print descriptions of cart
    cart.print_descriptions()

    print("-----------------------")

    # remove item from cart
    cart.remove_item("Sugar")
    # modify item3
    item3.item_quantity = 2
    # modify item in cart
    cart.modify_item(item3)

    # print total of cart
    cart.print_total()
    # print descriptions of cart
    cart.print_descriptions()

    # get cost of cart
    print("Total: $" + str(cart.get_cost_of_cart()))

    # get number of items in cart
    print("Number of items: " + str(cart.get_num_items_in_cart()))
