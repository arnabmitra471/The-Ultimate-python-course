num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive")
    if num <= 10:
        print("The number is between 1 and 10")
    elif num > 10 and num <= 20:
        print("The number is between 11 and 20")
    elif num > 20 and num <= 30:
        print("The number is between 21 and 30")
    elif num > 30 and num <= 40:
        print("The number is between 31 and 40")
    else:
        print("The number is greater than 40")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")
