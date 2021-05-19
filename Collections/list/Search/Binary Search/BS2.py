lst = [1,2,5,4,8,6,7,3,9,10]
lst.sort()

low = 0
upper = len(lst)-1
flag = 0
element = int(input("Enter an element to search : "))
while low <= upper :
    mid = (low + upper) // 2
    if element > lst[mid]:
        low = mid+1
    elif element < lst[mid]:
        upper = mid-1
    elif element == lst[mid]:
        flag = 1
        break

print(lst)
if flag > 0:
    print("Element found!!")
else:
    print("Element not found!")
