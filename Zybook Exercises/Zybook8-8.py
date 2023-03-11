input_dict = {}
user_input = input().split()
while user_input[0] != "quit":
    input_dict[user_input[0]] = user_input[1]
    user_input = input().split()

for key, value in input_dict.items():
    print(f"Eating {value} {key} a day keeps you happy and healthy.")
