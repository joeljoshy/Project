# return except [abc]

# [^abc]

import re

x = '[^abc]'  # check either a,b,c
matcher = re.finditer(x, "abcdefgabaabc")
for match in matcher:
    print("Match position : ",match.start())
    print("Match : ",match.group())
