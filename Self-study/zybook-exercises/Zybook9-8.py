input_file = input()
upper_bound = input()
lower_bound = input()

with open(input_file, "r") as file:
    contents = file.readlines()

# gets rid of \n characters
words = []
for word in contents:
    new_word = word.rstrip("\n")
    words.append(new_word)

for word in words:
    if (word >= upper_bound) and (word <= lower_bound):
        print(f"{word} - in range")
    else:
        print(f"{word} - not in range")