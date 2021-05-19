# Student

class Student:
    school = "KPMHSS"
    def std(self, name , age, gender, ID, Class):
        self.name = name
        self.age = age
        self.gender = gender
        self.ID = ID
        self.Class = Class
    def printSt(self):
        print("\n\nStudent Details --> \n\tName:", self.name,"\n\tAge : ",self.age,"\n\tGender : ",self.gender,"\n\tID : ",self.ID,"\n\tClass : ",self.Class,"\n\tSchool : ",Student.school)


st1 = Student()
st1.std("Joel",23,"M",2211,'XII')
st1.printSt()

st2 = Student()
st2.std('Johny',23,'M',1122,'XI')
st2.printSt()
