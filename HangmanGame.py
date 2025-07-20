import random

def gameName():
    print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/""")
    
hangman_stages = [
    '''
     -----
     |   |
     |   
     |   
     |  
     |
    _|_
    ''',
    '''
     -----
     |   |
     |   O
     |   
     |  
     |
    _|_
    ''',
     '''
     -----
     |   |
     |   O
     |   |
     |  
     |
    _|_
    ''',
    '''
     -----
     |   |
     |   O
     |  /|
     |  
     |
    _|_
    ''',

    '''
     -----
     |   |
     |   O
     |  /|\\
     |  
     |
    _|_
    ''',
    '''
     -----
     |   |
     |   O
     |  /|\\
     |  / 
     |
    _|_
    ''',
    '''
     -----
     |   |
     |   O
     |  /|\\
     |  / \\
     |
    _|_
    '''
]

def replay():
    while True:
        choice = input("Do you want to replay the game? (yes/no): ").lower().strip()
        if choice == "yes":
            play_game()
            break
        elif choice == "no":
            print("👋 Thank you for playing the Hangman Game!")
            break
        else:
            print("❌ Invalid input, please enter 'yes' or 'no'.")


def randomWord():
    words_list = ["choose", "banana", "orange", "laptop", "window", "rocket", "misile", "animal", "button", "garden"]
    return random.choice(words_list)

def play_game():
    gameName()

    choosenWord = randomWord()
    print(f"The word has {len(choosenWord)} letters.")
    
    placeholder = "_ "
    print(f"Word : {placeholder * 6}")
    print()

    guessed_word = ["_"] * len(choosenWord)
    guessed_letter = []
    numOfGuess = 0
    maxGuess = len(choosenWord)

    def is_word_complete():
        return "_" not in guessed_word

    while not is_word_complete() and numOfGuess < maxGuess:
        
        guess = input("Enter your guess : ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter only one valid alphabet letter at a time.")
            print(f"******************** lives left {maxGuess - numOfGuess}/6 ********************")
            print(hangman_stages[numOfGuess])
            print()
            continue

        if guess in guessed_letter:
            print("⚠️ you already guessed this word")
            print(f"******************** lives left {6 - numOfGuess}/6 ********************")
            print(hangman_stages[numOfGuess])
            print()
            continue
        elif guess in choosenWord:
            guessed_letter.append(guess)

        if guess in choosenWord:
            if len(guess) == 1:
                for i in range (len(choosenWord)):
                    if choosenWord[i] == guess:
                        guessed_word[i] = guess
            print()
            print(f"✅ correct Guess, '{guess}' is present in the word.")   

        else:
            numOfGuess += 1
            print(f"❌ Incorrect Guess, '{guess}' is not present in the word.")
            
        print(f"******************** lives left {6 - numOfGuess}/6 ********************")
        print(hangman_stages[numOfGuess])
        print(" ".join(guessed_word))
        print()

    if is_word_complete():
        print("🎉 Congratulations! You guessed the word correctly!")
    else:
        print(f"💀 Game Over. The word was: {choosenWord}")

    guessed_letter.clear()
    guessed_word.clear()

    replay()

if __name__ == "__main__":
    play_game()