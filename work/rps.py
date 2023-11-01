#rock paper scissors
import random

class RockPaperScissors:
    def __init__(self):
        self.options = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        return random.choice(self.options)

    def get_user_choice(self):
        while True:
            user_choice = input("Rock, paper, or scissors? (r/p/s): ")
            if user_choice in self.options:
                return user_choice
            else:
                print("Invalid choice.")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif user_choice == "rock" and computer_choice == "scissors":
            return "Win"
        elif user_choice == "scissors" and computer_choice == "paper":
            return "Win"
        elif user_choice == "paper" and computer_choice == "rock":
            return "Win"
        else:
            return "Lose"

    def play_game(self):
        computer_choice = self.get_computer_choice()
        user_choice = self.get_user_choice()

        winner = self.determine_winner(user_choice, computer_choice)

        print("You chose {}.".format(user_choice))
        print("The computer chose {}.".format(computer_choice))
        print("You {}!".format(winner))

def main():
    game = RockPaperScissors()

    while True:
        play_again = input("Play again? (y/n): ")
        if play_again == "n":
            break

        game.play_game()

if __name__ == "__main__":
    main()
