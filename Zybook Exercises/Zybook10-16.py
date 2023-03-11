class ItemToPurchase:

    def __init__(self, name="none", price=0.0, quantity=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

    def get_item_cost(self):
        item_cost = self.item_price * self.item_quantity
        return item_cost

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:.0f} = ${self.get_item_cost():.0f}")


if __name__ == "__main__":
    items = []
    for i in range(1, 2+1):
        print(f"Item {i}")
        item_name = input(f"Enter the item name:\n")
        item_price = float(input(f"Enter the item price:\n"))
        item_quantity = int(input(f"Enter the item quantity:\n"))
        print()
        item = ItemToPurchase(item_name, item_price, item_quantity)
        items.append(item)

    total_cost = 0
    print("TOTAL COST")
    for item in items:
        item.print_item_cost()
        total_cost = total_cost + item.get_item_cost()
    print()
    print(f"Total: ${total_cost:.0f}")
