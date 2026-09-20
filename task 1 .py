import random

def choose_word():
    
    words = ["python", "hangman", "computer", "keyboard", "program"]
    return random.choice(words)

def display_hangman(wrong_guesses):
  
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    return stages[wrong_guesses]

def play_hangman():
    word = choose_word()
    guessed_letters = []          
    wrong_guesses = 0
    max_wrong = 6

    print("=" * 40)
    print("      WELCOME TO HANGMAN GAME")
    print("=" * 40)
    print(f"In word {len(word)} letters are present . Guess now!\n")

    
    display_word = ["_"] * len(word)

    while wrong_guesses < max_wrong:
        print(display_hangman(wrong_guesses))
        print("Word: " + " ".join(display_word))
        print(f"wrong guesses: {wrong_guesses}/{max_wrong}")
        print(f"already guessed letters: {', '.join(guessed_letters) if guessed_letters else 'no letter'}")

        guess = input("\nGuess one letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("\n⚠️  Enter a single letter!\n")
            continue

        if guess in guessed_letters:
            print(f"\n⚠️  you had already enteres  '{guess}'  try again!\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"\n✅ correct ! '{guess}' this is present in the word.\n")
        
            for index, letter in enumerate(word):
                if letter == guess:
                    display_word[index] = guess
        else:
            wrong_guesses += 1
            print(f"\n❌ wrong guess! '{guess}' not present .\n")

        
        if "_" not in display_word:
            print(display_hangman(wrong_guesses))
            print("Word: " + " ".join(display_word))
            print("\n🎉 CONGRATULATIONS! you have guessed the word correct! 🎉")
            print(f"The word was: {word.upper()}")
            break

    else:
        
        print(display_hangman(wrong_guesses))
        print("\n💀 GAME OVER! you lose.")
        print(f"The word was: {word.upper()}")


def main():
    play_again = "yes"
    while play_again == "yes":
        play_hangman()
        play_again = input("\n want to play again? (yes/no): ").lower().strip()
        print("\n")

    print("thanks for playing ..good bye!")


if __name__ == "__main__":
    main()

