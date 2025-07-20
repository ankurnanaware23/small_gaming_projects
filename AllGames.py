
print("🎮 Welcome to the Game Hub!")
print("You can choose between two games:")
print("1. Random Number Game")
print("2. Snake Water Gun Game")
print("3. HangMan Game")

choice = input("Which game do you want to play? ").strip().lower()

if choice == "random number game":
    import RandomNumberGame as rng
    rng.play_game()

elif choice == "snake water gun game":
    import SnakeWaterGunGame as swg
    swg.play_game()

elif choice == "snake water gun game":
    import HangmanGame as hg
    hg.play_game

else:
    print("❌ Invalid choice! Please choose either 'Random Number Game' or 'Snake Water Gun Game'.")
    print("Exiting the Game Hub.")