# This is the main.py file for day 11
# Creating strings with single quotes and double quotes
name = 'Arnab'
friend = "Rohan"
another_friend = "Lovish"
print("Hello",name,friend,"and",another_friend)

# Using double quotes within a string created with single quotes
apple = 'He said "I want to eat an apple"'
print(apple)

# Using single quotes within a string created with double quotes
day_desc = "It's a beautiful day"
print(day_desc)

# Using the newline escape sequence for a newline in the output
greeting = "Hello\nWorld"
print(greeting)

# Using the \t escape sequence for a horizontal tab
tabbed_greeting = "Hello\tEveryone !!"
print(tabbed_greeting)
# Multiline strings
chat = """Hey I am good
Hi Harry
How are you ??
I am also \t good
"I want to eat an apple"
"""
print(chat)

# Indexing in strings
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) # Throws an error

print("Let's use a for loop")
# Iterating through a string
for letter in apple:
    print(letter)

st_err = "This is a \
multiline string"

long_str = """This is a very long string that
    we want to break into multiple lines using a backslash
        Each line is continued with a backslash"""
print(long_str)

advice = "An apple a day keeps the doctor away"
print(advice)
# print(advice[0])
# print(advice[1])
# print(advice[2])
# print(advice[3])
# print(advice[4])
# print(advice[5])
# print(advice[6])
# print(advice[7])
# print(advice[8])
# print(advice[9])
# print(advice[10])
# print(advice[11])

for i in advice:
    print(i)

print("The length of the string is",len(advice))
# advice[0] = "P"
# advice[5] = "a"