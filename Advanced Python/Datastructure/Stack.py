size = int(input("Enter the size of stack : "))
stack = []


def push():

    if len(stack) < size:
        element1 = input("Enter the element to push:")
        stack.append(element1)
        print("Stack : ", stack)
    else:
        print("Stack is full")


def pop():
    if len(stack) <= 0:
        print("Stack is empty")

    else:
        stack.pop()
        print("Stack : ", stack)


while True:
    option = int(input("Enter the stack operation: \n 1.Push 2.POP :"))
    if option == 1:
        push()
    elif option == 2:
        pop()
