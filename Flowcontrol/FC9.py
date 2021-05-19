# age gender marital status
# if female
age = int(input("enter you age:"))
sex = input("Enter your sex(M/F):")
MS = input("Enter your marital status( Y/N):")
if(sex=='F'):
    print("You can work in urban areas!!! ")
#elif((sex=='M')&(age<40)&(age>20)):
elif((sex=='M')&(20<=age<=40)):
    print("You can work anywhere!!")
elif((sex=='M')&(40<=age<=60)):
    print("You can work in urban areas only")
else:
    print("ERROR!!")