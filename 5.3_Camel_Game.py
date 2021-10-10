'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
import time
# Varibles---------------------------------
# 1 wolves
# 2 hunters
# 3 paranoid
shas = 0
done = False
dead = False
hum = 0
print("Welcome to the camel game!")
print("Your goal is to travel 200 miles though deep forests")

while not done:
    print("Good Luck!")
    print("You start your adventure.")
    while not dead:
        shas = random.randint(0,3)

        time.sleep(3)
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("F. Divert from the main path (slow)")
        print("Q. Quit.")
        hum = input("- ")
        if hum.lower() == "a":
            continue
        elif hum.lower() == "b":
            continue
        elif hum.lower() == "c":
            continue
        elif hum.lower() == "d":
            continue
        elif hum.lower() == "e":
            continue
        elif hum.lower() == "f":
            continue
        elif hum.lower() == "q":
            print("You quit.")
            done = True
            break
        else:
            print("Please answer with a letter")









