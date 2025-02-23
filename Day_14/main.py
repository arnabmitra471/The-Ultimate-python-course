# This is the main.py file for day 14
# Taking the age of the user as an input
age = int(input("Enter your age: "))
print("Your age is",age)
# Conditional operaors
# >, <, >=, <= ==, !=
print(age > 18)
print(age < 18)
print(age >= 18)
print(age <= 18)
print(age == 18)
print(age != 18)
'''
Syntax of the if statement

if condition:
    code to be executed
'''
# Checking the driving eligibility of a person based on his/her age
if age > 18:
    print("You can drive")
    print("Yes !!")
else:
    print("You cannot drive")
    print("No !!")
    print("Yay !!")
