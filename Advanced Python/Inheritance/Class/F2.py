class Student:
    def Exam(self,name,age,degree,mark):
        self.name = name
        self.age = age
        self.degree = degree
        self.mark = mark

    def print(self):
        print(self.name,self.age,self.degree,self.mark)
    def __str__(self):

        return "Name: "+self.name+" Age : "+str(self.age)+" Degree : "+self.degree+" Mark : "+str(self.mark)



f = open("F2","r")

for i in f:
    data = i.rstrip("\n").split(",")
    name = data[0]
    age = data[1]
    degree = data[2]
    mark = data[3]
    obj = Student()
    obj.Exam(name,age,degree,mark)
    if(int(mark)>190):
        print(obj)
