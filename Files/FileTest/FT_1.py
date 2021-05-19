f1 = open("File_1", "r")
f2 = open("Copy", "a")
for i in f1:
    f2.write(i)
print(f2)
