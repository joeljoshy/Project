# starting with a and ending with b


import re

n = input("Enter string : ")
x = '(^a[\w\W]*b)$'
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")
