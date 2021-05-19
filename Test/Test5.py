# Palindrome

item = input("Enter the word/number to check : ")
re_item = item[::-1]
print(item)
if item==re_item:
    print("It is palindrome!!")
else:
    print("Its not palindrome!!")