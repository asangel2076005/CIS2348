# Angelo Angel (2076005)

def get_age():
    age_sample = int(input())
    if not (age_sample >= 18) or not (age_sample <= 75):
        raise ValueError("Invalid age.")
    return age_sample


def fat_burning_heart_rate(age_sample):
    heart_rate_sample = (220 - age_sample) * 0.70
    return heart_rate_sample


if __name__ == "__main__":
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)

        print(f"Fat burning heart rate for a 35 year-old: {heart_rate:.1f} bpm")

    except ValueError as error:
        print(error)
        print("Could not calculate heart rate info.")
        print()
