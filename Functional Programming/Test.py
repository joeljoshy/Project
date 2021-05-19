# cube = lambda num:num**3
# print(cube(3))

# ch = lambda word:word[1:1]
# print(ch("Joel"))

lst = ['joel','john']
# l = [1,2,3,4,5]
#
# s = list(map(lambda i:i**2,l))
# print(s)

upp= list(map(lambda i:i.upper(),lst))
print(upp)

l = list(filter(lambda i:i[-1]=='l',lst))
print(l)