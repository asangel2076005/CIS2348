# Angelo Angel (2076005)

jersey_roster = {}

for i in range(1, 5+1):
    jersey_number = int(input(f"Enter player {i}'s jersey number:\n"))
    jersey_rating = int(input(f"Enter player {i}'s rating:\n"))
    print()
    jersey_roster[jersey_number] = jersey_rating

jersey_roster_sorted = sorted(jersey_roster.items())

print("ROSTER")
for jersey_number, jersey_rating in jersey_roster_sorted:
    print(f"Jersey number: {jersey_number}, Rating: {jersey_rating}")

while True:
    print()
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()

    user_choice = input("Choose an option:\n")

    if user_choice == "o":
        print("\nROSTER")
        for jersey_number, jersey_rating in jersey_roster_sorted:
            print(f"Jersey number: {jersey_number}, Rating: {jersey_rating}")
    elif user_choice == "a":
        jersey_number = int(input("Enter a new player's jersey number:\n"))
        jersey_rating = int(input("Enter the player's rating:\n"))
        jersey_roster[jersey_number] = jersey_rating
        jersey_roster_sorted = sorted(jersey_roster.items())
        print("\nPlayer added.")
    elif user_choice == "d":
        jersey_number = int(input("Enter a jersey number:\n"))
        if jersey_number in jersey_roster:
            del jersey_roster[jersey_number]
            jersey_roster_sorted = sorted(jersey_roster.items())
        else:
            print("\nThat player is not in the roster.")
    elif user_choice == "u":
        jersey_number = int(input("Enter a jersey number:\n"))
        if jersey_number in jersey_roster:
            jersey_rating = int(input("Enter a new rating for player:\n"))
            jersey_roster[jersey_number] = jersey_rating
            jersey_roster_sorted = sorted(jersey_roster.items())
        else:
            print("\nThat player is not in the roster.")
    elif user_choice == "r":
        rating = int(input("Enter a rating:\n"))
        print(f"\nABOVE {rating}")
        for jersey_number, jersey_rating in jersey_roster_sorted:
            if jersey_rating > rating:
                print(f"Jersey number: {jersey_number}, Rating: {jersey_rating}")
    elif user_choice == "q":
        break
