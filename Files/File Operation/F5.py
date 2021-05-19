# Temperature
f = open("A:\Luminar\Exercise\Files\Temperature", "r")
#print(f.read())
lst = []
dic = {}
for i in f:
    data = i.rstrip("\n").split(" ")
    year = data[0]
    tem = int(data[1])
    if year not in dic:

        dic[year] = data[1]
    else:
        if int(dic[year]) < tem:
            dic[year] = tem
print(dic)
for i in dic:
    print(i,":",dic[i])