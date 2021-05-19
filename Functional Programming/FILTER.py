# Filter
#-------

# Syntax
#-------

# filter(function,iterable)

lst = [1,2,3,4,5,6]
# def even(num):
#     return num%2==0
# ev = list(filter(even,lst))
# print(ev)

# using map
ev = list(filter(lambda num: num % 2 == 0, lst))
print(ev)
