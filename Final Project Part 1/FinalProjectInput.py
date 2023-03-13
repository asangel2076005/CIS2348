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


def sort_by_name(item):
    return item[1]


if __name__ == "__main__":
    import csv

    # ManufacturerList.csv
    manufacturer_list = CsvFiles()
    manufacturer_list.file_name = input("Enter manufacturer list file name:\n")
    print(manufacturer_list.sorted_dict())
    manufacturer_list.output_items()
    print()

    # PriceList.csv
    price_list = CsvFiles()
    price_list.file_name = input("Enter price list file name:\n")
    print(price_list.sorted_dict())
    price_list.output_items()
    print()

    # ServiceDatesList.csv
    service_dates_list = CsvFiles()
    service_dates_list.file_name = input("Enter service dates list file name:\n")
    print(service_dates_list.sorted_dict())
    service_dates_list.output_items()
    print()
