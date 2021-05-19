# python program to find second largest element from list
lst = [1,2,3,4,5,6,7,8]
largest = max(lst)
lst.remove(largest)
second_largest=max(lst)
print("Second largest element -- > ",second_largest)
