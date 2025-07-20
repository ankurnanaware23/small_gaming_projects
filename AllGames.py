def game_hub():
    print("🎮 Welcome to the Game Hub!")

    while True:
        print("\nYou can choose between the following games:")
        print("1. Random Number Game")
        print("2. Snake Water Gun Game")
        print("3. Hangman Game")

        choice = input("Which game do you want to play? (Enter 1, 2, or 3): ").strip()

        match choice:
            case "1":
                import RandomNumberGame as rng
                rng.play_game()

            case "2":
                import SnakeWaterGunGame as swg
                swg.play_game()

            case "3":
                import HangmanGame as hg
                hg.play_game()

            case _:
                print("❌ Invalid choice! Please choose 1, 2, or 3.")
                continue
        
        print()
        again = input("Do you want to return to the Game Hub and play another game? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    game_hub()
