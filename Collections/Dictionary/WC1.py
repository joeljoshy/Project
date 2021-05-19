pattern = " ABCDEFGB"

dic = {}

for i in pattern:
    if i not in dic:
        dic[i] = 1
    else:
        print("First Recursive Character is ", i)
        break
