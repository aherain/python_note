
a = [1, 2, 3]

for i in a:
    print(i)
    if i == 3:
        break

else:
    print("ninin")


a = a or {}

a = a if a else {}

first, *new, last = [94, 85, 73, 46]
print(new)
a = {}
a[(1,3)] = 100

dd= []

dd.append({'nihgao': 'vvv',
           'val': a[(1,3)]})

a[(1,3)] = 100-10

print('dddddd',dd, a[(1,3)])
