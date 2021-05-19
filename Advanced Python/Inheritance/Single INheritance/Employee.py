#  Single inheritance
class Employee:
    company = "Luminar"

    def emp(self, name, age):
        self.name = name
        self.age = age

    def print_e(self):
        print(self.name,self.age, Employee.company)


class Person(Employee):
    def per(self, ID, salary):
        self.ID = ID
        self.salary = salary

    def print_p(self):
        print(self.ID, self.salary,Employee.company)



em = Employee()
em.emp('Joel', 23)
em.print_e()

per = Person()
per.per(2211,20000),per.emp('Johny', 23)

per.print_p(),per.print_e()


# per.emp('Johny', 23)
# per.print_e()