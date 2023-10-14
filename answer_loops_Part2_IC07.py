"""
*************************************************************
    CS 104: Introduction to Programming
    Loops Part2(23 points total)
    Filename: loops_Part2_Template_IC07.py
    Date:   10/3/23
    Author: Fatima Bazurto
    (20 points)
**************************************************************"""

"""*****************************************************************
P4.3 page 230, Write a program that reads a line of input and prints(10 points)

Notes:

1. Promt the user just ONCE!
2. Make sure your print the output in one line.
3. You have to output your answer on a new line every time.
For example:
a
b
c
d
e

4. for problem "c" and "d": vowels = "aeiouAEIOU"
**************************************************************"""




"""a. Uppercase Letters in String (2 points)"""
 ##your code goes here:

text= input("Enter input please>> ")
ref=text

acc = ""
for var in text:
    if var.isupper():
        acc += var

print(acc)
#print('\\')






"""b. Every second letter of the string. (2 points)"""
  ##your code goes here:

acc = ""
for values in range(1, len(text)+1):
    if(values % 2 == 0):
        acc += text[values-1]
print(acc)

#print(ref[1::2], end= '')

#Hey How MANY hours is it?



"""c. The string with all vowels replaced by an underscore. (2 points)"""
  ##your code goes here:
vowels= ['a','e','i','o','u', "A", "E", "I", "O", "U"]
for var in text:
    if var in vowels:
        text=text.replace(var,"_")
print(text)




"""d. The number of digits in the string. (2 points)"""
  ##your code goes here:
sum=0
for var in ref:
    if var.isnumeric():
        sum=sum+1
print(sum)

#lets try with 23456

"""e. The poisition of all vowels in the string. 
Print the positions separated by a space. Example: 1 5 10 35 """
##your code goes here:

vowels = "aeiouAEIOU"
vowels = list(vowels)
acc= ""

for index, var in enumerate(ref):
    if( var.lower() in vowels):
        acc += str(index) + " "
print(acc)


print("-" * 30)
"""****************************************************************
P4.6 page 230, Minimum Value (4 points)
IMPORTANT: Make the loop break when a "q" is entered.
*****************************************************************"""
 ## your code goes here:

while ref != 'q':
    ref = input("Enter input please>> ")
    if ref == "3" or ref=="-4":
            print(ref)

'''
# Start with an empty list. You can 'seed' the list with
#  some predefined values if you like.
names = []
# Set new_name to something other than 'quit'.
new_name = ''
# Start a loop that will run until the user enters 'quit'.
while new_name != 'quit':
    # Ask the user for a name.
    new_name = input("Please tell me someone I should know, or enter 'quit': ")

    # Add the new name to our list.
    names.append(new_name)

# Show that the name has been added to the list.
print(names)'''
print("-" * 30)
"""*****************************************************************
(6 points) Write a Python program to construct the following pattern, using a nested loop number. 
Expected Output: 
1
22
333
4444
55555
666666
7777777
88888888
999999999

**************************************************************"""

 ## your code goes here:

BASE_SIZE = 9
for r in range(BASE_SIZE + 1):
    for c in range(r):
        print(r,end="")
    print()
#vowel_position=[str(index + 0) for index, var in enumerate(text) if var in vowels]
#print(" ".join(vowel_position))