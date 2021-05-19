# Multiple Inheritance

class Parent:
    def m1(self):
        print("inside parent")

class Child:
    def m2(self):
        print("inside child class")


class SubChild(Child,Parent):
    def m3(self):
        print("inside sub child")


obj = SubChild()
obj.m1()
obj.m2()
obj.m3()