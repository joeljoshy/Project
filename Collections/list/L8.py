# create list 1-100 and sort even and odd to separate list

lst = []
even = []
odd = []
for i in range(1, 101):
    lst.append(i)
for j in lst:
    if j % 2 == 0:
        even.append(j)
    else:
        odd.append(j)
print("Even list -->", even)
print("Odd list  -->", odd)
