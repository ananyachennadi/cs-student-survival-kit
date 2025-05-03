# Python Cheatsheet: File I/O 🐍

> File I/O means reading from or writing to files. In Python, you can use the `open()` function to read data from a file, write data to it, or add more content. This is useful when you want to save information or get input from files instead of typing everything in.
> 

# `.txt` — Plain Text Files

### Opening and Closing a `.txt` file

**Syntax**:

```python
file_object = open(filename, mode, encoding="utf-8")
```

**Common Modes:**

- `'r'` for reading (default)
- `'w'` for writing (truncates the file)
- `'a'` for appending
- `'r+'` for both reading and writing

<aside>
✅

**Best Practice:** Use a `with` block to open a file because it automatically handles closing the file

</aside>

```python
with open("data.txt", "r") as f:
    content = f.read()
# file is automatically closed here
```

### **Reading from a `.txt` file:**

**`read()`** : Reads the entire file as a single string.

```python
with open("example.txt", "r") as file:
    contents = file.read()
    print(contents)
```

**`readline()`**: Reads one line at a time.

```python
with open("data.txt", "r") as f:
    # Read the first line
    line = f.readline()

    while line:
        # Print each line without adding an extra newline (since lines already end with \n)
        print(line, end="")  
        # Read the next line
        line = f.readline()
```

### **Writing to a `.txt` file:**

**`write()`**: Overwrites the file

```python
with open("example.txt", "w") as file:
    file.write("Hello, this is a line.\n")
```

**`write()`**: Adds to the file

```python
with open("output.txt", "a") as f:  # Notice we are using a instead of w
    f.write("Appending this line.\n")
```

### Additional Tips & Best Practices

<aside>
⚠️

**Always close files.**

Use context managers (`with`) to automatically handle closure.

</aside>

<aside>
⚠️

**Be careful with write mode.**

`'w'` will overwrite an existing file — use `'a'` for appending if needed.

</aside>

# `.csv` — Comma-Separated Values

### Reading a `.csv` file

```python
import csv

with open("data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)  # Each row is a list of values
```

Without `newline=””`:

```python
Name,Age

Alice,22

Bob,25
```

With `newline=""` (correct way):

```python
Name,Age
Alice,22
Bob,25
```

### Writing a `.csv` file

```python
import csv

# use tuples if the data is meant to be unchangeable
data = [['Name', 'Age'], ['Alice', 22], ['Bob', 25]]

with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)  # Writes multiple rows
```

### Using `DictReader`

- The **keys** are taken from the header row.
- The **values** are from each row of data.

`data.csv` file:

```python
Name,Age
Alice,22
Bob,25
```

Using `DictReader`:

```python
import csv

with open('data.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

Output:

```python
{'Name': 'Alice', 'Age': '22'}
{'Name': 'Bob', 'Age': '25'}
```

### Using `DictWriter`

- You define the **field names** (column headers).
- Then you write dictionaries with matching keys as rows.

Using `DictWriter`:

```python
import csv

with open('output.csv', 'w', newline='') as f:
    fieldnames = ['Name', 'Age']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # fieldnames=fieldnames tells the writes what the keys are
		# f is the file object opened for writing
		
    writer.writeheader()  # Writes: Name,Age
    writer.writerow({'Name': 'Alice', 'Age': 22})
    writer.writerow({'Name': 'Bob', 'Age': 25})
```

This writes:

```python
Name,Age
Alice,22
Bob,25
```

# `.json` — JavaScript Object Notation

### Reading a `.json` file

```python
import json

with open('data.json') as json_file:
    data = json.load(json_file)  # Parses JSON into Python dict/list
    print(data)
```

### Writing a `.json` file

```python
import json

data = {"name": "Alice", "age": 22}

with open('output.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)  # indent for pretty print
```

### Parsing JSON Strings

```python
import json

json_str = '{"name": "Alice", "age": 22}'
data = json.loads(json_str)
print(data)
```

### Converting to JSON String

```python
import json

data = {'name': 'Bob', 'age': 25}
json_str = json.dumps(data)
print(json_str)
```