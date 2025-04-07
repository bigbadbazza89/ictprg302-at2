print("Hi and Welcome to Wordle!\n"
      "The aim of this game is to correctly guess a secret 5-letter word!\n"
      "You will have 6 attempts remaining to achieve success!\n")

import random

with open("all_words.txt", "r") as all_words:
    all_lines = []
    for a_word in all_words:
        all_lines.append(a_word.strip())

with open("target_words.txt", "r") as target_words:
    target_lines = []
    for t_word in target_words:
        target_lines.append(t_word.strip())
    target_word = random.choice(target_lines)
target = target_word

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
    for letter in range(len(guess)):
        if guess[letter] == target[letter]:
            score[letter] = 2
        elif guess[letter] in target:
            score[letter] = 1
        else:
            score[letter] = 0
    return score

tries_remaining = 6
while tries_remaining > 0:
    attempt = input("Your guess please: ")
    attempt = attempt.lower()
    if attempt in all_lines:
        guess = attempt
        print(score_guess(guess, target))
        tries_remaining -= 1
        print(f"You have {tries_remaining} tries remaining")
    else:
        print("Not a suitable word!")


if tries_remaining == 0:
    print("\nBetter Luck Next Time!")


# Barrie Seldon, 20146589, 06/04/25

# guess = "onion"
# print("Guess> ", guess)
# target = "blood"
# print("Target> ", target)







