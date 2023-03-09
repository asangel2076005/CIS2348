# Angelo Angel (2076005)

def menu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()


def output_roster(user_dictionary):
    print("ROSTER")
    for number, rating in user_dictionary.items():
        print(f"Jersey number: {number}, Rating: {rating}")
    print()


if __name__ == "__main__":
    jersey_number = []
    jersey_rating = []

    for i in range(1, 5 + 1):
        user_number = int(input(f"Enter player {i}'s jersey number:\n"))
        user_rating = int(input(f"Enter player {i}'s rating:\n"))
        print()
        if (0 <= user_number <= 99) and (1 <= user_rating <= 9):
            jersey_number.append(user_number)
            jersey_rating.append(user_rating)

    # sorts pairs based on their keys
    jersey_pairs = dict(zip(jersey_number, jersey_rating))
    jersey_pairs_sorted = dict(sorted(jersey_pairs.items()))

    print("ROSTER")
    for number, rating in jersey_pairs_sorted.items():
        print(f"Jersey number: {number}, Rating: {rating}")
    print()

    menu()

    user_choice = input("Choose an option:\n")
    print()

    while user_choice != "q":
        if user_choice == "o":
            output_roster(jersey_pairs_sorted)
        user_choice = input()