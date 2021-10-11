'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
import time
# Varibles---------------------------------
# 1 wolves
wolv = 0
# 2 hunters
hunt = 0
# 3 paranoid
para = 0
shas = 0 #gamemode

miles = 0
done = False
dead = False
hum = 0
day = 0
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
        if hum.lower() == "a": #Drink
            day +=1

        elif hum.lower() == "b": #Mod Sped
            continue
        elif hum.lower() == "c": #Full Sped
            miles +=
        elif hum.lower() == "d": #Stop night
            continue
        elif hum.lower() == "e": #Status check
            continue
        elif hum.lower() == "f": #Divert
            continue
        elif hum.lower() == "q": #Quit
            print("You quit.")
            done = True
            break
        else:
            print("Please answer with a letter")
        if shas == 1:
            wolv += 8
        elif shas == 2:
            hunt += 13
        else:
            para += 10

        if








