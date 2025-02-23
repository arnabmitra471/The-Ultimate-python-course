year = int(input("Enter a year: "))
# Leap year occuring in the century
if year % 400 == 0 and year % 100 == 0:
    print(year,"is a century leap year")
# A normal leap year
elif year % 4 == 0 and year % 100 != 0:
    print(year,"is a normal leap year")
else:
    print(year,"is not a leap year")
