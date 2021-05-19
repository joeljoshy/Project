
class Calculator:

    def cal(self, num1, num2):

        self.num1 = num1
        self.num2 = num2
        print("Numbers are ", self.num1, ",", self.num2)

    def sum(self):
        print("Sum = ", self.num1+self.num2)

    def diff(self):
        print("Difference = ", self.num1-self.num2)

    def pro(self):
        print("Product = ", self.num1*self.num2)

    def div(self):
        print("Quotient = ", self.num1/self.num2)



obj = Calculator()
obj.cal(10, 2)
obj.sum()
obj.pro()
obj.diff()
obj.div()
