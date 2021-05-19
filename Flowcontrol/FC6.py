# 4 subjects , total marks, 188-200 A+, 168-179 A, 148 -169 B+,

sub1 = int(input("Enter mark of subject1 (out of 50):"))
sub2 = int(input("Enter mark of subject2 (out of 50):"))
sub3 = int(input("Enter mark of subject3 (out of 50):"))
sub4 = int(input("Enter mark of subject4 (out of 50):"))
total = sub1+sub2+sub3+sub4
print("Total mark :",total)
if(total<=200)&(total>=180):
    print("Grade is A+")
elif(total<=179)&(total>=160):
    print("Grade is A")
elif(total<=159)&(total>=140):
    print("Grade is B+")
elif(total<=139)&(total>=120):
    print("Grade is B")
elif(total<=119)&(total>=100):
    print("Grade is C+")
elif(total<=99)&(total>=80):
    print("Grade is C")
elif(total<=79)&(total>=60):
    print("Grade is D+")
else:
    print("FAIL")