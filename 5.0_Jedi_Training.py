  #Sign your name:________________

'''
 1. Make the following program work.
   '''

# print("This program takes three numbers and returns the sum.")
# total = 0
# for i in range(3):
#     x = int(input("Enter a number: "))
#     total += x
# print("The total is:", total)
#

'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''
# for i in range(1,100):
#     if (i % 2) == 0:
#         print(i)
# print("DOne")
#
#
#

'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''
# i = 10
# while i > -1:
#     print(i)
#     i += -1
#





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''
# import random
#
# R =  random.randint(1,10)
# print(R)
#



'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
# n = 0
# p = 0
# zero = 0
# t = 0
# for i in range (1,8):
#     x = int(input("What is a number?- "))
#     t += x
#     if x > 0:
#         p += 1
#     elif x == 0:
#         zero += 1
#     else:
#         n += 1
# print("You had",p,"positive entries")
# print("You had",n,"negative entries")
# print("You had",zero,"zero entries")
# print("You had a sum",t)