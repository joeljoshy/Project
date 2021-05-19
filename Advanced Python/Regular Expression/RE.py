# pattern matching

# re -- package for pattern matching

import re

count = 0
matcher = re.finditer('ab', 'abbbbbababbbababa')  #  how many times ab has repeated
for match in matcher:
    count += 1

print("Count: ", count)