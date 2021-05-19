# count vowels
string = input("Enter a string : ")
#print(string)
vow = 'aeiou'
count=0
for i in string:
    if i in vow:
        count += 1
if count > 0:
    print(count)
else:
    print("Vowel not found!!")
