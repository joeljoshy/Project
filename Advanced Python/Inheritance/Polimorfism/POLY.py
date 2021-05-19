# Same method name and different parameter
# method over ride
class Parent:

    def prop(self):
        print("1 B$")

    def car(self):
        print("Agera")


class Child(Parent):
    def car(self):
        print("Jesko")


ob = Child()
ob.car()