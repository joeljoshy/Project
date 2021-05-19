# lst = [1,2,3,4,5]
# ln=len(lst)
# count=1
# for i in lst:
#     res=i**count
#     count += 1
#     print(res)

lst=[1,2,3,4,5]
count=1
for i in range(0,len(lst)):
    res=lst[i]**count
    count+=1
    print(res)