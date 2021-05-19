# def sum():
#     x = int(input("Enter num1: "))
#     y = int(input("Enter num2: "))
#     print(x+y)
#
# sum()
# sum()
#
# def pro():
#     x = int(input("Enter num1: "))
#     y = int(input("Enter num2: "))
#     print(x*y)
# pro()

# n = lambda n1,n2:n1+n2
# print(n(2,3))
#
# def dif():
#     n1=int(input("Enter num 1: "))
#     n2=int(input("Enter num 2: "))
#     diff=n1-n2
#     return diff
# data =dif()
# print(data)



def factorial(num):

        f=1
        for i in range (num,1,-1):
                f=f*i
        print("Factorial of ",num," is ",f)
num = int(input("Enter a number : "))
factorial(num)