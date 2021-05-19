# create list with numbers 1-100 and find prime numbers to new list
lst=[]
prime=[]
flag=0
for i in range(1,101):
    lst.append(i)
for i in lst:
    if(i>1):
        for p in range(2,i):
            if i % p == 0:
               flag=1

        if flag==0:
             prime.append(i)
        flag=0
print(prime)