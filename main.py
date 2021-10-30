# highLow.py
#
# Python Bootcamp Day 12 - High Low Game
# Usage:
#      Pick a number between 1 and 100 with 2 levels of difficulty.
#
# Marceia Egler October 6, 2021

import random
from art import logo

print(logo)

def guess():
    number = random.randint(1,100)    
    guess_loop = True

    EASY = 10
    HARD = 5

    print("Welcome to the guessing game!\nI'm thinking of a number between 1 and 100.")    
    
    def set_difficulty():
        '''Set number of turns a player will be given.'''
        difficulty = input("Choose a difficulty. Easy or Hard: ").lower()
        if difficulty == 'easy':
            return EASY
        if difficulty == 'hard':
            return HARD

    turns = set_difficulty()

    def make_guess(guess:int, answer:int, turns:int):
        '''Compare guess to answer. Returns # of guesses remaining.'''
        if guess > answer:
            print("Too high.")
            return turns - 1
        elif guess < answer:
            print("Too low.")
            return turns - 1
        else:
            print(f"You got it! The number was {answer}.")

    while guess_loop:
        
        print(f"You have {turns} attempts remaining to guess the number.")        
        user_guess = int(input("Make a guess: "))
        turns = make_guess(user_guess, number, turns)
        if turns == 0:
            print("You ran out of guesses. Game over.")
            guess_loop = False
        elif user_guess != number:
            print("Try again")
      

guess()