'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
#1 = rock
#2 = paper
#3 = sissors
hum = 0
import random
comp = 0
q = False
ply = 0
games = 0
win = 0
lose = 0
tie = 0
while not q:
    print("Do you want to play rock paper scissors?")
    ply = input("Ans- ")
    if ply.lower() == "yes" or ply.lower() == "ye" or ply.lower() == "y" or ply.lower() == "sure":
        for i in range(0,3):
            comp = random.randint(1,3)# Inational processing before computing------------------
            print("Rock, Paper, or Scissors?")
            hum = input("Ans- ")
            games += 1
            if hum.lower() == "rock" or hum.lower() == "r":
                hum = 1
            elif hum.lower() == "paper" or hum.lower() == "p":
                hum = 2
            elif hum.lower() == "scissors" or hum.lower == "scissor" or hum.lower == "s":
                hum = 3
            else:
                print("Please enter Rock Paper or Scissors")
                print("Try again")
                break
            if comp == 1:
                print("Comp- Rock")
            elif comp == 2:
                print("Comp- Paper")
            else:
                print("Comp- Scissors")

            if hum == 1 and comp == 2: # Logic system------------------------------
                print("You lost")
                lose += 1
            elif hum == 1 and comp == 3:
                print("You Won")
                win += 1
            elif hum == 2 and comp == 1:
                print("You Won")
                win += 1
            elif hum == 2 and comp == 3:
                print("You lost")
                lose += 1
            elif hum == 3 and comp == 2:
                print("You Won")
                win += 1
            elif hum == 3 and comp == 1:
                print("You lost")
                lose +=1
            else:
                print("Your tided")
                tie += 1            #End of Logic unit -------------------------------------

    elif ply.lower() == "no" or ply.lower() == "n" or ply.lower() == "nope":
        break
    else:
        print("Please answer with yes or no")
print("You played",games,"games.") #Score system
print("You won",win,"times.")
print("You lost",lose,"times.")
print("and tied",tie,"times")
print("done.")










