import re

n = input("Enter string: ")
x = '([a-zA-Z]+\d{1})$'
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")
