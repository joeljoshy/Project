# Create an example for three types of inheritance in one program by using Person as main class

class Person:  # parent class

        def details(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender

        def print(self):
            print(self.name, self.age, self.gender)

class Student(Person):  # child class

        def det(self, r_no, school):
            self.r_no = r_no
            self.school = school

        def print_s(self):
            print(self.r_no, self.school)


class Parent(Student,Person):
        def parent(self,p_name):
            self.p_name = p_name
            print("Parent name: ",self.p_name)


class Child(Student):
        def child(self,c_name):
            self.c_name = c_name
            print("Child name : ",self.c_name)



#  Sinlge
obj = Student()
obj.details('Johny', 23, 'Male')
obj.det(10, 'LMPS')
obj.print()
obj.print_s()

#  Multiple

ob = Parent()
ob.details('Joel',23,'Male')
ob.det(20,'KPM')
ob.parent('Joel')
ob.print()
ob.print_s()

# Multi-level
ob1 = Child()
ob1.details('Jo',23,'M')
ob1.print()
ob1.det(22,'LL')
ob1.print_s()
ob1.child('Anjo')

ob2 = Student()
ob2.details('joe',22,'M')
ob2.print()


