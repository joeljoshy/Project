# List comprehension

# lst = []
# for i in range(1, 51):
#     lst.append(i)
# print(lst)

# Using list comprehension
# -------------------------

# lst = [i for i in range(1,51)]
# print(lst)

# Even numbers
# ls = [i for i in range(1, 51) if i % 2 == 0]
# print(ls)

# square even numbers and cube odd numbers
# lst = [i*i if i%2==0 else i*i*i for i in range (1,51)]
# print(lst)

# print even or odd
# lst = [(i, "even") if i % 2 == 0 else (i, "odd") for i in range(1, 51)]
# print(lst)

# square

# lst = [2,3,4,5,6]
# square = [num**2 for num in lst]
# print(square)

# lst = ['apple','orange','lemon']
#
# word = [(w,w,w) for w in lst]
# print(word)

# l1 = [10,20]
# l2 = [30,40] q
#
# num = [(n1,n2) for n1 in l1 for n2 in l2]
# print(num)

lst =[1,2,3,4,5,6]
num = [i for i in lst if i%2==0]
print(num)