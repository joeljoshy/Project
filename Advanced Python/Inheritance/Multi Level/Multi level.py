#  Multilevel / hierarchical inheritance

class Parent:
    def m1(self):
        print("Inside parent")

class Child(Parent):

    def m2(self):
        print("Inside child class")

class Subchild(Child):
    def m3(self):
        print("Inside subchild")


obj1 = Subchild()
obj1.m1()
obj1.m2()
obj1.m3()

obj2 = Child()
obj2.m1()
obj2.m2()