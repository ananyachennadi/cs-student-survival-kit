myMap = {}
myMap['alice'] = 88
myMap['bob'] = 77
print(myMap)
print(len(myMap))

myMap['alice'] = 80

print('alice' in myMap)
myMap.pop('alice')
print('alice' in myMap)

myMap = {'alice':90, 'bob':70}

# dict comprehension
myMap = {i:2*i for i in range(3)}
print(myMap)

# looping through dicts
myMap = {'alice':90, 'bob':70}
for key in myMap:
    print(key, myMap[key])

for val in myMap.values():
    print(val)

for key,val in myMap.items():
    print(key, val)