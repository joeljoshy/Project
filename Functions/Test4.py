# remove special characters

string="H,el;l,o W::or?ld"
s_char=",<.>/?;:"
n_string=""
# for i in string:
#     if i in s_char:
#         continue
#     else:
#         n_string+=i

for i in string:
    if i not in s_char:
        n_string+=i
print(n_string)