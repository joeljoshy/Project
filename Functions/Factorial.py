def factorial():
    f = 1
    for i in range(num, 1, -1):
        f *= i
    print("Factorial of ", num, " is ", f)


num = int(input("Enter a number : "))
factorial()
