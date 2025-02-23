apple_price = 210
budget = 200

# Checking if we can buy the apples or not
# Using if else statement
if apple_price <= budget :
    print("Alexa, add 1 kg apples to the cart")
else:
    print("Alexa, do not add 1 kg apples to the cart")

# Program to check if a number is positive,negative or zero
# Using if elif else statement
num = int(input("Enter a number: "))

if num > 0:
    print("It is positive")
elif num == 0:
    print("It is zero")
elif num == -999:
    print("The number is very special !!")
else:
    print("It is negative")

print("I am happy now !!")