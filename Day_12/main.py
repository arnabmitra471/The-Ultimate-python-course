# This is the main.py file for day 12

names = "Harry,Shubham,Vrinda,Arnab,Rohan"
# Finding the length of a string
print("The length of the string is",len(names))
print(names[0:5])
print(names[:5])
print(names[6:13])
print(names[6:12])

fruit = "Pineapple"
anotherFruit = "Mango"
n = len(fruit)
mangoLen = len(anotherFruit)
print(fruit,"is a",n,"character word")
print(anotherFruit,"is a",mangoLen,"character word")

# Omitting the start and end indices
print(fruit[0:4])
print(fruit[:4])
print(fruit[2:6])
print(fruit[:6])
print(fruit[2:])

# Negative slicing
print(fruit[:len(fruit)-3])
print(fruit[0:-3])
print(fruit[-3:-1])
# print(fruit[len(fruit)-1:len(fruit)-3])

# 9 - 3 = 6
# 0:6
text = "Hello World"
slice1 = text[0:5]
slice2 = text[:5]
slice3 = text[7:]
slice4 = text[:]

print("The length of",text,"is",len(text))
print(slice1)
print(slice2)
print(slice3)
print(slice4)

# Quick Quiz
nm = "Harry"
print(nm[-4:-2])
# 1:3
print(nm[::-1])