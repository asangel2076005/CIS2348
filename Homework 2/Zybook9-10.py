# Angelo Angel (2076005)
import csv

file_name = input()
file_name_list = []
unique_name_list = []

with open(file_name, "r") as csvfile:
    contents = csv.reader(csvfile)

    for row in contents:
        for word in row:
            if word not in file_name_list:
                file_name_list.append(f"{word} {row.count(word)}")

for item in file_name_list:
    if item not in unique_name_list:
        unique_name_list.append(item)

for item in unique_name_list:
    print(item)

