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
    if ply.lower() == "yes" or ply.lower() == "yeah" or ply.lower() == "y" or ply.lower() == "sure":
        print("Press s for scissors,")
        print("Press r for rock,")
        print("and Press p for paper")
        print("You can quit at anytime by pressing q")
        while not q:
            comp = random.randint(1,3)# Inational processing before computing------------------
            print("Rock, Paper, or Scissors?")
            hum = input("Ans- ")

            if hum.lower() == "rock" or hum.lower() == "r":
                hum = 1
            elif hum.lower() == "paper" or hum.lower() == "p":
                hum = 2
            elif hum.lower() == "scissors" or hum.lower() == "scissor" or hum.lower() == "s":
                hum = 3
            elif hum.lower() == "q" or hum.lower() == "quit" or hum.lower() == "leave" or hum.lower() == "l":
                q = True
                break
            else:
                print("Please enter Rock Paper or Scissors")
                print("Try again")
                i -= 1
                continue
            games += 1


            if comp == 1:
                print("Comp- Rock")
            elif comp == 2:
                print("Comp- Paper")
            elif comp == 3:
                print("Comp- Scissors")
            else:
                pass

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
                if not q:
                    print("Your tied")
                    tie += 1
                else:
                    pass                #End of Logic unit -------------------------------------

    elif ply.lower() == "no" or ply.lower() == "n" or ply.lower() == "nope":
        break
    else:
        print("Please answer with yes or no")
print("You played",games,"games.") #Score system
print("You won",win,"times.")
print("You lost",lose,"times.")
print("and tied",tie,"times")
print("done.")










