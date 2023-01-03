### ppp - python practice project

### the first script will be an applied practice of python for me to
### learn python better. This code will randomly sample an array of
### names and puth them into a list:

# create an array and sample from it
import random
from random import sample

NameArray = ["Dave", "Kathy", "Brennan", "Alyssa", "Ian",
             "Kellie", "Kieran", "Hailey", "Kellan",
             "Cali", "Finn"]
SampleLength = [1]

for len in (SampleLength):
    print(sample(NameArray, 3))

### This second script will take Hailey's name
### and spell it letter by letter

LetOne = ["H"]
LetTwo = ["A"]
LetThree = ["I"]
LetFour = ["L"]
LetFive = ["E"]
LetSix = ["Y"]

Hailey = LetOne + LetTwo + LetThree + LetFour + LetFive + LetSix
print(Hailey)

### read a file into python
#import readline

open("/Users/kieranmckeag/Desktop/Magna_Labs/Benchtop Files/file1.txt")

### rock paper scissors game
import random
import os
import re

def check_play_status():
    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input("Do you wish to play again? (yes or no): ")
            if response.lower() not in valid_responses:
                raise ValueError("You must type yes or yo")
            if response.lower() == "yes":
                return True
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("Thanks for playing!")
                exit()
        except ValueError as err:
            print(err)
def play_rps():
    play = True
    while play:
        os.system("cls" if os.name == "nt" else "clear")
        print("")
        print("Rock, Paper, Scissors - Shoot!")

        user_choice = input("Choose your move"
                            "[R]ock], [P]aper, or [S]cissors:")
        if not re.match("[SsRrPp]", user_choice):
            print("Please choose a letter:")
            print("[R]ock, [P]aper, or [S]cissors")
            continue
        print(f'You chose: {user_choice}')

        choices = ["R", "P", "S"]
        opp_choice = random.choice(choices)

        print(f"I chose: {opp_choice}")

        if opp_choice == user_choice.upper():
            print("It's a tie!")
            play = check_play_status()
        elif opp_choice == 'R' and user_choice.upper() == 'S':
            print("Rock beats scissors, I win!")
            play = check_play_status()
        elif opp_choice == "S" and user_choice.upper() == "P":
            print("Scissors beats paper, I win!")
            play = check_play_status()
        elif opp_choice == "P" and user_choice.upper() == "R":
            print('Paper betas rock, I win!')
            play = check_play_status()
        else:
            print("You win!\n")
            play = check_play_status()
if __name__ == "__main__":
    play_rps()
