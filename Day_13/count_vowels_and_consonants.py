str1 = input("Enter the string: ")
vowels = "aeiouAEIOU"
vowel_count = cons_count = 0

for char in str1:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            cons_count += 1
print("The number of vowels in the string is",vowel_count)
print("The number of consonants in the string is",cons_count)