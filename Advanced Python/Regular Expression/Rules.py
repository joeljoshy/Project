# rules without []

import re


# to chech space --> \s

# x = '\s'
# matcher = re.finditer(x, "aB@1c D3e^8F0gaba Abc")
# for match in matcher:
#     print("Match position : ", match.start())
#     print("Match : ", match.group())

# \d for digits

# x = '\d'
# matcher = re.finditer(x, "aB@1c D3e^8F0gabaAbc")
# for match in matcher:
#     print("Match position : ", match.start())
#     print("Match : ", match.group())



#Except digits

# x = '\D'
# matcher = re.finditer(x, "aB@1c D3e^8F0gabaAbc")
# for match in matcher:
#     print("Match position : ", match.start())
#     print("Match : ", match.group())


# all words except special characters
# x = '\w'
# matcher = re.finditer(x, "aB@1c D3e^8F0gabaAbc")
# for match in matcher:
#     print("Match position : ", match.start())
#     print("Match : ", match.group())

# for special characters

x = '\W'
matcher = re.finditer(x, "aB@1c D3e^8F0gabaAbc")
for match in matcher:
    print("Match position : ", match.start())
    print("Match : ", match.group())