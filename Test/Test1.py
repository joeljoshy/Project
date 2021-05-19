# Python program to remove duplicate elements in list

lst = [1,2,3,4,4,5,6,6,6,7,8,9,9,9,9,10]
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(" Original list --> ",lst)
print(" List after removing duplicate elements -->",new_lst)