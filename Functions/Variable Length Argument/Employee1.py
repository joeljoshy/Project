employee = {
    1000: {"eid": 1000,"name": "ajay", "salary": 25000,"designation": "developer"},
    1001: {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    1002: {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    1003: {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    1004: {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"}

}

# name of id
def print_employee(**kwargs):
    id = kwargs['id']
    prop =  kwargs['prop']

    if id in employee:
        print(employee[id]['name'])
        print(employee[id]['salary'])
    else:
        print("Invalid ID !!")

num =int( input("Entr id : "))
print_employee(id=num,prop='salary')

# prop = salary