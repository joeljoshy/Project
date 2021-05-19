#  Customer
f = open("A:\Luminar\Exercise\Files\customer","r")
# for i in f:
#     data = i.rstrip("\n").split(",")
#     print(data)
#     country = data[-1]
#     f_name = data[1]
#
#     age = data[3]
#     if country == 'india':
#         print(f_name, ",", age, ",", country)
# age > 50

for i in f:
    data = i.rstrip("\n").split(",")
    id = data[0]
    country = data[-1]
    f_name = data[1]
    age = int(data[3])
    l_name = data[2]
    prof = data[4]
    lst = [id,f_name, l_name, prof, age, country]
    # if age > 50:
    #     print(lst)

# prof == doctor

    if prof == 'Doctor':
        print(lst)