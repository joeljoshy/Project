#  Dictionary

# Denoted by
#     dic = {}

# Values stored in dictionary by key:value pairs
dic = {'name': 'joel', 'Age': 23, 'Height': 6.1, 'Loc': 'EKM'}
print(dic)

# Supports heterogeneous data


# Insertion order is preserved


# Duplicate keys not supported
# It supports duplicate values


# Value can be collected from dictionary using its corresponding key
#   --------------------------------------------------------------------
#   print(dic["name"])
#   print(dic["Loc"])

# for i in dic:
#     print(i, ":", dic[i])

# It is mutable
#   ---------------
#   dic['Age']=22
# dic['Age']-=1
# print(dic)


# REMOVING ELEMENTS
#   --------------------
# del dic['Height']
# print(dic)

# dic.pop('Loc')
# print(dic)

# check key present in dictionary or not
# print("age" in dic)
dic['Gender'] = 'M'
print(dic)