import random

def welcome_message():
    print("""Welcome to the Sanke, Wate and Gun Game!
In this game, you will play against the computer.""")

def game_rules():
    print("""The rules are simple:
🐍 Snake drinks Water → Snake wins
💧 Water douses Gun → Water wins
🔫 Gun kills Snake → Gun wins
 ❌ If both choices are the same → It's a draw

You will have 10 rounds to play.
Let's see who wins!""")


def get_computer_choice():
    return random.choice(["snake", "water", "gun"])

def get_user_choice():
    user_choice = input("Enter your choice (snake/water/gun): ").lower()

    if user_choice not in ["snake", "water", "gun"]:
        print("Invalid choice! Please choose either 'snake', 'water', or 'gun'.")
        return get_user_choice()
    
    return user_choice


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "snake" and computer_choice == "water") or \
         (user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snake"):
        return "win"
    else:
        return "lose"

def play_round():
    uc = get_user_choice()
    cc = get_computer_choice()

    print(f"Computer chose: {cc}")
    result = determine_winner(uc, cc)

    if result == "win":
        print(f"You win this round! {uc} beats {cc}.")
        return 1
    elif result == "lose":
        print(f"You lose this round! {cc} beats {uc}.")
        return -1
    else:
        print(f"It's a draw! Both chose {uc}.")
        return 0
    
def play_again():
    choice = input("Do you want to play again? (yes/no): ").lower()
    if choice == "yes":
        play_game()
    elif choice == "no":
        print("Thank you for playing! Goodbye!")
    else:
        print("Invalid choice! Please enter 'yes' or 'no'.")
        play_again()

def play_game():
    welcome_message()
    game_rules()
    Score = 0

    for i in range (10):
        print(f"\nRound {i + 1}:")
        round_result = play_round()
        Score += round_result

    print(f"\nGame Over! Your final score is: {Score}")
    if Score > 0:
        print("🏆 Congratulations! You won the game!")
    elif Score < 0:
        print("😞 Sorry! You lost the game.")
    else:
        print("😐 It's a tie!")
    
    play_again()




if __name__ == "__main__":
    play_game()


