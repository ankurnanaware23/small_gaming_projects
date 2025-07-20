import random
def welcome_message():
    print("Welcome to the Random Number Game!")
    print("Try to guess the number between 1 and 100.")


def game_rules():
    print("Game Rules:")
    print("1. The computer will randomly select a number between 1 and 100.")
    print("2. You will try to guess the number.")
    print("3. After each guess, you will be informed if your guess is too high, too low, or correct.")
    print("4. The game continues until you guess the correct number.")


def user_choice():
    while True:
        try:
            choice = int(input("Enter your guess (1-100): "))
            if 1 <= choice <= 100:
                return choice
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def computer_choice():
    return random.randint(1, 100)

def play_round(uc, cp, attempts):

    if( uc == cp):
        print("🎉 Congratulations! You guessed it right!")
        attempts += 1
        print(f"Total attempts: {attempts}")
        return
    elif (uc < cp):
        print("Your guess is too low.")
        attempts += 1
        play_round(user_choice(), cp, attempts)
    elif (uc > cp):
        print("Your guess is too high.")
        attempts += 1
        play_round(user_choice(), cp, attempts)

def play_again():
    while True:
        choice = input("Do you want to replay the game? (yes/no): ").lower().strip()
        if choice == "yes":
            play_game()
            break
        elif choice == "no":
            print("👋 Thank you for playing the Random Number Game!")
            print("Returning to Game Hub...")
            return 
        else:
            print("❌ Invalid input, please enter 'yes' or 'no'.")


def play_game():
    play_round(user_choice(), computer_choice(), attempts=0)
    play_again()


if __name__ == "__main__":
    welcome_message()
    game_rules()

    play_game()