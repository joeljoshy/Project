lst = [[1001, 'Joel', 25, 1000], [1002, 'johny', 26, 2000], [1003, 'Ann', 27, 3000], [1004, 'Maria', 28, 4000]]
# for i in lst:
#     for j in i:
#         print(j, end=" ")
#     print()


# print name

# for i in lst:
#     print(i[1])

# names of salary above 2000

# for i in lst:
#     if i[3] > 2000:
#         print(i[1])

# sum of salary
sum = 0
for i in lst:
    sum += i[3]
print(sum)
