# This is the main.py file for day 22

marks = [3,5,6,"Arnab","Rohan","Shaarav","Vrinda",True,False,True]
# print(marks)
# print(type(marks))

# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])
# print(marks[6])

for i in marks:
    print(i)

colors = ["Red","Green","Blue","Yellow","Violet","Brown"]
print(colors)

colors[1] = "Magenta"
print(colors)
print(len(colors))
# Negative indexing
print(colors[-3])
print(colors[-5])
print(colors[1])
if "Rohan" in marks:
    print("Yes it is present")
else:
    print("No")

# Same thing applies for strings as well
if "ary" in "Harry":
    print("Yes")

# List slicing
l2 = [34,76,22,97,12,87,22,65]
print(l2[2:5])
print(l2[2:4])

print(l2[1:])
print(l2[:])
print(marks[1:-1])
print(marks[1:9])


fruits = ["Banana","apple","pear","pineapple","Guava"]
element = input("Enter an element in the list: ")
# print(element)

if element in fruits:
    print(element,"is there in the basket")
else:
    print("You need to buy it")

if "6" in marks:
    print("6 is present in the list")

else:
    print("6 is not present in the list")

# List comprehension

lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)

names = ["Milo","Sarah","Bruno","Anastasia","Rosa"]
names_with_o = [item for item in names if "o" in item]
print(names_with_o)

names_with_o = [name for name in names if len(name) > 4]
print(names_with_o)