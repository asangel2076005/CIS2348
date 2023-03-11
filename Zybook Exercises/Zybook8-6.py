user_name = input().split()

if len(user_name) == 3:
    first_name = user_name[0]
    middle_name = user_name[1]
    last_name = user_name[2]

    first_initial = first_name.replace(first_name[1:], ".")
    middle_initial = middle_name.replace(middle_name[1:], ".")
    print(f"{last_name}, {first_initial}{middle_initial}")
else:
    first_name = user_name[0]
    last_name = user_name[1]
    first_initial = first_name.replace(first_name[1:], ".")
    print(f"{last_name}, {first_initial}")
