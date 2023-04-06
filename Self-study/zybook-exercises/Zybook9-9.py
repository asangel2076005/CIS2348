import csv

input_file = input()
with open(input_file, "r") as user_csv:
    word_counter = csv.reader(user_csv, delimiter=",")

    output_list = []
    for row in word_counter:
        for word in row:
            if f"{word} - {row.count(word)}" not in output_list:
                output_list.append(f"{word} - {row.count(word)}")

    for word in output_list:
        print(word)
