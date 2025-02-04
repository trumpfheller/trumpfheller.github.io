---
title: Python - Dictionary 
layout: default
---

## Dictionaries

* items are Key-Value pairs 
* are not sequences but iterables
* also known as `associative arrays` or `maps`
* Container similar to sets

### Dictionary items

* Key is mapped to a value.
* Keys are unique, can be strings, numbers or tuples.
* Values can be any type.

### Dictionary Literals

* surrounded by curly braces {}
* Items are key-value pairs seperated by a colon 
* Items are seperated by a comma

### Examples

* state => capital
{'California':'Sacramento', 'Texas':'Austin', 'New York':'Albany'}

* id => employee
{1:'Alex', 2:'Lin', 3:'Miranda'}

* Postal code => city
{'94720':'Berkeley', '94104':'Berkeley', '94105':'Berkeley'}

 * File Types(category => list of files)
fileTypes = {'images':[flower.jpg, 'logo.png', 'python.png'],'music':['beethoven-5th.mp3', 'do-you-feel-it.flac']}

* Grades (letter grade => test scores)
grades = {'A':[98,95,97,92],'B':[88,82,85], 'C':[75,78]}

### Initiate with `my_dict = {}` VS `my_dict = dict()`

* `my_dict = {}` is generally preferred for its simplicity and readability. 
* Use `my_dict = dict()` when you need to take advantage of its ability to create dictionaries from keyword arguments or other iterable inputs.

Syntax:

* `my_dict = {}` uses the **literal syntax** for dictionary creation. It's more concise and generally preferred for creating an empty dictionary.
* `my_dict = dict()` uses the **constructor** of the dict class to create an empty dictionary. This is a bit more verbose but can be useful in certain contexts.

```python
# Creating empty dictionary
my_dict = {}

# Adding key-value pairs to the dictionary
my_dict['name'] = 'Alice'
my_dict['age'] = 30
my_dict['city'] = 'New York'

# Printing the dictionary
print(my_dict)

# Accessing a value by its key
print('Name:', my_dict['name'])

# Updating a value
my_dict['age'] = 31
print('Updated age:', my_dict['age'])

# Removing a key-value pair
del my_dict['city']
print('After removing city:', my_dict)

# Iterating over the dictionary
for key, value in my_dict.items():
    print(f'{key}: {value}')

# Output
{'name': 'Alice', 'age': 30, 'city': 'New York'}
Name: Alice
Updated age: 31
After removing city: {'name': 'Alice', 'age': 31}
name: Alice
age: 31

```

```python
x = dict(name='Mike')
print(x)  # Output: {'name': 'Mike'}
```

Performance:

* `my_dict = {}`` is slightly faster because it directly creates an empty dictionary, whereas `my_dict = dict()`` involves a function call to the dict constructor. However, the difference is typically negligible for most applications.

Readability:

* `my_dict = {}` is often considered **more readable** and is **commonly used** in Python code. It's the preferred way when you need a simple, empty dictionary.
* `my_dict = dict()` when you want to emphasize that you're using the dict class, or in cases where you want to create a dictionary with keyword arguments.

Use Cases:

* `my_dict = {}` is straightforward and is the standard way to create an empty dictionary.
* `my_dict = dict()` can be useful when creating a dictionary from keyword arguments or another iterable. For example:

```python

my_dict = dict(a=1, b=2, c=3)

# This creates a dictionary 
{'a': 1, 'b': 2, 'c': 3}.
```

### Dicitonary operators

* Index
* Assignment
* Membership
* delete

### Example for Index Operator

```python
d={'a':1,'b':2,'c':3,}
print(d['a'])
# return value associated with key
# Output
# 1
print(d['x'])
# Output
# KeyError: 'x'
```

### Membership Operator

```python
key in d
```

### Example Membership Operator 

```python
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Check if 'name' is a key in the dictionary
print('name' in person)  # Output: True

# Check if 'address' is not a key in the dictionary
print('address' not in person)  # Output: True

# Check if 'Alice' is a value in the dictionary
print('Alice' in person.values())  # Output: True

# Check if 40 is not a value in the dictionary
print(40 not in person.values())  # Output: True
```

### Assignment Operator

* to put items in the dictionary, we use the assignment operator
* if key exists, update key's value to value
* if key doesn't exist, add a new key-value item

```python
d={'a':1,'b':2,'c':3,}
d['a']=100
print(d)
d['e']=5
print(d)

#Output
# {'a':100,'b':2,'c':3}
# {'a':100,'b':2,'c':3,'e':5}
```

### Delete Operator

