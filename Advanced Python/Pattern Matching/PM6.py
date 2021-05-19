#kerala vehicle registration number validation
# KL39E5862\


import re

n = input("Enter Vehicle No : ")
x = '(^KL+\d{2}\w{1,2}\d{4})$'
match = re.fullmatch(x,n)
if match is not None:
    print("Kerala Registered.")
else:
    print("Invalid No!!!")