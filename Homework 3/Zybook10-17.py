# Angelo Angel (2076005)

class ItemToPurchase:

    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        return (f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${self.item_quantity * self.item_price:.0f}")


if __name__ == "__main__":
    items = []
    for i in range(1, 3):
        print(f"Item {i}")
        user_item_name, user_item_price, user_item_quantity = userQuery()
        user = ItemToPurchase(user_item_name, user_item_price, user_item_quantity)
        items.append(user)
        print()
