# Inheritance using constructor

class Parent:
    def __init__(self, name, age, gendr):

        self.name = name
        self.age = age
        self.gender = gendr

    def print(self):
        print("Name : ", self.name, "Age : ", self.age, "Gender : ", self.gender)

class Child(Parent):
    def __init__(self, place, name, age, gender):
        super().__init__(name, age, gender)
        self.place = place

    def print_C(self):
        print("Place : ", self.place)
        print("Age : ", self.age)

obj = Child("EKM", 'Joel', 23, "Male")
obj.print()
obj.print_C()