arr = [1,2,3]
print(arr)

# initialise with fixed size
arr=[0]*3

# can be used as a stack
arr.append(4)
print(arr)

arr.pop()
print(arr)

arr.insert(1, 7)
print(arr)

arr[0] = 0
print(arr)

# splicing
arr = [1,2,3,4]

print(arr[1:3]) # [2, 3]
print(arr[0:4]) 
print(arr[-3:-1]) # [2, 3]

# unpacking
a, b, c = [1,2,3]
print(a, b, c)

# looping through arrays
nums = [1,2,3]

# with index
for i in range(len(nums)):
    print(nums[i])

# without index
for n in nums:
    print(n)

# with index and value
for i,n in enumerate(nums):
    print(i,n)

# looping through multiple arrays simultaneously with unpacking
nums1=[1,3,5]
nums2=[2,4,6]
for a, b in zip(nums1, nums2):
    print(a,b)

# reverse an array
nums = [1,2,3]
nums.reverse()
print(nums)

# sort an array in ascending order
arr = [5,4,7,3,8]
arr.sort()
print(arr)

#sort in reverse
arr.sort(reverse=True)
print(arr)

#sort in alphabetical order
arr=['bob','alice','jane','doe']
arr.sort()
print(arr)

#custom sort (length of string)
arr.sort(key=lambda x: len(x))
print(arr)