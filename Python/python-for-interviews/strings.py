# string manipulation
s='abc'
print(s[0:2])

#they are immutable
# s[0] = 'A' not possible

#creates a new string when modified
s += 'def'
print(s)

# numeric strings can be converted to ints
print(int('123') + int('123'))

# ints can be converted to strings
print(str(123) + str(123))

# join strings
strings=['ab','cd','ef']
print(''.join(strings))
