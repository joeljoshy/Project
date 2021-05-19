class Parent:

    def f1(self,name,age):
        self.name = name
        self.age = age
        print("Details :",self.name,self.age)

class Child(Parent):

    def f1(self,car,bike):
        self.car = car
        self.bike = bike
        print("Vehicle :",self.car,self.bike)

ob = Child()
ob.f1('jesko','H4')