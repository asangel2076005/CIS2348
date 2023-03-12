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
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")

    user_choice = input("Choose an option:\n")

    if user_choice == "o":
        print("ROSTER")
        for jersey_number, jersey_rating in jersey_roster_sorted:
            print(f"Jersey number: {jersey_number}, Rating: {jersey_rating}")
    elif user_choice == "a":
        jersey_number = int(input("Enter a new player's jersey number:\n"))
        jersey_rating = int(input("Enter the player's rating:\n"))
        jersey_roster[jersey_number] = jersey_rating
        jersey_roster_sorted = sorted(jersey_roster.items())
