class Vehicle:
    def car(self, company, color):
        self.company = company
        self.color = color
        print("Car details : ", self.company, self.color)

    def bike(self):
        print()


ve = Vehicle()
ve.car('BMW', ", Black")
#ve.bike()
