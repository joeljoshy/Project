



class Name:
    def details(self,name,age):
        self.name = name
        self.age = age
       # print(self.name,self.age)
    def __str__(self):
        return self.name+" , "+str(self.age)



f = open("F1", "r")

for i in f:
    data = i.rstrip("\n").split(",")
    name = data[0]
    age = data[1]
    obj = Name()
    obj.details(name,age)
    print(obj)