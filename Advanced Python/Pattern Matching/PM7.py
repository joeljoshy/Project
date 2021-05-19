# email
import re


n = input("Enter email : ")
x = '([a-zA-Z0-9]+@[a-zA-Z]+.[a-z])'
match = re.match(x, n)
if match:
    print("Valid Mail")
else:
    print("Invalid Mail")
