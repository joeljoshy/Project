# repeated item from file
import re

f = open('R1', 'r')
count = 0
for i in f:
    matcher = re.finditer('bb',i)
    for i in matcher:
        count +=1

print(count)