class Pycharm:
    def compile(self):
        print("Compile using pycharm.")
    def execute(self):
        print("Execute using pycharm.")

class VS:
    def compile(self):
        print("Compile using VS.")
    def execute(self):
        print("Execute using VS.")

class Programmer:
    def code(self,code):
        code.compile()
        code.execute()


pr = Programmer()
py = Pycharm()
vs = VS()
pr.code(py)
pr.code(vs)