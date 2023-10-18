"""
*****************************************************************
    CS 104: Introduction to Programming
    Decisions Part 2(25 points total)
    Filename: decisions_Template_Part2_IC_S17.py
    Date:   9/20/23
    Author: Fatima Bazurto
*****************************************************************
# Python program to check if the input number is odd or even.
# A number is even if division by 2 give a remainder of 0.
# If remainder is 1, it is odd number.
(2 points total)
"""
# your code goes here:

num=int(input("Please enter a number>> "))
if num%2==0:
    print("EVEN")
elif num%2 == 1:
    print("ODD")












print("-" * 30)

"""
*****************************************************************
Problem «Leap year» (Easy)

Statement: Given the year number. You need to check if this year is a leap year.
If it is, print LEAP, otherwise print COMMON.

The rules in Gregorian calendar are as follows: 
a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100 
a year is always a leap year if its number is exactly divisible by 400
Make sure you do some Input Validation. 

Warning. The words LEAP and COMMON should be printed all caps. 
(5 points total)
*****************************************************************
"""
# your code goes here:
year =input("PLease enter year>> ")
if year.isdigit():
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("LEAP")
    else:
        print("COMMON")
else:
    print("Not a valid input!")














print("-" * 30)

"""
*****************************************************************
#  supermarket coupons 
Make sure you do some Input Validation.

A supermarket awards coupons depending on 
how much a customer spends on groceries. 
For example, if you spend $50, you will get a coupon worth eight percent of that amount. 
The following table shows the percent used to calculate the coupon awarded for different amounts spent. 
Write a program that calculates and prints the value of the coupon a person can receive based on groceries purchased. 

Here is a sample run:
Please enter the cost of your groceries: 14
You win a discount coupon of $ 1.12. (8% of your purchase)
Money Spent	Coupon Percentage
Less than $10	        No coupon
From  $10 to $60	8%
More than $60 to $150	10%
More than $150 to $210	12%
More than $210	        14%


(5 points total)
*****************************************************************
"""


# your code goes here:
cost = input("Please enter cost>> ")
if cost.isdigit():
    cost=int(cost )
    if 10 <= cost <= 60:
        discount = cost*(8/100)
        print(f"You win a discount coupon of $ {discount}. (8% of your purchase)")
    elif 60< cost <=150:
        discount= cost*(10/100)
        print(f"You win a discount coupon of $ {discount}. (10% of your purchase)")
    elif 150 < cost <= 210:
        discount = cost*(12/100)
        print(f"You win a discount coupon of ${discount}0. (12% of your purchase)")
    elif cost > 210:
        discount = cost*(14/100)
        print(f"You win a discount coupon of ${discount}0. (14% of your purchase)")
else:
    print("Not a valid input!")













