# min 8 max 15 .except numbers


import re

n = input("Enter string : ")
x = '\D{8,15}'
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")