from random import choice
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def get_choice():
    options = ["paper", "rock", "scissors"]

    # Get computer and user choice.
    while True:
        user_choice = input("Please choose rock, paper or scissors: ").strip().lower()
        computer_choice = choice(options)
        if user_choice not in options:
            print("Invalid choice. Please select either paper, rock, or scissors.\n")
        else:
            return user_choice, computer_choice


def determine_win(user, computer):
    possible_wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    return possible_wins[user] == computer


def game_play(current_round, user, comp):
    clear_screen()
    current_round += 1
    print("--|----|-- Rock-Paper-Scissors Game --|----|--")
    print(f"\nRound: {current_round}    Your score: {user}    Computer score: {comp}")
    print("----------------------------------------------\n")

    user_choice, computer_choice = get_choice()

    if computer_choice == user_choice:
        result = (
            "It's a tie! 😟😟😟 Let's see who prevails in the next round",
            user_choice,
            computer_choice,
        )
    else:
        if determine_win(user_choice, computer_choice):
            result = (
                "Well played! You win this round! 😊😊😊",
                user_choice,
                computer_choice,
            )
            user += 1
        else:
            result = (
                "Computer wins! 😒😒😒 keep trying!",
                user_choice,
                computer_choice,
            )
            comp += 1

    return ((current_round, comp, user), result)


def main():
    rounds = 0
    user_score = 0
    comp_score = 0

    while True:

        data, result = game_play(rounds, user_score, comp_score)

        rounds, comp_score, user_score = data
        print(
            f"\nYou Choose: {result[1]}\t Computer Choose: {result[2]}\nResult: {result[0]}\n"
        )

        while True:
            option = input("Would you like to play again [yes/no]: ").strip().lower()
            if option not in ("yes", "no"):
                print("You can choose either yes or no\n")
            else:
                break

        if option == "no":
            print(
                f"\nRounds: {rounds}    Your Score: {user_score}    Computer Score: {comp_score}\n"
            )
            break


if __name__ == "__main__":
    main()
