s1 = input("Enter a string: ")

# A string of vovels maintained for checking
vowels = "AEIOUaeiou"
result = "" # The resultant string obtained after removing vowels

for char in s1:
    if char not in vowels:
        result = result + char

print(result)