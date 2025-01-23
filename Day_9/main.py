# This is the main.py file for day 9

# Explicit typecasting
num1 = "25"
num2 = "36"
print(type(num1))
print(type(num2))
print(int(num1) + int(num2))

string = "15"
number = 7
string_num = int(string)
total = number + string_num

print("The sum of both the numbers is",total)

# Implicit typecasting
c = 1.9
print(type(c))
d = 8
print(type(d))
res = c + d

print(res)
print(type(res))
