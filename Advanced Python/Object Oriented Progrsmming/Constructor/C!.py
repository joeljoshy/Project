#  Constructor

#  its used to initialise instance variable
# Constructor automatically invoke when objects created

class Person:
    def __init__(self, name, age,  gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print(self):
        print(self.name, self.age, self.gender)


pe = Person('Johny', 23, 'M')
pe.print()
