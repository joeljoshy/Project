def check_age(age):
    age = int(input("Enter age :"))
    if age>=18:
        print("Eligible for vaccination.")
    else:
    # print("Not applicable.")
         raise Exception('not applicable')  # Exception class


# Try
try :
    check_age(17)
except Exception as e:
    print(e.args)