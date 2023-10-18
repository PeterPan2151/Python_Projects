import random
import hangman_words
import hangman_art
import os


# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
print(chosen_word)

print(hangman_art.logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')


# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in range(word_length):
    display += '_'

# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
# Then you can tell the user they've won.
while True:
    if '_' not in display:
        print("You Won!!")
        break
    else:

        # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
        user_guess = input("Guess a letter: ").lower()
        os.system('cls')

        # If the user has entered a letter they've already guessed, print the letter and let them know.
        if user_guess in display:
            print(f"You've already guessed {user_guess}")

        # Loop through each position in the chosen_word;
        # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
        # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
        # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == user_guess:
                display[position] = letter

        # If guess is not a letter in the chosen_word,
        # Then reduce 'lives' by 1.
        # If lives goes down to 0 then the game should stop and it should print "You lose."
        if user_guess not in chosen_word:
            print(f"{user_guess} is not in the word.")
            lives -= 1
        print(f"lives left: {lives}")
        if lives == 0:
            print("You loose")
            break

    # Join all the elements in the list and turn it into a String.

    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])
