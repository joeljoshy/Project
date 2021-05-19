# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # even = list(filter(lambda ev: ev % 2 == 0, lst))
# # print(even)
#
# # num>5
#
# num = list(filter(lambda n:n>=5,lst))
# print(num)
#
#

employee = [
    {"eid": 1000,"name": "ajay", "salary": 25000,"designation": "developer"},
    {"eid": 1001, "name": "vjay", "salary": 22000, "designation": "developer"},
    {"eid": 1002, "name": "arun", "salary": 26000, "designation": "qa"},
    {"eid": 1003, "name": "varun", "salary": 27000, "designation": "ba"},
    {"eid": 1004, "name": "ram", "salary": 20000, "designation": "mrkt"}]


name = list(map(lambda em:em['name'],list(filter(lambda emp:emp["designation"] == 'developer', employee))))
print(name)

# for i in emp_dev:
#     for k, v in i.items():
#         print(k, ":", v)
#     print()
