"""This program runs an interactive game similar to that of Wordle."""

import random

def score_guess(guess, target):
    """This function returns a result with clues, based on how close to the target word, the guess word is.
    Clues include:
    0 - The letter is not matching at that location or in the word
    1 - The letter is not matching at that location, but is in the word
    2 - The letter is matching at that location

    An example is:
    score_guess("onion", "blood")
     [1, 0, 0, 2, 0]"""

    score = [0]*len(target)
    for i in range(len(guess)):
        if guess[i] == target[i]:
            score[i] = 2
        elif guess[i] in target:
            score[i] = 1
        else:
            score[i] = 0
    return score

introduction = ("\nHi and Welcome to Word Guess!\n\n"
      "The aim of this game is to correctly guess a secret 5-letter word!\n\n"
      "You will have 6 attempts to achieve success!\n\n"
      "Good Luck!\n")

reminder = ("For a reminder of the instructions on how to play, please type 'help' in the prompt at any time!\n")

help_message = ("Instructions:\n"
                "A 2 indicates a letter is in the correct position!\n"
                "A 1 indicates a letter is in the word but in the wrong position!\n"
                "A 0 indicates a letter is not in the word at all!\n")

print(introduction)

print(reminder)

print(help_message)

# print(f"Debug: {help_message}")

with open("all_words.txt", "r") as all_words:
    all_word_list = []
    for word in all_words:
        all_word_list.append(word.strip())
# print(f"All Words\nThe first five words: {all_lines[:5]}\n The last five words: {all_lines[-5:]}\n")

with open("target_words.txt", "r") as target_words:
    target_word_list = []
    for objective in target_words:
        target_word_list.append(objective.strip())
    target_word = random.choice(target_word_list)
target = target_word
# print(f"Target Words\nThe first five words: {target_lines[:5]}\n The last five words: {target_lines[-5:]}")

print(f"Debug Test Target Word: {target}\n")

tries_remaining = 6
while tries_remaining > 0:
    attempt = input("Your guess please: ")
    attempt = attempt.lower()
    if attempt in all_word_list:
        guess = attempt
        print(score_guess(guess, target))
        if score_guess(guess, target) == [2, 2, 2, 2, 2]:
            print("\nYou Guessed The Secret Word!\n")
            print("Thanks For Playing!")
            break # program ends here
        tries_remaining -= 1
        print(f"\nYou have {tries_remaining} tries remaining!")
    elif attempt == "help":
        print(help_message)
    elif len(attempt) != len(all_word_list[0]):
        print("Word is wrong size!")
    else:
        print("Not a valid word!")

if tries_remaining == 0:
    print(f"\n\nThe Secret Word Is {target.upper()}!\n\nBetter Luck Next Time!\n")
    print("Thanks For Playing!") # program ends here

# print(len(all_lines[0])) #Debug to check the length of a word in all_words.txt

# Barrie Seldon, 20146589, 06/04/25

# guess = "world"
# print("Guess> ", guess)
# target = "world"
# print("Target> ", target)
#
# print("Outcome> ", score_guess("world", "world"))
# print("Expected> ", [2, 2, 2, 2, 2])

# guess = "world"
# print("Guess> ", guess)
# target = "hello"
# print("Target> ", target)
#
# print("Outcome> ", score_guess("world", "hello"))
# print("Expected> ", [0, 0, 0, 0, 0])

# guess = "world"
# print("Guess> ", guess)
# target = "hello"
# print("Target> ", target)
#
# print("Outcome> ", score_guess("world", "hello"))
# print("Expected> ", [0, 1, 0, 2, 0])







