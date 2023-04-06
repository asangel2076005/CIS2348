class Team:

    def __init__(self):
        self.name = "none"
        self.wins = 0
        self.losses = 0

    def get_win_percentage(self):
        win_percentage = self.wins / (self.wins + self.losses)
        return win_percentage

    def print_standing(self):
        print(f"Win percentage: {self.get_win_percentage():.2f}")
        if self.get_win_percentage() >= 0.5:
            print(f"Congratulations, Team {self.name} has a winning average!")
        else:
            print(f"Team {self.name} has a losing average.")


if __name__ == "__main__":
    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.name = team_name
    team.wins = team_wins
    team.losses = team_losses

    team.print_standing()
