import random


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissors' and computer_choice == 'paper'):
        return "win"
    else:
        return "lose"


def play_game():
    options = ['rock', 'paper', 'scissors']
    wins = 0
    losses = 0
    ties = 0

    while True:
        player_choice = input("Enter your choice (rock/paper/scissors), or 'q' to quit: ").lower()
        if player_choice == 'q':
            print("Thanks for playing. Here are your results:")
            print(f"Wins: {wins}")
            print(f"Losses: {losses}")
            print(f"Ties: {ties}")
            break

        while player_choice not in options:
            print("Invalid choice. Please try again.")
            player_choice = input("Enter your choice (rock/paper/scissors), or 'q' to quit: ").lower()

        computer_choice = random.choice(options)

        print(f"\nYour choice: {player_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        if result == "win":
            print("You win!")
            wins += 1
        elif result == "lose":
            print("You lose!")
            losses += 1
        else:
            print("It's a tie!")
            ties += 1

        print()


# Start the game
play_game()
