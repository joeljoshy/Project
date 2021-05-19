# Create a valid phone numbers file from the following file?

import re

lst = []
valid = []
invalid = []
f = open('Q7', 'r')
for i in f:
    lst.append(i.rstrip('\n'))
print(lst)

x = '[+][9][1]\d{10}'

for i in lst:
    match = re.fullmatch(x, i)
    if match:
        valid.append(i)

    else:
        invalid.append(i)
print("\nValid Numbers: ")
for i in valid:
    print(i)
print("\nInvalid Numbers :")
for i in invalid:
    print(i)
