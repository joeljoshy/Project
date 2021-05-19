# number of class attented
# no of class held
# print %
# if allowed >75%

class_attended = int(input("Enter the number of classes attended :"))
class_held = int(input("Enter the number of classes held :"))
percentage =(class_attended/class_held)*100
print("Percentage of class attended = ",percentage,"%")
if(percentage>=75):
    print("You are allowed to sit in class.")
else:
    print("You cannot attend class.")