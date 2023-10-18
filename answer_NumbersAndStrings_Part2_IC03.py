"""
*****************************************************************.

    CS 104: Introduction to Programming
    Intro (17 points)
    Filename: variables_IC03_S17_Part2.py
    Date:   Wed, Sep 6
    Author: Erek Mills
    
*****************************************************************

The code window is used to write programs.  You enter the code, save the program, run the program, and you see its output in the shell window.
For most program needs you are going to want to edit your program in a separate document and then run it.
IDLE comes with its own built-in text editor.  Saving your programs if you have a long program.  For testing quick ideas, the shell window is perfect.
"""

"""
nP2.15 page 82  Printing a grid  (6 points)
"""
#your code goes here
print("+--+--+--+")
print("|  |  |  |")
print("+--+--+--+")
print("|  |  |  |")
print("+--+--+--+")
print("|  |  |  |")
print("+--+--+--+")


print("-" * 30)
"""
nnP2.20 page 83  Christmas Tree (5 points)
"""
#your code goes here
print('   /\\ ')
print('  /  \\ ')
print(' /    \\ ')
print('/      \\ ')
print('--------')
print('  "  " ')
print('  "  " ')
print('  "  " ')

print("-" * 30)
"""
7. nnP2.16 page 82 Breaking a number into individual digits. Read a 5 digit integer and display it with spaces between each digit. (6 points)
"""
#your code goes here
number = int(input("Enter a 5-digit positive integer: "))
if number < 10000 or number > 99999:
    print("Invalid input. Please enter a 5-digit positive integer.")
else:
    number_str = str(number)

    for digit in number_str:
        print(digit, end=" ")

num1 = 10

num2 = 20

num3 = 2

result = num1 / num2 / num3

print(result)