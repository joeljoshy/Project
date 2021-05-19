class Vehicle:
    def print(self,type,color,variant):
        self.type = type
        self.color = color
        self.variant = variant
        print("Your vehicle is ",self.type,", color is  ",self.color,", Variant ",self.variant)

ve = Vehicle()
ve.print('Car', 'Black', 'Sedan')