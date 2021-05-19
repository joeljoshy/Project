# Check the number is indian (+91)
import re

n = input("Enter mob number with country code : ")
x = '[+][9][1]\d{10}'  # Start with + , 9 , 1 and followed by 10 digits
match = re.fullmatch(x, n)
if match is not None:
    print(" Valid ")
else:
    print(" Invalid")
