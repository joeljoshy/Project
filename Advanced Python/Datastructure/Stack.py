size = int(input("Enter the size of stack : "))
stack = []


def push():

    if len(stack) < size:
        element = input("Enter the element to push:")
        stack.append(element)
        print("Stack : ", stack[::-1])
    else:
        print("Stack is full")


def pop():
    if len(stack) <= 0:
        print("Stack is empty")

    else:
        stack.pop()
        print("Stack : ", stack[::-1])


while True:
    option = int(input("Enter the stack operation: \n 1.Push 2.POP :"))
    if option == 1:
        push()
    elif option == 2:
        pop()
