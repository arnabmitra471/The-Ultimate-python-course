s1 = input("Enter first string: ")
s2 = input("Enter another string: ")

if len(s1) == len(s2) and len(s1) != 0:
    concatenated_str = s1 + s1
    print(concatenated_str)

    if s2 in concatenated_str:
        print("It is a rotation of the original string")
    else:
        print("It is not a rotation of the original string")