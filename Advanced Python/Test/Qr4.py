# Create an Animal class using constructor and build a child class for Dog

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print(self):
        print("Name :",self.name,"\nAge : ",self.age)

class Dog(Animal):
    def __init__(self,breed,color,name,age):
        super().__init__(name,age)

        self.breed = breed
        self.color = color

    def print_d(self):
        print("Dog Breed :",self.breed, "\nColor :",self.color)


obj = Dog('Lab','Black','Max',2)
obj.print()
obj.print_d()