```python
del d[key]
```

* delete item with key
* KeyError if not found
* removes an item with a specific key.

---

### Accessing elements

#1. Accessing by Key using Square Brackets (`[]`)

```python
# Creating a dictionary
student = {"name": "Alice", "age": 20, "major": "Computer Science"}

# Accessing values using keys
print(student["name"])   # Output: Alice
print(student["age"])    # Output: 20
print(student["major"])  # Output: Computer Science
print(student["grade"])  # KeyError: 'grade'
```

#2. Access using `get()` Method:

```python
# Accessing values using get() method
print(student.get("name"))    # Output: Alice
print(student.get("grade"))   # Output: None (key does not exist)
print(student.get("grade", "N/A"))  # Output: N/A (default value specified)
```

#3. Access by iterating through Keys:

```python
# Iterating through keys
for key in student:
    print(key, "->", student[key])
#Output
name -> Alice
age -> 20
major -> Computer Science
```

#4. Access by iterating Through Key-Value Pairs

```python
# Iterating through key-value pairs
for key, value in student.items():
    print(key, "->", value)
```

#5. Accessing Keys and Values Separately:

```python
# Accessing keys
keys = student.keys()
print(keys)   # Output: dict_keys(['name', 'age', 'major'])

# Accessing values
values = student.values()
print(values)  # Output: dict_values(['Alice', 20, 'Computer Science'])
```

---

* dict Example used in `mapping`

```python
# Define a dictionary mapping product IDs to names and prices
products = {
    1: {"name": "Laptop", "price": 1200.00},
    2: {"name": "Mouse", "price": 25.00},
    3: {"name": "Keyboard", "price": 50.00},
    4: {"name": "Monitor", "price": 300.00}
}

# Function to retrieve product information
def get_product_info(product_id):
    if product_id in products:
        return products[product_id]
    else:
        return None

# Example usage:
product_id = 2
product_info = get_product_info(product_id)

if product_info:
    print(f"Product ID {product_id} is a {product_info['name']} priced at ${product_info['price']}")
else:
    print(f"Product with ID {product_id} not found.")
```

*  dict Example used in `counting`

```python
# Example list
data = [1, 2, 3, 2, 1, 3, 2, 1, 1, 2, 3, 1, 2, 3]

# Initialize an empty dictionary to count occurrences
count_dict = {}

# Count occurrences of each element in the list
for item in data:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

# Print the resulting dictionary with counts
print("Count of each element:")
for key, value in count_dict.items():
    print(f"{key}: {value}")
```
Counting Process:
* We iterate through each element (`item`) in the  `data` list.
* If the `item` already exists as a `key in count_dict`, we increment its count (`count_dict[item] += 1`).
* If the `item` is encountered for the first time, we initialize its count to 1 (`count_dict[item] = 1`).

*  dict Example used in `accumulating`

```python
# Sample data: a list of items
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# Create an empty dictionary to accumulate counts
item_counts = {}

# Iterate over each item in the list
for item in items:
    # If the item is already in the dictionary, increment its count
    if item in item_counts:
        item_counts[item] += 1
    # If the item is not in the dictionary, add it with a count of 1
    else:
        item_counts[item] = 1

# Print the accumulated counts
print(item_counts)
# OUTPUT
{'apple': 3, 'banana': 2, 'orange': 1}

```

*  dict Example used in categorizing 

```python
# Sample data: a list of fruits with their types
fruits = [
    ('orange', 'citrus'),
    ('lemon', 'citrus'),
    ('strawberry', 'berry'),
    ('blueberry', 'berry'),
    ('banana', 'tropical'),
    ('mango', 'tropical')
]

# Create an empty dictionary to categorize fruits
fruit_categories = {}

# Iterate over each fruit in the list
for fruit, category in fruits:
    # If the category is already in the dictionary, append the fruit to the list
    if category in fruit_categories:
        fruit_categories[category].append(fruit)
    # If the category is not in the dictionary, add it with a list containing the fruit
    else:
        fruit_categories[category] = [fruit]

# Print the categorized fruits
print(fruit_categories)

# Output
{
    'citrus': ['orange', 'lemon'],
    'berry': ['strawberry', 'blueberry'],
    'tropical': ['banana', 'mango']
}

```

***

| Data Type | Content Type | Sequence | Mutable |
|:-------------|:------------------|:-------------|:------------------|
| String | characters | yes | no |
| list | anything | yes | yes |
| tuple | anything | yes | no |
| range | integers | yes | no |
| set | anything | no | yes |
| dictionary | name-value pairs | no | yes |

***
