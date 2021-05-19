#  single inheritance

class Person:  # parent class / base class / super class

    def details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print(self):
        print(self.name, self.age, self.gender)


class Student(Person):  # child class / sub class / derived class

    def det(self, r_no, school):
        self.r_no = r_no
        self.school = school

    def print_s(self):
        print(self.r_no, self.school)


per = Person()
per.details('Joel', 23, "M")
per.print()

st = Student()
st.det(10, 'LMPS')
st.print_s()

st.details('Johny', 23, 'M')
st.print()
