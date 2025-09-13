x = 2

# multiline conditionals need to be in brackets
if (x > 2 
    and x!= 2):
    x -= 1
elif x == 2:
    x *= 5
else:
    x += 2

print(x)