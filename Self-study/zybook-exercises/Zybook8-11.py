user_input = input().split()

words = []
for letter in user_input:
    if letter[0].isupper():
        words.append(letter)

for word in words:
    print(f"{word[0]}.", end="")
print()
