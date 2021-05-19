num1 = 10
num2 = 20
print("Numbers before swapping num1 =",num1,"num2 =",num2)
# temp = num1
# num1 = num2
# num2 = temp
#------------------
num1 = num1+num2
num2= num1 - num2
num1 = num1 - num2
#(num1,num2) = (num2,num1)
print("Numbers after swapping num1 =",num1,"num2 =",num2)