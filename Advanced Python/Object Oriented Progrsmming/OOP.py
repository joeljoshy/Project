# class - design pattern
# object - real world entities
# references - name that refers the memory location of an object


# class class_name:
#     def function_name(self):


class Person:
    def people(self, name, age,  gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("Hello", self.name, self.age, self.gender)


#  object

pe = Person()
pe.people("joel", 23, "M")
re = Person()
re.people('Johny', 22, "M")
