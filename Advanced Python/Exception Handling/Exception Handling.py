a = int(input("Enter fisrt no : "))
b = int(input("Enter second no : "))

try:  # works everytime
    print(a / b)


except:  # works when exception occurs

    print("Error!!")

finally:
    print("Output")
