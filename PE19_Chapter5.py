#Kelly Thackeray
#March 18, 2024
#Number guessing game

import random

def main():
    number = 0
    play = 1

    while (play > 0):
        number = random.randint(1,100)
        play = playGuessingGame(number)

    print('Thank you for playing.')

def playGuessingGame(num):
    userGuess = int(input('Enter a number between 1 to 100. 0 to quit: '))

    while userGuess > 0:
        if userGuess > num:
            print('Too high, try again')
            userGuess = int(input('Enter a number between 1 to 100. 0 to quit: '))
        elif userGuess < num:
            print('Too low, try again')
            userGuess = int(input('Enter a number between 1 to 100. 0 to quit: '))
        else:
            print('Congratulations! You guessed the correct number!')
            return userGuess
    return userGuess

main()
