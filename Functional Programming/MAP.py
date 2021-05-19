# Map
#  to perform same function on every objects
# lst = [2,3,4,5]
# f(x) = [4,9,16,25]

# ls = [a,b,c,d]
# l=[]

# Syntax
#--------
# map(function,itreable)

lst = [2,3,4,5,6]
# def sq(num):
#     return num**2
# s = list(map(sq,lst))
# print(s)

# using map

s = list(map(lambda num:num*num,lst))
print(s)
