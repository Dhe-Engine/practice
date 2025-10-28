import random

def play_game():
    option_list = ["rock","paper","scissors"]

    user_choice = input("Choose between 'rock','paper','scissor': \n").lower()
    computer_choice = random.choice(option_list)

    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It is a tie")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "paper":
        if computer_choice == "scissor":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "scissor":
        if computer_choice == "rock":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print(f"Out of range: '{user_choice}'")

while True:
    play_game()