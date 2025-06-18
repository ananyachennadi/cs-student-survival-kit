# 📦 Useful Python Libraries

# How to install Libraries in Python

```python
import math                     # Whole library
from math import sqrt           # Specific function
import numpy as np              # Alias
```

💡 *Install external libraries using* `pip install packagename` *in the terminal.*

# Useful Libraries

## File & Folder Tools

### `os` – File & Folder Operations

```python
import os
os.mkdir("test_folder")  # Create a folder
```

### `shutil` - Copy & Move Files

```python
import shutil

shutil.copy("file.txt", "backup/file.txt")  # Copy file
```

### `csv` – Read & Write CSV Files

```python
import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])    # Write header
    writer.writerow(["Ananya", 95])       # Write data row
```

## Date & Time

### `datetime` – Work with Dates and Times

```python
from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Format current time
```

### `time` – Sleep, Delay, and Timers

```python
import time

print("Start")
time.sleep(2)        # Wait for 2 seconds
print("End")
```

## Math & Randomness

### `math` – Math Functions

```python
import math

print(math.sqrt(25))     # Square root
print(math.ceil(3.14))   # Round up
print(math.pi)           # Pi constant
```

### `random` – Generate Random Values

```python
import random

print(random.randint(1, 10))            # Random number 1–10
print(random.choice(["A", "B", "C"]))   # Random item from list
```

## Data Formats

### `json` – Handle JSON Data

```python
import json

data = {"name": "Ananya", "age": 20}
json_string = json.dumps(data)       # Convert dict to JSON string
print(json_string)
```

### `requests` – Make HTTP API Calls

```python
import requests

response = requests.get("https://api.example.com/books")
data = response.json()

print(data["title"])
```

💡 *You have to first install the requests library in the terminal using:*

```bash
pip install requests
```

## Command-Line Tools

### `argparse` – Command-Line Arguments (CLI)

> `argparse` is a built-in Python library that lets you add command-line arguments to your scripts.
> 

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name")   # add --name as a CLI option
args = parser.parse_args()

print(f"Hello, {args.name}!")
```

*Run this in terminal:*

```bash
python script.py --name Ananya
```

*Output:*

```
Hello, Ananya!
```

### `sys` – System Info & Exit

```python
import sys

print(sys.argv)     # List of command-line arguments
sys.exit()          # Exit the program early
```
