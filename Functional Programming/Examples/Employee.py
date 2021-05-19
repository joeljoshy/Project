employee = [
    {"eid": 1000,"name": "ajay", "salary": 25000,"designation": "developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"}]


emp_names = list(map(lambda emp:emp["name"],employee))
for i in emp_names:
    print(i)