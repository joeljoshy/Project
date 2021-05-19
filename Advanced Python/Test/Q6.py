# Create objects of the following file and print the details of student with maximum mark?

class Student:
    def Exam(self,name,rno,degree,mark):
        self.name = name
        self.rno = rno
        self.degree = degree
        self.mark = mark

    def print(self):
        print(self.name,self.rno,self.degree,self.mark)
    def __str__(self):

        return "Name: "+self.name+" Rno : "+str(self.rno)+" Degree : "+self.degree+" Mark : "+str(self.mark)


f = open("Q5","r")

for i in f:
    data = i.rstrip("\n").split(",")
    name = data[0]
    rno = data[1]
    degree = data[2]
    mark = data[3]
    obj = Student()
    obj.Exam(name,rno,degree,mark)
    if(int(mark)==200):
         print(obj)

