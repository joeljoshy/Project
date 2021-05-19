f = open("F2", "r")
word = f.read()
w = word.rstrip("\n").split(" ")
dic = {}
for i in w:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)
# Key value pair

for k,v in dic.items():
    print(k,",",v)