# Angelo Angel (2076005)

user_input = input()

user_list = user_input.split(" ")
for list in user_list:

    print(f"{list} {user_list.count(list)}")