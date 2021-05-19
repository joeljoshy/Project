#  Multiple inheritance

class Student:
    def s_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_s(self):
        print(self.name, self.age, self.gender)

class ID:
    def id(self, ID_no):
        self.ID_no = ID_no

    def print(self):
        print(self.ID_no)

class STD(Student, ID):

    def std(self,Class):
        self.Class = Class

    def print_std(self):
        print(self.Class)

obj = STD()
obj.s_details('Joel',22,"Male")
obj.id(2211)
obj.std('XII')
obj.print_s()
obj.print()
obj.print_std()