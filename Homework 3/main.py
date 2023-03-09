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


# adds a pair to the current list
def add_player(user_dictionary):
    new_number = int(input("Enter a new player's jersey number:\n"))
    while new_number < 0 or new_number > 99:
        print("Must be between 0-99 (inclusive)")
        new_number = int(input("Enter a new player's jersey number:\n"))

    new_rating = int(input("Enter the new player's rating:\n"))
    while new_rating < 1 or new_rating > 9:
        print("Must be between 1-9 (inclusive)")
        new_rating = int(input("Enter the new player's rating:\n"))

    user_dictionary[new_number] = new_rating
    sorted_user_dictionary = dict(sorted(user_dictionary.items()))
    return sorted_user_dictionary


# removes a pair based on their keys
def remove_player(user_dictionary):
    jersey_delete = int(input("Enter a jersey number:\n"))
    print()
    del user_dictionary[jersey_delete]
    return user_dictionary


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

    checker = True

    if checker == True:
        print("ROSTER")
        for number, rating in jersey_pairs_sorted.items():
            print(f"Jersey number: {number}, Rating: {rating}")
        print()

    menu()

    user_choice = input("Choose an option:\n")
    while user_choice != "q":
        if user_choice == "o":
            if checker == False:
                output_roster(jersey_pairs_sorted)
        elif user_choice == "a":
            if checker == False:
                new_pair = add_player(jersey_pairs_sorted)
                jersey_pairs_sorted = new_pair
        elif user_choice == "d":
            if checker == False:
                print()
                new_pair = remove_player(jersey_pairs_sorted)
                jersey_pairs_sorted = new_pair
        checker = False
        user_choice = input()


