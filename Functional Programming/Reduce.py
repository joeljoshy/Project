import functools
lst = [1,3,3,4,5]
#print sum

# total = functools.reduce(lambda n1,n2:n1+n2,lst)
# print(total)

# Highest number

high = functools.reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(high)