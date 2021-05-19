# python program to produce star triangle
n = int(input("Enter limit:"))
space = n-1
for i in range(1,n+1):
    for j in range(0,space):
        print(end=" ")
    space -= 1
    for j in range(i,i+i):
        print("*", end=" ")

    print("")