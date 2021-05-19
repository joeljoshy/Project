class Calculator:

    def num(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

class Operation(Calculator):
    def add(self):
        print("Sum =",self.num1+self.num2)
    def diff(self):
        print("Difference =",self.num1-self.num2)
    def pro(self):
        print("Product =",self.num1*self.num2)
    def quo(self):
        print("Quodient =",self.num1/self.num2)


s = Operation()
s.num(10,5 )
s.add()
s.diff()
s.pro()
s.quo()