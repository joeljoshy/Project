# count of letters
s = 'Joel Joshy'
print(s)
let = input("Enter the letter to count: ")
count = 0
for i in s:
    if let in i:
        count += 1
if count > 0:
    print(count)
else:
    print("Letter not found!!!")
