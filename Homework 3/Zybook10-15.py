# Angelo Angel (2076005)

class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        percentage = self.wins / (self.wins + self.losses)
        return percentage

    def print_standing(self):
        percentage = self.get_win_percentage()

        print(f"Win percentage: {percentage:.2f}")
        if percentage >= 0.50:
            print(f"Congratulations, Team {self.name} has a winning average!")
        else:
            print(f"Team {self.name} has a losing average")


if __name__ == "__main__":
    team = Team()

    user_name = input()
    user_wins = int(input())
    user_losses = int(input())

    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    team.print_standing()