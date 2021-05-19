# lst = [7,8,9,4,3,2,1]
# num > 5 - num + 1 else num - 1




# lst = [7,8,9,4,3,2,1]
# # new_list = [i+1 if i>5 else i-1 for i in lst]
# new_list=list(map(lambda i:i+1 if i>5 else i-1))
# print(new_list)



lst1=[10,20,21,22,23]
lst2=[20,21,10,22,23]

# n_list = [i for i in lst1 + lst2 if i not in lst1 or i not in lst2]
n_list = list(i for i in lst1+lst2 if i not in lst1 or i not in lst2)
print(n_list)
if not n_list:
    print("same")
else:
    print("not Same")
