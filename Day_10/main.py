# This is the main.py file for day 10
'''
name = input("Enter your name: ")
print("My name is",name)
'''


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
res = int(num1) + int(num2)
res_str = str(num1) + str(num2)
res2 = int(num1) - int(num2)

prod_res_str = int(num1) * int(num2)
prod_res_int = int(num1) * int(num2)
print("The sum of the numbers is",res)
print("The resultant string after concatenation is",res_str)
print("The difference of",num1,"and",num2, "is",res2)
print("The arthmetic product of",num1,"and",num2,"is",prod_res_int)


num3 = int(input("Enter first number:  "))
num4 = int(input("Enter second number: "))
result = num3 * num4
print("The product of",num3,"and",num4,"is",result)

greeting = "hello everyone"
repeat_count = 4
print(greeting * repeat_count)
# print(greeting ** repeat_count)

num1 = 10
num2 = 4
rem = num1 % num2
print("The remainder when",num1,"is divided by",num2,"is",rem)
