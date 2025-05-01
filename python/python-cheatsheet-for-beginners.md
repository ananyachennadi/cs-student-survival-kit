# Python Syntax Cheatsheet for Students / Beginners 🐍

> A curated Python syntax reference for beginners and interview prep. Clear, example-driven, and focused on the essentials you’ll actually use.
> 

# Basic Syntax (Essential for Beginners)

### Printing

```python
print("hello, world")

name = input("Whats your name? ")  # asks for user input
print("Hello,", name)  # prints with a space in between hello, and name
print("Hello, " + name)
print(f"Hello, {name}")  # most common way
```

<aside>
💡

**Tip:** *To run this, save the file as `hello.py`, then run in terminal:*

</aside>

```bash
python hello.py
```

### Comments

```python
# This is a single-line comment

"""
This is a
multi-line comment
"""
```

# Variables & Data Types

```python
x = 5              # int
y = 3.14           # float
name = "Alice"     # string
is_ready = True    # boolean
```

## Type Conversion

```python
int("5")       # 5
str(3.14)      # "3.14"
float("10")    # 10.0
```

```python
# Prompt user for x
x = int(input("x: "))

# Prompt user for y
y = int(input("y: "))

# Perform addition
print(x + y)
```

# Operators

```python
5 + 2    # 7
5 - 2    # 3
5 * 2    # 10
5 / 2    # 2.5
5 // 2   # 2
5 % 2    # 1
2 ** 3   # 8
5 == 5   # True
5 != 3   # True
5 > 2    # True
True and False   # False
True or False    # True
not True         # False
```

# Data Structures

### Lists

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
fruits.append("orange")
```

```python
# Get scores
scores = []
for i in range(3):
    score = int(input("Score: "))
    scores.append(score)

# Print average
average = sum(scores) / len(scores)
print(f"Average: {average}")
```

<aside>
💡

**Tip:** *A list in Python is essentially a dynamic array.* 

</aside>

### Tuples

```python
coords = (10, 20)
```

<aside>
💡

**Tip:** *Tuples cannot be modified — no changing, appending, or deleting elements.*

</aside>

### Dictionaries

```python
people = [
    {"name": "Yuliia", "number": "+1-617-495-1000"},
    {"name": "David", "number": "+1-617-495-1000"},
    {"name": "John", "number": "+1-949-468-2750"},
]

# Search for name
name = input("Name: ")
for person in people:
    if person["name"] == name:
        print(f"Found {person['number']}")
        break
else:
    print("Not found")
```

*We can simplify this code as follows:*

```python
people = {
    "Yuliia": "+1-617-495-1000",
    "David": "+1-617-495-1000",
    "John": "+1-949-468-2750",
}

# Search for name
name = input("Name: ")
if name in people:
    print(f"Number: {people[name]}")
else:
    print("Not found")
```

<aside>
💡

**Tip:** *A dictionary in Python is essentially a hash map.* 

</aside>

# Control Flow

```python
age = 18
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

e.g.

```python
s = input("Do you agree? ")

# Check whether agreed
if s == "Y" or s == "y":
    print("Agreed.")
elif s == "N" or s == "n":
    print("Not agreed.")
```

Another approach to this same code is to use *lists*:

```python
s = input("Do you agree? ")

# Check whether agreed
if s in ["y", "yes"]:
    print("Agreed.")
elif s in ["n", "no"]:
    print("Not agreed.")
```

# Loops

### For Loop

```python
for i in range(5):  #iterates 5 times (0-4)
    print(i)
```

### While Loop

```python
n = 0
while n < 3:
    print(n)
    n += 1
```

### Loop Control

```python
for i in range(5):
    if i == 3:
        break  # exit loop
    if i == 1:
        continue  # skip iteration
```

# Functions

<aside>
✅

**Best Practice:** In Python, when you define your own functions, it's common practice to create a `main()` function to organise your program's logic. Then, you call this `main()` function at the end of your script:

</aside>

```python
def main():
    meow(3)

# Meow some number of times
def meow(n):
    for i in range(n):
        print("meow")

main()
```

# Error Handling

```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Can run")
```

<aside>
🔍

*Common exceptions:*

- `TypeError`
- `ValueError`
- `IndexError`
- `KeyError`
</aside>

# List Comprehensions (Great for interviews!)

List comprehensions offer a concise, readable way to create new lists by processing or filtering items. 

### Flatten nested lists

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = []
for row in matrix:
	for num in row:
		flattened.append(num)
"""
Read it as:
for each row in matrix, and for each num in that row, include num in the new list.
"""
```

### Create a list of all numbers from 1 to 20 that are divisible by 3

```python
div_by_3 = [x for x in range(1, 21) if x % 3 == 0]
print(div_by_3)  # Output: [3, 6, 9, 12, 15, 18]
```

### Convert a list of strings to uppercase using a list comprehension:

```python
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']
```

### From a list of words, create a list of only those with more than 4 characters:

```python
words = ["hi", "hello", "cat", "elephant", "sun"]
long_words = [word for word in words if len(word) > 4]
print(long_words)  # Output: ['hello', 'elephant']
```

### Generate a list of tuples where each tuple contains a number and its square for numbers 0–5:

```python
squares = [(x, x**2) for x in range(6)]
print(squares)  # Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```