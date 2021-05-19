line = "hai hai hi joel hai hello"

word = line.split(" ")
print(word)
dic = {}
for i in word:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
print(dic)
