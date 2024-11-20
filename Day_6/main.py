import cmath as cm
# This is the main.py file for day 6

num = 123453456366
print(num)

friend_name = "Rajeswari Di"
print("My friend's name is",friend_name)

first_name = 'Arnab'
print(first_name)

a = 12
b = True
c = "Anamika Di"
d = None
e = False
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))

print(a + b)
# print(a + c)
"""
a = "I am "
b = 20
print(a + b)
"""
e = 1.23
print(e,type(e))

z1 = complex(8,-2)
z2 = complex(56,35)
print(z1)
print(z2)

arg_z1 = cm.phase(z1)
print(arg_z1)

arg_z2 = cm.phase(z2)
print(arg_z2)

pol_z1 = cm.polar(z1)
pol_z2 = cm.polar(z2)

print(pol_z1)
print(pol_z2)

print(cm.rect(8.246211251235321,-0.24497866312686414))
sin_z2 = cm.sin(z2)
print(sin_z2)

greeting = "Good Morning Everyone"
print(greeting)
print("The type of",greeting,"is",type(greeting))

l1 = [23,56,12,87.5,43,189,"Arnab","Vrinda","Anamika",["apple","banana","pear"]]
print(l1)
print(type(l1))

t1 = (23,56,12,87.5,43,189,"Arnab","Vrinda","Anamika",("apple","banana","pear"))
print(t1)
print(type(t1))

details = {
    "name" : "Sakshi",
    "age" : 20,
    "can vote" : True
}
print(details)
print(type(details))
