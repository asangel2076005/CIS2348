parts = input().split()
name = parts[0]

while parts[0] != '-1':
    try:
        age = int(parts[1]) + 1
        if not isinstance(age, int):
            raise ValueError

        print(f'{name} {age}')
    except ValueError as error:
        print(f"{name} 0")

    parts = input().split()
    name = str(parts[0])
