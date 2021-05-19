num = int(input("Enter a number:"))
m=0
f=0
while(num!=0):
    m=num%10
    f=num//10
    num=f
    print(m,end="")