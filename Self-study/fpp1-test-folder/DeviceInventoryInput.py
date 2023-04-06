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
        sorted_list_of_items = sorted(self.list_of_items(), key=sort_by_id)
        return sorted_list_of_items


def sort_by_name(name):
    return name[1]


def sort_by_date(date):
    from datetime import datetime
    return datetime.strptime(date[4], '%m/%d/%Y')


def sort_by_name_date(name_date):
    from datetime import datetime
    return name_date[1], datetime.strptime(name_date[4], '%m/%d/%Y')


def sort_by_id(i_d):
    return i_d[0]


def sort_by_price(price):
    return int(price[3])


# Combines all csv files and places all their contents with their respective ID's
def combined_list(list1, list2, list3):
    list1 = sorted(list1, key=sort_by_id)
    list2 = sorted(list2, key=sort_by_id)
    list3 = sorted(list3, key=sort_by_id)
    general_list = []
    for row_x, row_y, row_z in zip(list1, list2, list3):
        for item_x, item_y, item_z in zip(row_x, row_y, row_z):
            if item_x == item_y == item_z:
                general_list.append([item_x, row_x[1], row_y[1], row_z[1]])
    # Places items by order of: item id, manufacturer name, item type, price, service date, and situation
    formatted_items = []
    for row in general_list:
        formatted_items.append([row[0], row[1][0], row[1][1], row[2][0], row[3][0], row[1][2]])
    return formatted_items


# Splits the mm/dd/yyyy format into their respective positions of date and convert each to int
def get_current_date():
    import datetime
    current_date = datetime.date.today()
    current_date_formatted = current_date.strftime("%m/%d/%Y")

    year = int(current_date_formatted.split("/")[2])
    day = int(current_date_formatted.split("/")[1])
    month = int(current_date_formatted.split("/")[0])
    return month, day, year


if __name__ == "__main__":
    import csv

    # ManufacturerList.csv
    manufacturer_list = CsvFiles()
    manufacturer_list.file_name = "ManufacturerList.csv"

    # PriceList.csv
    price_list = CsvFiles()
    price_list.file_name = "PriceList.csv"

    # ServiceDatesList.csv
    service_dates_list = CsvFiles()
    service_dates_list.file_name = "ServiceDatesList.csv"

    full_inventory = combined_list(manufacturer_list.sorted_list_of_items(),
                                   price_list.sorted_list_of_items(),
                                   service_dates_list.list_of_items())

    # Make Device Inventory for each items
    device_inventory_dict = {}
    for item in full_inventory:
        category = item[2]
        if category in device_inventory_dict:
            device_inventory_dict[category].append(item)
        else:
            device_inventory_dict[category] = [item]

    # Write CSV files for each devices
    for device, data in device_inventory_dict.items():
        sorted_device_inventory = sorted(data, key=sort_by_id)
        with open(f"{device.capitalize()}Inventory.csv", "w", newline="") as device_inventory:
            device_inventory_writer = csv.writer(device_inventory)
            for devices in sorted_device_inventory:
                device_inventory_writer.writerow([devices[0], devices[1], devices[3], devices[4], devices[5]])