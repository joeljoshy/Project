salary = float(input("Enter your salary:"))
service = float(input("Enter the total years of service:"))
bonus = float((5/100)*salary)
if(service>=5):
    print("your net bonus amount is ",salary+bonus)
else:
    print("Bonus not applicable!!")