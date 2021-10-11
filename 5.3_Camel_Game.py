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
shasnum = 0 #3 round wait

camHealth = 7
cantWat = 5
miles = 0
done = False
dead = False
hum = 0
day = 0
div = 0
print("Welcome to the camel game!")
print("Your goal is to travel 200 miles though deep forests")

while not done:
    print("Good Luck!")
    print("You start your adventure.")
    shas = random.randint(0, 3)
    while not dead:

        shasnum += 1
        time.sleep(2)
        print("You have traveled", miles, "miles")
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("F. Divert from the main path (slow)")
        print("Q. Quit.")
        hum = input("- ")
        if hum.lower() == "a": #Drink
            cantWat -= 1
            continue
        elif hum.lower() == "b": #Mod Sped
            miles += 8 - div
            day += 1
            print("Your camel is walking.")
        elif hum.lower() == "c": #Full Sped
            miles += 16 - div
            day += 1
            print("Your camel is running at blisting speeds.")
        elif hum.lower() == "d": #Stop night
            camHealth += 7
            day += 1
        elif hum.lower() == "e": #Status check
            print()
            print()
            print()
            print()
            continue

        elif hum.lower() == "f": #Divert
            continue
        elif hum.lower() == "q": #Quit
            print("You quit.")
            done = True
            break
        else:
            print("Please answer with a letter")

        if shasnum > 2:

            if shas == 1:
                wolv += random.randint(6,13)
                print("Something is", miles - wolv, "miles away")
            elif shas == 2:
                hunt += 9
                print("Something is", miles - hunt, "miles away")
            else:
                para += 10
                print("Something is", miles - para, "miles away")
        else:
            pass










