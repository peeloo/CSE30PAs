from random import choice
import random
import os

# File path to the dictionary.txt

dictionary_file = 'dictionary.txt'


def import_dictionary(filename):
    dictionary = {size: [] for size in range(1, 13)}
    max_size = 12
    try:
        with open(filename, 'r') as file:
            for line in file:
                word = line.strip()
                size = len(word)
                if size > max_size:
                    size = max_size
                dictionary[size].append(word)
    except Exception as e:
        print(f'An error has occurred: {e}')
    return dictionary

def get_game_options():
    default_size = random.randint(3, 12)
    default_lives = 5

    try:
        size = int(input("Please choose a size of a word to be guessed [3 – 12, default any size]: ") or default_size)
        if size < 3 or size > 12:
            print(f"Invalid input. Setting word size to {default_size}.")
            size = default_size
    except ValueError:
        print(f"Invalid input. Setting word size to {default_size}.")
        size = default_size

    print(f"The word size is set to {size}.")

    try:
        lives = int(input("Please choose a number of lives [1 - 10, default 5]: ") or default_lives)
        if lives < 1 or lives > 10:
            print(f"Invalid input. Setting number of lives to {default_lives}.")
            lives = default_lives
    except ValueError:
        print(f"Invalid input. Setting number of lives to {default_lives}.")
        lives = default_lives

    print(f"You have {lives} lives.")
    return size, lives

if __name__ == '__main__':
    dictionary = import_dictionary(dictionary_file)
    print('Welcome to the Hangman Game!')

    while True:
        size, lives = get_game_options()
        word_list = dictionary[size]
        chosen_word = choice(word_list)
        guessed_letters = []
        attempts_left = lives
        displayed_word = ""

        for letter in chosen_word:
            if letter == "-":
                displayed_word += "-"
            else:
                displayed_word += "_"

        print("\nLetters chosen:")
        print(displayed_word, f"lives: {attempts_left} {'O' * attempts_left}")

        while attempts_left > 0:
            guess = input("Please choose a new letter > ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Enter a single letter.")
            elif guess in guessed_letters:
                print("You have already chosen this letter.")
            else:
                guessed_letters.append(guess)

                if guess in chosen_word:
                    print("You guessed right!")
                    for i in range(len(chosen_word)):
                        if chosen_word[i] == guess:
                            displayed_word = displayed_word[:i] + guess + displayed_word[i+1:]
                else:
                    print("You guessed wrong, you lost one life.")
                    attempts_left -= 1

            print("\nLetters chosen:")
            print(displayed_word, f"lives: {attempts_left} {'X' * (10 - attempts_left) + 'O' * (attempts_left)}")

            if displayed_word == chosen_word:
                print(f"Congratulations!!! You won! The word is {chosen_word}!\n")
                break

        if displayed_word != chosen_word:
            print(f"You lost! The word is {chosen_word}!\n")

        play_again = input("Would you like to play again [Y/N]? ").lower()
        if play_again != 'y':
            print("Goodbye!")
            break
