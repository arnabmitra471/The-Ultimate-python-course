s1 = input("Enter a string: ")

result = ""

for char in s1:
    if char not in result:
        result += char

print("The resultant string after removing duplicates is",result)
