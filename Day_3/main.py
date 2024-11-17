# This is the main.py file for day 3

import pandas as pd

df = pd.read_excel("birthday_buddies.xlsx")
print(df)
print(df["Name"])
print(df["Birthday"])
print(type(df["Name"]))
print(type(df["Birthday"]))

l1 = (16,54,87,87,98,12,165,876,210)
index = ("a","b","c","d","e","f","g","h","i")
s = pd.Series(l1,index=index)
print(s)
print(type(s))