user_input = input()
user_input_stripped = user_input.replace(" ", "")

if user_input_stripped == user_input_stripped[::-1]:
    print(f"palindrome: {user_input}")
else:
    print(f"not a palindrome: {user_input}")
