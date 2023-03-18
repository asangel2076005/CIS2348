def get_age():
    age = int(input())
    if not (age >= 18) or not (age <= 75):
        raise ValueError("Invalid age.")
    return age


def fat_burning_heart_rate(age):
    heart_rate = (220 - age) * 0.70
    return heart_rate


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)

        print(f"Fat burning heart rate for a 35 year-old: {heart_rate:.1f} bpm")

    except ValueError as error:
        print(error)
        print("Could not calculate heart rate info.")
        print()
