'''
This is a simple python game called "Guess The Word.
It randomly chooses 1 word from the list and ask users to guess it.
'''

import random

class GuessWord():

    # List of words
    words = ["cat", "dog", "Lion", "tiger", "Elephant"]

    # logic of the code
    def logic(self):

        # selecting a random word  from the list
        # and making a list out of it
        word = random.choice(self.words)
        word_list = [*(word).lower()]

        # this is for user when he guesses single alphabet
        display_alpha = ['#']*len(word_list)
        chances = 3

        while chances:
            print(display_alpha)
            user_guess = input("Enter the alphabet or the word: ")

            # if the word is guessed break out of the loop
            if word.lower() == user_guess:
                print("You gussed it right!!!!")
                break

            # if user has guessed single alphabet of the word, display it
            elif len(user_guess) == 1 and (user_guess in word_list):
                index = word_list.index(user_guess)
                display_alpha[index] = user_guess
                chances -= 1
                print(f"You are left with {chances} chances...")

            else:
                chances -= 1
                print(f"You are left with {chances} chances...")


guess = GuessWord()
guess.logic()