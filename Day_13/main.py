# This is the main.py file for day 13

# Strings are immutable
name = "!!!Arnab Mitra !!!!!!!!!!"
print("The length of the string is",len(name))
print(name)
# print(id(name))
cap_name = name.upper()
print(cap_name)
# print(id(cap_name))

lower_name = name.lower()
print(lower_name)

print(name.rstrip("!"))
print(name.lstrip("!"))
print(name.strip("!"))


friend = "Rohan Rohan"
print(friend.replace("Rohan","Harry"))

names = "Rohan,Harry,Arnab,Vrinda,Shaarav"
names_list = names.split(",")
print(names_list)

blog_heading = "introduction To Js"

print(blog_heading.capitalize())

cons = "Welcome to the console"
print(len(cons))
centered_cons = cons.center(50,"0")
print(centered_cons)
print(len(centered_cons))

str1 = "Abcacadafafacdafa"
print(str1.count("a"))

str1 = "Welcome to the console !!!"
print(str1.endswith("!!!"))
print(str1.endswith("e",1,7))
print(str1.endswith(" ",1,7))
print(str1.endswith("to",4,10))

print(str1[4:10])

str2 = "He's name is Dan. He is an honest man"
print(str2.find("is"))
print(str2.find("scjhcsjhcs"))

print(str2.find("is",15))

print(str2.index("is"))
# print(str2.index("ishh"))

alphabets = "abc123DCR567"
print(alphabets.isalnum())

name = "I am Arnab Mitra"
print(name.isalnum())

welcome_msg = "Welcome"
print(welcome_msg.isalpha())
print(welcome_msg.isalnum())

greeting = "Hello World"
print(len(greeting))
print(greeting.ljust(30,"#"))
print(greeting.rjust(30,"#"))

str3 = "hello everyone"
print(str3.islower())

str4 = "I AM A GOOD BOY !!"
print(str4.isupper())

str5 = "124433873"
print(str5.isdigit())

str6 = "7greeting"
print(str6.isidentifier())

org = "world health organisation"
print(org.istitle())

lang = "Python is an interpreted language"
print(lang.startswith("Python"))
print(lang.swapcase())

person_desc = "His name is Dan and he is an honest man"
print(person_desc.title())