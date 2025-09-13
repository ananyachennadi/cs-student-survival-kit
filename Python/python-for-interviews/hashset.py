my_set = set()

my_set.add(1)
my_set.add(2)
print(my_set)
print(len(my_set))

print(1 in my_set)
print(2 in my_set)
print(3 in my_set)

my_set.remove(2)
print(2 in my_set)

# list to set
print(set([1,2,3]))

# set comp
my_set = {i for i in range(5)}