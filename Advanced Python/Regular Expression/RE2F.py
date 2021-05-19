# with match positions from file

import re

f = open('R1', 'r')
count = 0
for i in f:
    matcher = re.finditer('ab', i)
    for match in matcher:
        print("Match available  at : ",match.start())
        print("Group : ",match.group())
        count += 1
print("Count : ",count)