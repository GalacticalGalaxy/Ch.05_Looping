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
shas = random.randint(1,2) #gamemode
shasnum = 0 #3 round wait
oas = 0

camHealth = 7
cantWat = 3
comd = 4
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
    shas = random.randint(0, 2)
    while not dead:
        oas = random.randint(1,10)

        time.sleep(2)
        if oas == 1:
            print("\033[1;34;48m\n") # Blue
            print("You found a stream!")
            print("Your camel is eating figs")
            print("and Your water has been refilled!")
            cantWat = 3
            comd = 4
            camHealth = 7
        print("\033[1;37;48m\n") #
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
            if cantWat > 0:
                cantWat -= 1
                comd = 4
            elif cantWat == 0 or cantWat < 0:
                print("\033[1;30;41m\n") # red and black
                print("Your all out of water")
            continue
        elif hum.lower() == "b": #Mod Sped
            miles += 8 - div
            day += 1
            comd -= 1
            print("Your camel is walking.")
        elif hum.lower() == "c": #Full Sped
            miles += 16 - div
            day += 1
            comd -= 1
            camHealth -= random.randint(3,4)
            print("\033[1;36;40m\n")
            print("Your camel is running at blisting speeds.")
        elif hum.lower() == "d": #Stop night
            camHealth = 7
            day += 1
        elif hum.lower() == "e": #Status check
            print("Your camel has", camHealth, "good days left.")
            print("You have", comd,"commands left without a drink.")
            print("You have", cantWat, "drinks left in your canteen.")
            print()
            continue

        elif hum.lower() == "f": #Divert

            comd -= 1
        elif hum.lower() == "q": #Quit
            print("You quit.")
            done = True
            break
        else:
            print("Please answer with a letter")
        shasnum += 1

        if shasnum > 2:

            if shas == 1:
                wolv += random.randint(6,13)
                print("Something is", miles - wolv, "miles away w")
            elif shas == 2:
                hunt += 9
                print("Something is", miles - hunt, "miles away h")
            else:
                para += 10
                print("Something is", miles - para, "miles away p")
        else:
            pass
        if comd == 0 or camHealth < 0 or hunt > miles or wolv > miles:
            print("You died")
            print("You made it", miles, "miles.")
            done = True
            dead = True
            break
        if miles > 200:
            print("You Won! Great Job!")
            done = True
            dead = True
            break












