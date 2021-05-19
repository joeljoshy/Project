# skip the repeated elements and print
a = 'joeljoshy'
b = ""
for i in a:
    if i in b:
        continue
    else:
        b += i
    print(b)
