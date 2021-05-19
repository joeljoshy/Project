# Count of proffession
f = open("A:\Luminar\Exercise\Files\customer", "r")
lst = []
dic = {}
for i in f:
    data = i.rstrip("\n").split(",")
    prof = data[4]
    lst.append(prof)
for i in lst:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)
