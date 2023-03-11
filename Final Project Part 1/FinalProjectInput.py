


if __name__ == "__main__":
    import csv

    print("Full Inventory List")
    full_inventory_input = "FullInventory.csv"  # input("Enter Full Inventory CSV File: ")

    with open("FullInventory.csv", "r") as full_inventory_file:
        items = csv.reader(full_inventory_file, delimiter=",")
        rows = list(items)