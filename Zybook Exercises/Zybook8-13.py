user_input = input("Enter input string:\n")

while user_input != "q":
    while "," not in user_input:
        print("Error: No comma in string.\n")
        user_input = input("Enter input string:\n")

    user_input = user_input.replace(" ", "").split(",")
    print(f"First word: {user_input[0]}")
    print(f"Second word: {user_input[1]}")
    print()
    user_input = input("Enter input string:\n")
