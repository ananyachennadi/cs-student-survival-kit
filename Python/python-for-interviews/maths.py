import math

# 2.5
print(5/2)

# integer division uses //
# 2
print(5//2)

# languages round towards 0 so negative numbers round down
# -2
print(-3 // 2)

# workaround for rounding towards 0 is to 
# use decimal divison and then convert to int
print(int(-3 / 2))

# modulus
# 1
print(9%2)

# math library 
print(math.floor(3/2)) # 1 rounds down
print(math.ceil(3/2)) # 2 rounds up
print(math.sqrt(2)) # gets square root
print(math.pow(2, 3)) # 2^3 powers

# you can use these for max/min int
float('inf')
float('-inf')