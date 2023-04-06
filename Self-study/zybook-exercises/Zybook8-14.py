if __name__ == "__main__":
    user_title = input("Enter a title for the data:\n")
    print(f"You entered: {user_title}")
    print()

    header_list = []
    for i in range(1, 2+1):
        column_header = input(f"Enter the column {i} header:\n")
        print(f"You entered: {column_header}")
        print()
        header_list.append(column_header)

    data_point_str_list = []
    data_point_int_list = []
    user_data_point = input("Enter a data point (-1 to stop input):\n")
    while user_data_point != "-1":
        user_data_point = user_data_point.split(" ")
        if "".join(user_data_point).count(",") < 1:
            print("Error: No comma in string.\n")
            user_data_point = input("Enter a data point (-1 to stop input):\n")
            continue
        if "".join(user_data_point).count(",") > 1:
            print("Error: Too many commas in input.\n")
            user_data_point = input("Enter a data point (-1 to stop input):\n")
            continue
        if not "".join(user_data_point).split(",")[-1].isdigit():
            print("Error: Comma not followed by an integer.\n")
            user_data_point = input("Enter a data point (-1 to stop input):\n")
            continue

        data_point = " ".join(user_data_point)
        data_string = data_point.split(",")[0]
        data_int = int(data_point.split(",")[1])
        data_point_str_list.append(data_string)
        data_point_int_list.append(data_int)
        print(f"Data string: {data_string}")
        print(f"Data integer: {data_int}")
        print()

        user_data_point = input("Enter a data point (-1 to stop input):\n")
    print()

    # Information Table
    print(f"{user_title:>33}")
    print(f"{header_list[0]:<20}|{header_list[1]:>23}")
    print("-"*44)
    for i in range(len(data_point_int_list)):
        print(f"{data_point_str_list[i]:<20}|{data_point_int_list[i]:>23}")
    print()

    # Information Histogram
    for i in range(len(data_point_int_list)):
        print(f"{data_point_str_list[i]:>20}", "*"*data_point_int_list[i])
