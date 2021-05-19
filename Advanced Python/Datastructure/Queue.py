size = int(input("Enter the size of queue : "))
Queue = []


def insert():

    if len(Queue) < size:
        element1 = input("Enter the element to insert:")
        Queue.append(element1)
        print("Queue : ", Queue)
    else:
        print("Queue is full!!")


def delete():
    if len(Queue) <= 0:
        print("Queue is empty!!")

    else:
        Queue.remove(Queue[0])
        print("Queue : ", Queue)


while True:
    option = int(input("Enter the Queue operation: \n 1.Insert 2.Delete :"))
    if option == 1:
        insert()
    elif option == 2:
        delete()
