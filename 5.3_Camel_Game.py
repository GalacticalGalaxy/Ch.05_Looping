'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
import random
import time
# Varibles---------------------------------
# 1 wolves
wolv = -20
# 2 hunters
hunt = -20
# 3 paranoid
para = 0
shasnum = 0 #3 round wait
oas = 0

pray = random.randint(1,5)
camHealth = 7
cantWat = 3
comd = 5
miles = 0
done = False
dead = False
hum = 0
day = 0
div = 0
print("\033[1;33;48m\n") # Blue
print("Welcome to the camel game!")
print("Your goal is to travel 200 miles though deep forests")

while not done:
    print("Good Luck!")
    print("You start your adventure.")
    shas = random.randint(1, 2)
    while not dead:
        oas = random.randint(1,10)
        time.sleep(2)

        print("\033[1;32;48m") #Green
        print("You have traveled", "\033[1;36;48m", miles, "\033[1;32;48m", "miles")
        print("\033[1;32;48m", "A. Drink from your canteen.") # Green
        print("\033[1;33;48m", "B. Ahead moderate speed.") # yellow
        print("\033[1;34;48m", "C. Ahead full speed.")  # blue
        print("\033[1;35;48m", "D. Stop for the night.")  # purple
        print("\033[1;36;48m", "E. Status check.")  # cyan
        print("\033[1;31;48m", "Q. Quit.")  # Red

        hum = input("- ")
        if hum.lower() == "a": #Drink------------------------
            if cantWat > 0:
                cantWat -= 1
                comd = 5
                print("\033[1;32;48m\n")  #
                print("You drank some water.")
            elif cantWat == 0 or cantWat < 0:
                print("\033[1;31;48m\n") # red and black
                print("Your all out of water")
            continue
        elif hum.lower() == "b": #Mod Sped--------------------------
            miles += 8 - div
            day += 1
            comd -= 1
            camHealth -= 2
            print("\033[1;33;48m","Your camel is walking.") #Yellow
        elif hum.lower() == "c": #Full Sped----------------------------
            miles += 16 - div
            day += 1
            comd -= 1
            camHealth -= random.randint(3,4)
            print("\033[1;34;48m\n") #Blue
            print("Your camel is running at blisting speeds.")
        elif hum.lower() == "d": #Stop night---------------------------------
            camHealth = 7
            day += 1
            for i in range(1,10):
                s = random.randint(1,30)
                time.sleep(.3)
                if s > 10 and s < 17 or s == 10:
                    print("\033[1;36;48m", "...") # Cyan
                elif s > 17 and s < 24 or s == 17:
                    print("\033[1;33;48m", "...") # Yellow
                elif s > 24 and s < 28 or s == 24:
                    print("\033[1;32;48m", "...") # Green
                elif s > 28 or s == 28:
                    print("\033[1;31;48m", "...!") # Red
                else:
                    print("\033[1;35;48m", "...") # Purple

                if s > 28: # Wake up Sleep night
                    print("You wake up to the sound twigs snapping." or print("Something woke you up."))
                    print("Will you either")
                    print("1. Check it out.")
                    print("2. Go back to sleep")
                    hum = int(input("- "))
                    if hum == 1:
                        if miles - hunt < 5 and s == 30:
                            print("You found wolves and scared them off.")
                            print("In the process you lost your sleep.")
                        elif miles - hunt < 5 and s == 30:
                            print("You found hunters and scared them off.")
                            print("In the process you lost your sleep.")
                        else:
                            print("You found nothing and you lost your sleep.")
                            break
                    elif hum == 2:
                        print("You went back to sleep")
                        if miles - wolv < 17 and s == 30:
                            print("The wolves got you")
                            done = True
                            dead = True
                            break #@@@@@@@@@@@@@@@@@@@@@@@@@########################ASK HERMON STOP COMMANSD
                        elif miles - hunt < 17 and s == 30:
                            print("The hunters got you")
                            done = True
                            dead = True
                            break #@@@@@@@@@@@@@@@@@@@@@@@@@########################ASK HERMON STOP COMMANSD
                        else:
                            camHealth = 7

                    else:
                        print("please respond with a 1 or a 2.")
                        continue

            print("\033[1;35;48m", "You stopped for the night.")
        elif hum.lower() == "e": #Status check-----------------------------------
            print("\033[1;36;48m")
            print("Your camel has", camHealth, "good days left.")
            print("You have", comd,"commands left without a drink.")
            print("You have", cantWat, "drinks left in your canteen.")
            if shas == 0:
                print("Something is", miles - wolv, "miles away")
            elif shas == 1:
                print("Something is", miles - hunt, "miles away")

            continue

        elif hum.lower() == "f": #Divert------------------------------------

            comd -= 1
        elif hum.lower() == "q": #Quit---------------------------------------------
            print("\033[1;31;48m")
            print("You quit.")
            done = True
            break
        else:
            print("\033[1;31;48m")
            print("Please answer with a letter")
            continue
        shasnum += 1

        if oas == 1: #Stream----------------------------
            print("\033[1;34;48m\n") # Blue
            print("You found a stream!")
            print("Your camel is eating figs")
            print("and Your water has been refilled!")
            cantWat = 3
            comd = 5
            camHealth = 7
                    # DEATH CODE -------------------------------------------------------------------
        # if comd == 0 or camHealth < 0 or hunt > miles or wolv > miles:
        #     print("\033[1;31;48m\n")  # Red
        #     print("You died")
        #     print("You made it", miles, "miles.")
        #     done = True
        #     dead = True
        #     break
        if comd == 0:
            print("You ran out of commands")
            print("Will you either,")
            print("A. Pray for help.")
            print("B. Quit.")
            hum = input("- ")
            if hum.lower() == "a":
                pray = random.randint(1,5)
                if pray == 5:
                    print("You were found sleeping")
                    print("You were given water")
                    continue
                else:
                    print("You were never found" or "The wolves found you first")
                    print("You died")
                    done = True
                    dead = True
                    break
            else:
                print("You gave up")
                done = True
                dead = True
                break
        if hunt > miles:
            print("The hunters caught up to you.")
            print("You died")
            done = True
            dead = True
            break
        if wolv > miles:
            print("The Wolves caught up to you.")
            print("You died")
            done = True
            dead = True
            break
        if camHealth <= 0:
            print("You ran your camel to death!")
            done = True
            dead = True
            break

        if miles >= 200: #You Won --------------------------------------------------
            print("\033[1;33;48m\n")  # Green
            print("You Won! Great Job!")
            done = True
            dead = True
            break
        if shas == 1:
            print("Something is", miles - wolv, "miles away")
            wolv += random.randint(6, 12)
        elif shas == 2:
            print("Something is", miles - hunt, "miles away")
            hunt += 9
        # elif shas == -1:
        #     para += 10
        #     print("Something is", miles - para, "miles away p")











