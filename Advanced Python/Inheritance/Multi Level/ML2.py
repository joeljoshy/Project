#  person child parent student
#  child and parent inherit person
#  student class inherit child

class Person:
    def per(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(self.name, self.age, self.gender)

class Parent(Person):
    def par(self, job, place, salary):
        self.job = job
        self.place = place
        self.salary = salary
        print(self.job, self.place, self.salary)

class Child(Person):
    def chi(self, school):
        self.school = school
        print(self.school)

class Student(Child):
    def std(self, rollno):
        self.rollno = rollno
        print(self.rollno)


obj1 = Parent()
obj1.per('Joel', 23, 'Male')
obj1.par('Developer', 'EKM', 50000)

obj2 = Child()
obj2.chi('KPMHSS')

obj3 = Student()
obj3.std(10)