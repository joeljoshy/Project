# Create a child class Bus that will inherit all of the variables and methods of Vehicle class

class Vehicle:


    def vehicle(self, v_colour, v_seats, v_company ):

        self.v_colour = v_colour
        self.v_seats = v_seats
        self.v_company = v_company


class Bus(Vehicle):

    def bus(self):
        print("Bus colour :",self.v_colour, "Seat capacity :", self.v_seats, "Bus Company Name :", self.v_company)


obj = Bus()
obj.vehicle('Red', 40, 'Volvo')
obj.bus()

