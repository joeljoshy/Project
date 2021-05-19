class Employee:
    company = "Luminar"
    def emp(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

    def print(self):
        print(self.name,self.age,self.id,self.salary,Employee.company)

em = Employee()
em.emp('Joel',23,2211,20000,)
em.print()