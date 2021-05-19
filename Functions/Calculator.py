def calculator():
    if choice == 1:
        print(num1+num2)
    elif choice==2:
        print(num1-num2)
    elif choice==3:
        print(num1*num2)
    elif choice==4:
        print(num1/num2)
    else:
        print("Invalid choice!!!")
num1=float(input("Enter fist number : "))
num2=float(input("Enter second number : "))
choice=int(input("1,Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter your choice : "))
calculator()