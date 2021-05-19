# num
# for loop 2 - (num-1)
#
# num%2==0
#     not prime
num = int(input("Enter a number : "))
flag=0
for i in range(2, num):
    if(num%i==0):
        flag=1
if(flag==1):
    print("not prime")
else:
    print("prime")