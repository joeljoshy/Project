#   rstrip  - to remove end item
#   lstrip - to remove front item
f = open("F1", "r")
lst = []
for i in f:
    lst.append(int(i.rstrip("\n")))  # to convert str to int
print(lst)
print(sum(lst))
