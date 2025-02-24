age = int(input("Enter your age: "))

"""
Child - 0 to 12 years
Teen - 13 to 19 years
Adult - 20 to 59
Senior - 60+
"""

if age <= 0:
    print("It is an invalid age")
else:
    if age <= 12:
        print("You are a child !!")
    elif age <= 19:
        print("You are teen")
    elif age <= 59:
        print("You are an adult")
    else:
        print("You are a senior citizen")
