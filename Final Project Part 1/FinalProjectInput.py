class CsvFiles:

    def __init__(self):
        self.file_name = "none"
        self.dict = {}

    def sorted_dict(self):
        import csv
        with open(self.file_name, "r") as csv_file:
            contents = csv.reader(csv_file, delimiter=",")
            for row in contents:
                for item in row:
                    if item != row[0]:
                        continue
                    else:
                        self.dict[item] = row[1:]
        sorted_dict = dict(sorted(self.dict.items(), key=sort_by_name, reverse=True))
        return sorted_dict

    def output_items(self):
        for keys, values in self.sorted_dict().items():
            print(f"{keys}: {', '.join(values)}")

    def list_of_items(self):
        list_of_items = list(self.sorted_dict().items())
        return list_of_items

    def sorted_list_of_items(self):
        sorted_list_of_items = sorted(self.list_of_items(), reverse=True)
        return sorted_list_of_items


def sort_by_name(item):
    return item[1]


if __name__ == "__main__":
    import csv

    # ManufacturerList.csv
    manufacturer_list = CsvFiles()
    manufacturer_list.file_name = "ManufacturerList.csv"  # input("Enter manufacturer list file name:\n")
    print(manufacturer_list.sorted_dict())
    manufacturer_list.output_items()
    print()

    # PriceList.csv
    price_list = CsvFiles()
    price_list.file_name = "PriceList.csv"  # input("Enter price list file name:\n")
    print(price_list.sorted_dict())
    price_list.output_items()
    print()

    # ServiceDatesList.csv
    service_dates_list = CsvFiles()
    service_dates_list.file_name = "ServiceDatesList.csv"  # input("Enter service dates list file name:\n")
    print(service_dates_list.sorted_dict())
    service_dates_list.output_items()
    print()

    # Writes FullInventory.csv File
    with open("FullInventory.csv", "w", newline="") as full_inventory_file:
        full_inventory_writer = csv.writer(full_inventory_file)
        combined_list = zip(manufacturer_list.sorted_list_of_items(), price_list.sorted_list_of_items(), service_dates_list.sorted_list_of_items())

        full_inventory_list = []
        for row_x, row_y, row_z in combined_list:
            for item_x, item_y, item_z in zip(row_x, row_y, row_z):
                if item_x == item_y == item_z:
                    full_inventory_list.append([item_x, row_x[1], row_y[1], row_z[1]])

        # Places items by order of: item id, manufacturer name, item type, price, service date, and situation
        full_inventory = []
        for row in full_inventory_list:
            full_inventory.append([row[0], row[1][0], row[1][1], row[2][0], row[3][0], row[1][2]])

        # Writes FullInventory.csv File
        full_inventory_writer.writerows(sorted(full_inventory, key=sort_by_name))
