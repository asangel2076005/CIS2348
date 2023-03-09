user_input = input()
tokens = user_input.split()
token_digits = []

for num in tokens:
    num = int(num)
    token_digits.append(num)
token_digits.sort()

for num in token_digits:
    if num < 0:
        continue
    else:
        print(f"{num} ", end="")
print()

