# Angelo Angel (2076005)

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
        sorted_dict = dict(sorted(self.dict.items(), key=sort_by_name))
        return sorted_dict

    def output_items(self):
        for keys, values in self.sorted_dict().items():
            print(f"{keys}: {', '.join(values)}")

    def list_of_items(self):
        list_of_items = list(self.sorted_dict().items())
        return list_of_items

    def sorted_list_of_items(self):
        sorted_list_of_items = sorted(self.list_of_items())
        return sorted_list_of_items


def sort_by_name(item):
    return item[1]


def sort_by_date(item):
    from datetime import datetime
    return datetime.strptime(item[4], '%m/%d/%Y')


def sort_by_name_date(item):
    from datetime import datetime
    return item[1], datetime.strptime(item[4], '%m/%d/%Y')


def sort_by_id(item):
    return item[0]


if __name__ == "__main__":
    import csv
    from datetime import datetime

    # ManufacturerList.csv
    manufacturer_list = CsvFiles()
    manufacturer_list.file_name = input("Enter manufacturer list file name:\n")

    # PriceList.csv
    price_list = CsvFiles()
    price_list.file_name = input("Enter price list file name:\n")

    # ServiceDatesList.csv
    service_dates_list = CsvFiles()
    service_dates_list.file_name = input("Enter service dates list file name:\n")

    # Combines all csv files and places all their contents with their respective ID's
    combined_list = zip(manufacturer_list.sorted_list_of_items(),
                        price_list.sorted_list_of_items(),
                        service_dates_list.sorted_list_of_items())
    full_inventory_list = []
    for row_x, row_y, row_z in combined_list:
        for item_x, item_y, item_z in zip(row_x, row_y, row_z):
            if item_x == item_y == item_z:
                full_inventory_list.append([item_x, row_x[1], row_y[1], row_z[1]])

    # Places items by order of: item id, manufacturer name, item type, price, service date, and situation
    # !IMPORTANT USE full_inventory AS BASE FOR OTHER CSV FILES
    full_inventory = []
    for row in full_inventory_list:
        full_inventory.append([row[0], row[1][0], row[1][1], row[2][0], row[3][0], row[1][2]])

    # Writes FullInventory.csv File
    with open("FullInventory.csv", "w", newline="") as full_inventory_file:
        # Sorts full_inventory by both name and date
        full_inventory_by_dates = sorted(full_inventory, key=sort_by_name_date)
        full_inventory_writer = csv.writer(full_inventory_file)
        full_inventory_writer.writerows(full_inventory_by_dates)

    # This section separates full inventory by devices: tower, laptop, and phones
    laptop_list = []
    phone_list = []
    tower_list = []
    for devices in full_inventory:
        information_list = [devices[0], devices[1], devices[3], devices[4], devices[5]]
        if devices[2] == "laptop":
            laptop_list.append(information_list)
        elif devices[2] == "phone":
            phone_list.append(information_list)
        elif devices[2] == "tower":
            tower_list.append(information_list)

    # Writes LaptopInventory.csv
    with open("LaptopInventory.csv", "w", newline="") as laptop_inventory_file:
        # Sorts laptop_inventory by id
        laptop_inventory_by_id = sorted(laptop_list, key=sort_by_id)
        laptop_inventory_writer = csv.writer(laptop_inventory_file)
        laptop_inventory_writer.writerows(laptop_inventory_by_id)

    # Writes PhoneInventory.csv
    with open("PhoneInventory.csv", "w", newline="") as phone_inventory_file:
        # Sorts phone_inventory by id
        phone_inventory_by_id = sorted(phone_list, key=sort_by_id)
        phone_inventory_writer = csv.writer(phone_inventory_file)
        phone_inventory_writer.writerows(phone_inventory_by_id)

    # Writes TowerInventory.csv
    with open("TowerInventory.csv", "w", newline="") as tower_inventory_file:
        # Sorts tower_inventory by id
        tower_inventory_by_id = sorted(tower_list, key=sort_by_id)
        tower_inventory_writer = csv.writer(tower_inventory_file)
        tower_inventory_writer.writerows(tower_inventory_by_id)
