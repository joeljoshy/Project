

# RULES

# [a-z] small letter

import re

# x = '[a-z]'
# matcher = re.finditer(x, "aBcDeFgabaAbc")
# for match in matcher:
#     print("Match position : ",match.start())
#     print("Match : ",match.group())


#  Capital letters [A-Z]

# x = '[A-Z]'
# matcher = re.finditer(x, "aBcDeFgabaAbc")
# for match in matcher:
#     print("Match position : ",match.start())
#     print("Match : ",match.group())


# both capital and small letters [a-zA-Z]

# x = '[a-zA-Z]'
# matcher = re.finditer(x, "aBcDeFgabaAbc")
# for match in matcher:
#     print("Match position : ", match.start())
#     print("Match : ", match.group())



# [0-9] for digits

# x = '[0-9]'
# matcher = re.finditer(x, "aB1cD3e8F0gabaAbc")
# for match in matcher:
#     print("Match position : ", match.start())
#     print("Match : ", match.group())

# for special symbols --> [^0-9a-zA-Z]

# x = '[^0-9a-zA-Z]'
# matcher = re.finditer(x, "aB@1c D3e^8F0gabaAbc")
# for match in matcher:
#     print("Match position : ", match.start())
#     print("Match : ", match.group())