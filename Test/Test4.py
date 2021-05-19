# Fibonacci series

limit = int(input("Enter the limit : "))
n1=0
n2=1
sum=0
for i in range (0,limit):
    sum=n1+n2
    n1=n2
    n2=sum
    print(sum,end=" ")