'''
COIN TOSS PROGRAM
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
import random
score = 0
coin = 0
user = 0
for i in range(0,50):
    coin = random.randint(0,1)
    if 1 == coin:
        print("Heads")
        score += 1
    else:
        print("Tails")
print("You Heads",score,"times and Tails",50-score,"times" )

print("done")














