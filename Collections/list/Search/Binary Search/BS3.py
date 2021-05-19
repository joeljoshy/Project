lst = [1,2,3,4,5]
element = int(input("Enter an element to search : "))
for i in lst:
   for j in lst:
      if i+j==element:
           print(i,j)
           break

      else:
             print("Element not in list!")