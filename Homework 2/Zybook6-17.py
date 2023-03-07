# Angelo Angel (2076005)

user_password = input()
user_strong_password = ''

for char in user_password:
    if char == 'i':
        user_strong_password = user_strong_password + '!'
    elif char == 'a':
        user_strong_password = user_strong_password + '@'
    elif char == 'm':
        user_strong_password = user_strong_password + 'M'
    elif char == 'B':
        user_strong_password = user_strong_password + '8'
    elif char == 'o':
        user_strong_password = user_strong_password + '.'
    else:
        user_strong_password = user_strong_password + char

print(f"{user_strong_password}q*s")
