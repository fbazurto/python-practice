"""
*****************************************************************.

CS 104: Introduction to Programming
Introduction to Python. InClass (12 points)
Filename: DecisionsPart1_IC01_F17.py
Date: 9/13/23
Author: Fatima Bazurto
*****************************************************************

String Comparisons (see page 128 - 129)(7 points)
Promt the user for a string.


Write a program that reads in a string and prints whether it • contains only letters.
•	contains only uppercase letters.
•	contains only lowercase letters.
•	contains only digits.
•	contains only letters and digits.
•	starts with an uppercase letter.
•	ends with a period.


"""
#your code goes here

phrase = input("Please enter phrase >> ")
if phrase.isalpha():
    print("contains only letters.")
if phrase.islower():
    print("contains only lowercase letters.")
if phrase.isdigit():
    print("contains only digits.")
if phrase.isalnum():
    print("contains only letters and digits.")
if phrase[0].isupper():
    print("starts with an uppercase letter.")
if phrase.endswith("."):
    print("ends with a period.")

print("-" * 30)

""" Seasons (5 points)


The following algorithm yields the season (Spring, Summer, Fall, or Winter) for a given month and day.

If month is 1, 2, or 3, season = "Winter" 
Else if month is 4, 5, or 6, season = "Spring"
Else if month is 7, 8, or 9, season = "Summer"
Else if month is 10, 11, or 12, season = "Fall"
If month is divisible by 3 and day >= 21
	 	If season is "Winter", season = "Spring" 
	 	Else if season is "Spring", season = "Summer" 
	 	Else if season is "Summer", season = "Fall" 
	 	Else season = "Winter" 


Write a program that prompts the user for a month and day and then prints the season, as determined by this algorithm.

"""
#your code goes here
month = int(input("Please enter a month>>"))
day = int(input("PLease enter a day>> "))
if (month <= 3 and month % 3 ==0 and day >= 21):
    print("Spring")
elif (month >= 12 and month % 3 == 0 and day>= 21):
    print("Winter")
elif (month % 3 == 0 and month >3 and month < 9 and day >= 21):
    print("Summer")
elif(month %3 == 0 and month >8 and month <12 and day>=21):
    print("Fall")
