#  print object in str
class Employee:

    def emp_details(self, name, age, company, ID):

        self.name = name
        self.age = age
        self.company = company
        self.ID = ID
        print(self.name, self.age, self.company, self.ID)

    def __str__(self):
        return self.name+" , "+str(self.ID)  # convert int to str to print


emp = Employee()
emp.emp_details('Joel', 23, 'Google', 2211)
print(emp)
