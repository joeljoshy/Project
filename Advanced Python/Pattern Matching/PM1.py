import re

n = input("Enter mobile number : ")
x = '\d{10}'
match = re.fullmatch(x,n)
if match is not None:
    print("Valid")
else:
    print("Invalid")
