user_input = input().split()
user_letter = user_input[0]
user_word = " ".join(user_input[1:])

if user_word.count(user_letter) == 1:
    print(f"{user_word.count(user_input[0])} {user_letter}")
else:
    print(f"{user_word.count(user_input[0])} {user_letter}'s")
