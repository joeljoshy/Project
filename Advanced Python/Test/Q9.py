# Write a Python program to find the sequences of one upper case letter followed by lower case letters?

import re

n = input("Enter string : ")
x = '(^[A-Z]{1}[a-z])$'
match = re.fullmatch(x,n)
if match :
    print("Valid")
else:
    print("Invalid")
