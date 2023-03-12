class CsvFiles:

    def __init__(self):
        self.file_name = "none"
        self.dict = {}

    def _sorted_dict(self):
        import csv
        with open(self.file_name, "r") as csv_file:
            contents = csv.reader(csv_file, delimiter=",")
            for row in contents:
                for item in row:
                    if item != row[0]:
                        continue
                    else:
                        self.dict[item] = row[1:]
        sorted_csv_files_dict = dict(sorted(self.dict.items(), key=sort_manufacturer))
        return sorted_csv_files_dict.items()

    def output_items(self):
        for keys, values in self._sorted_dict():
            print(f"{keys}: {values}")


def sort_manufacturer(item):
    return item[1]


if __name__ == "__main__":
    import csv

    # ManufacturerList.csv
    manufacturer_list = CsvFiles()
    manufacturer_list.file_name = input("Enter manufacturer list file name:\n")
    manufacturer_list.output_items()
    print()

    # PriceList.csv
    price_list = CsvFiles()
    price_list.file_name = input("Enter price list file name:\n")
    price_list.output_items()
    print()

    # ServiceDatesList.csv
    service_dates_list = CsvFiles()
    service_dates_list.file_name = input("Enter service dates list file name:\n")
    service_dates_list.output_items()
    print()
