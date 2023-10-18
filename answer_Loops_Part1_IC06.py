"""***************************************************************
    CS 104: Introduction to Programming
    Loops(18 points total)
    Filename: loops_Part1_IC05.py
    Date:   9/25/23
    Author: Fatima Bazurto
**************************************************************"""

"""**************************************************************
Write a nested loop to make the following pattern: (2 points)
* * * * * *
* * * * * *
* * * * * *

**************************************************************"""
# your code goes here:
for i in range(3):
    print("* * * * * *")

print("-" * 30)
"""*************************************************************
Display each character in a word on a separate line. (2 points)
For example, if the user provides the input "Python", the program prints:
P
y
t
h
o
n

*************************************************************"""
# your code goes here:

text = input("Please enter whatever text you want>> ")
for x in text:
    print(x)





print("-" * 30)
"""*************************************************************
(4 points)
Write a program that reads a word and  print it IN REVERSE.
For example, if the user provides the input "Python", the program prints: "nohtyP"


*************************************************************"""
# your code goes here:
text = input("Please type whatever you want girlie>> ")[::-2]
for x in text:
    print(x)







print("-" * 30)
"""*************************************************************

Write a program with loops that compute:  (10 points total)

1. Use a loop to sum the even numbers from 2 to 100 (inclusive)

2. Compute the sum of all of the squares from 1 to 10 (exlusive).

3. Compute all powers of 2 from 2 ** 0 to 2 ** 20 (inclusive).

4. Compute the sum of all odd integers between a and b(inclusive) where a and b are inputs.

5. Compute the sum of the odd digits in an input. For example:

    If the input is "32a7b79" then sum = 3 + 7 + 7 + 9 = 26.

    Note: make sure to do input validation(!).


*************************************************************"""

# your code goes here:
#1
sum = 0
for i in range(2,101,2):
    sum = sum +i
print(sum)

#2
sum = 0
for var in range (1,10):
    sum =sum + (var**2)
print(sum)

#3
sum = 0
for var in range (0, 21,1):
    sum = (2**var)
    print(sum)

#4
a = int(input("enter an integer pls>> "))
b = int(input("enter an integer pls>> "))
sum=0                            #Compute the sum of all odd integers between a and b(inclusive) where a and b are inputs.
if a% 2 != 0:
    for i in range(a, b +1,2):
        sum = sum + i
    print(sum)
else:
    a = a+1
    if a % 2 != 0:
        for i in range(a, b + 1, 2):
            sum = sum + i
        print(sum)

#5
answer = input('Please enter a phrase with letters and numbers>> ')
sum = 0
for var in answer:
    if var.isdigit():
        var=int(var)
        if var %2 != 0:
            sum = sum + var
print(sum)













