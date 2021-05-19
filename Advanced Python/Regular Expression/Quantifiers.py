import re

# x = 'a+' # a including group
# r = "aaa abc aa acaac"
# matcher = re.finditer(x, r)
# for match in matcher:
#     print("Match position : ", match.start())
#     print("Match : ", match.group())



# count including zero number of a

x = 'a*' # a including group
r = "aaa abc aa acaac"
matcher = re.finditer(x, r)
for match in matcher:
    print("Match position : ", match.start())
    print("Match : ", match.group())