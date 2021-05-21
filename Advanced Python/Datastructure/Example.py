num = []
alpha = []
special = []


def checkstring(string):


    for i in string:

        if (i.isdigit()):
            num.append(i)

        elif (i.isalpha()):
            alpha.append(i)

        else:
            special.append(i)

    print("Number Stack : ",num[::-1], "\nAlphabet Stack : ", alpha[::-1], "\nSpecial Character Stack :", special[::-1])



checkstring(input("Enter a string : "))
