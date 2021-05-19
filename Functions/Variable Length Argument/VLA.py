# def add(num1,num2) : #-- > parameterss
#     return num1+num2
#
# result = add(10,20)  # --> arguments
# print(result)


# For variable length of arguments
class Calculator:

    def add(self, *args):

        self.args = args
        res = 0
        for num in args:
            res += num
        print(res)

    def mul(self, *args):
        self.args = args
        pro = 1
        for num in args:
            pro *= num
        print(pro)


obj = Calculator()
obj.add(12, 3)
obj.mul(4, 5)
