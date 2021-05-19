# current year
# current month
# current day
# dob
# print age

c_year = int(input("Enter current year : "))
c_month = int(input("Enter current month : "))
c_day = int(input("Enter current day : "))

print("Current Date : ", c_day, "/", c_month, "/", c_year)

yob = int(input("Enter your year of birth : "))
mob = int(input("Enter your month of birth : "))
dob = int(input("Enter your day of birth : "))

print("Date of Birth :", dob, "/", mob, "/", yob)

# print age
y_diff = int(c_year-yob)
m_diff = int(c_month-mob)
d_diff = int(c_day-dob)
if y_diff > 1:
    if c_month >= mob & c_day >= dob:
        print("Your are ", y_diff, "years old!!")
    elif c_month >= mob & c_day < dob:
        print("Your are ", y_diff-1, "years old")
    elif c_month < mob:
        print("You are ", y_diff-1, "years old!!")
elif y_diff == 1:
    if c_month >= mob & c_day >= dob:
        print("You are ", y_diff, "year old!!")
    elif c_month >= mob & c_day < dob:
        print("Your are ", 12-m_diff-1, " months old!!")
    elif c_month < mob:  # & c_day < dob:
        print("You are ", 12-m_diff-1, "months old!!")
elif y_diff == 0:
    if c_month == mob:
        print("You are ", d_diff, "day(s) old")
    else:
        print("You are ", m_diff, "months(s) old")
