"""
Write a program to count the uppercase and lowercase characters,digits
and spaces in a string given by the user as input
"""

str1 = input("Enter a string: ")
# Finding the length of the string
n = len(str1)
# Initializing the variables
upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0

# Iterating through the entire string
for i in str1:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1
    elif i.isdigit():
        digit_count += 1
    elif i.isspace():
        space_count += 1

print("The number of uppercase characters is",upper_count)
print("The number of lowercase characters is",lower_count)
print("The number of digit characters is",digit_count)
print("The number of space characters is",space_count)


name = "Arnab Mitra"
print(name[::-1])


org_str = input("Enter a string: ")
rev_str = org_str[::-1]

if rev_str == org_str:
    print("It is a palindorme")
else:
    print("It is not a palindrome")
