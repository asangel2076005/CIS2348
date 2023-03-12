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
        sorted_csv_files_dict = dict(sorted(self.dict.items(), key=sort_manufacturer))
        return sorted_csv_files_dict.items()

    def output_items(self):
        for keys, values in self.sorted_dict():
            print(f"{keys}: {values}")


def sort_manufacturer(item):
    return item[1]


if __name__ == "__main__":
    import csv

    manufacturer = CsvFiles()
    manufacturer.file_name = input("Enter Manufacturer File name:\n")
    manufacturer.output_items()
