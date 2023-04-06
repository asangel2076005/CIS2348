input_file = input()

with open(input_file, "r") as user_file:
    contents = user_file.readlines()

file_list = []
for line in contents:
    line = line.replace("\n", "")
    file_list.append(line)

file_dict = {}
for line in range(0, len(file_list), 2):
    file_dict[file_list[line+1]] = int(file_list[line])

# outputs the shows in output_titles.txt
show_sorted = sorted(file_dict, reverse=True)
with open("output_titles.txt", "w") as output_titles:
    for channel in show_sorted:
        output_titles.write(f"{channel}\n")

# outputs the channel: shows in output_keys.txt
pseudo_channels_dict = {}
for keys, values in file_dict.items():
    pseudo_channels_dict[keys] = values

channels_dict = {}
for keys, values in pseudo_channels_dict.items():
    if values not in channels_dict:
        channels_dict[values] = [keys]
    else:
        channels_dict[values].append(keys)

channels_dict_sorted = dict(sorted(channels_dict.items(), reverse=True))
with open("output_keys.txt", "w") as output_keys:
    for keys, values in channels_dict_sorted.items():
        output_keys.write(f"{keys}: {'; '.join(values)}\n")
