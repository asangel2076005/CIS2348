def sort_manufacturer(item):
    return item[1]


if __name__ == "__main__":
    import csv
    input_csv_file = input("Enter csv name: ")
    csv_files_dict = {}
    with open(input_csv_file, "r") as csv_file:
        contents = csv.reader(csv_file, delimiter=",")
        for row in contents:
            for item in row:
                if item != row[0]:
                    continue
                else:
                    csv_files_dict[item] = row[1:]

    print("Unsorted Dictionary")
    for keys, values in csv_files_dict.items():
        print(f"{keys}: {values}")

    sorted_csv_files_dict = dict(sorted(csv_files_dict.items(), key=sort_manufacturer))

    print("Sorted Dictionary")
    for keys, values in sorted_csv_files_dict.items():
        print(f"{keys}: {values}")
