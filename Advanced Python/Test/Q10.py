# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b

import re

n = input("Enter string : ")
x = '(^a[\w\W]*b)$'
match = re.fullmatch(x,n)
if match :
    print("Valid")
else:
    print("Invalid")
