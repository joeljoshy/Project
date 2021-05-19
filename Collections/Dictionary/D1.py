EMPLOYEE = {'ID': "1001", "Name": 'Joel', "Designation": "Dev", "Salary": 20000}

# Print emp name

print("EMP Name : ", EMPLOYEE['Name'])

# company : name

if 'COMP' not in EMPLOYEE:
    EMPLOYEE['COMP'] = 'Google'
    print(EMPLOYEE)

# Salary + 5000
EMPLOYEE['Salary'] += 5000

#   Print

for i in EMPLOYEE:
    print(i, ":", EMPLOYEE[i])
