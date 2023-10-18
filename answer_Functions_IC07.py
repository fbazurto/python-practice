"""
*****************************************************************
    CS 104: Introduction to Programming
    Functions(14 points total)
    Filename: functionsProgrammingInClassAssignment_IC_S17.py
    Date:   10/12/23
    Author: Fatima Bazurto
    (10 points + 4 Extra Credit total)
*****************************************************************

Write a function def countWords(string1) that returns a count
of all words in the string string1.  Words are separated by spaces.
For example, countWords(“Software eventually works, while hardware eventually fails”)
should return 7.  Try different strings!

*****************************************************************
Extra credit (4 points): write your function so that it works even if words are separated by multiple(!) spaces:

For example: “Software             eventually                   works, while               hardware eventually fails”
should return 7. Try different strings!
*****************************************************************

*****************************************************************
"""


# your code goes here:

# 1-prompt user for string

string1 = input("Please enter whatever words you like girly <3 ")
def countWords(string1):
    word_split = string1.split( )
    count = len(word_split)
    return count
print(countWords(string1))



'''
test failed when i typed string.split(' ')
however, when i took away the quotes, the 
len of the string was counted without regard to spaces
Also, when i print(word_split), the output is in a list [ , ]
answer of why from stackoverflow:
"If you don't specify the seperator, split() 
whitespace(any whitespace including tabs etc) 
is used as default separator and 
consecutive whitespaces are grouped. 
 If you specify whitespace yourself, split(' ')
consecutive whitespaces are not grouped."

i specified the seperator and changed the way the split method 
works by default
by default, all whitespace is grouped and ignored
'''



'''
if word_split != ' ':
   empty_list = empty_list + word_split
print(empty_list)
'''
