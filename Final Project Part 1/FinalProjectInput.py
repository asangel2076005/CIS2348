

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
                    csv_files_dict[item] = [row[1:]]
    print(csv_files_dict)
