class Student:
    def s_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_s(self):
        print(self.name, self.age, self.gender)

class ID(Student):
    def id(self, ID_no):
        self.ID_no = ID_no

    def print_i(self):
        print(self.ID_no)

class STD(ID):

    def std(self,Class):
        self.Class = Class

    def print_std(self):
        print(self.Class)


obj1 = STD()
obj1.s_details('Joel',22,"Male")
obj1.id(2211)
obj1.std('XII')
obj1.print_s(),obj1.print_i(),obj1.print_std()
print()

obj2 = ID()
obj2.s_details("Johny",23,"Male")
obj2.id(2112)
obj2.print_s(),obj2.print_i()