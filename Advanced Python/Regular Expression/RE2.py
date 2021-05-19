# with match positions

import re

count = 0
matcher = re.finditer('ab', 'ababababbbbabbabababab')
for match in matcher:
    print("Match available  at : ",match.start())  # returns match position
    print("Group : ",match.group())  # returns which is match
    count += 1
print("Count : ",count)