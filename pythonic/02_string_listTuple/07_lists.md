---
title: lec_07 Lists
layout: default
---

 ||[back](../index.html)

## Lists

* Containers of items stored in a sequence
* are mutable - items can be changed
* have all sequence operators, functions and methods

|   | Sequence  | Mutable  |
|---|---|---|
|  List | YES  | YES  |
|  tuple | YES  | NO  |
|  String | YES  | NO  |
|  Range | YES  | NO  |
|  Set | NO | YES  |
| Dict  |  NO | YES  |

 a list of dictionaries 
 ```python
 # Creating a list of dictionaries
list_of_dicts = [
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Alice", "age": 25, "city": "Los Angeles"},
    {"name": "Bob", "age": 35, "city": "Chicago"}
]

# Accessing elements in the list of dictionaries
print(list_of_dicts[0]["name"])  # Output: John
print(list_of_dicts[1]["age"])   # Output: 25
print(list_of_dicts[2]["city"])  # Output: Chicago
```

 a dictionary of lists?
```python
# Creating a dictionary of lists
dict_of_lists = {
    "fruits": ["apple", "banana", "orange"],
    "colors": ["red", "yellow", "orange"],
    "numbers": [1, 2, 3, 4, 5]
}

# Accessing elements in the dictionary of lists
print(dict_of_lists["fruits"])   # Output: ['apple', 'banana', 'orange']
print(dict_of_lists["colors"][0])  # Output: red
print(dict_of_lists["numbers"][2])  # Output: 3
```

### Lists Literals

* a list literal is a way to directly create a list by specifying its elements within square brackets [].
* when you want to initialize a list with a known set of elements. 

```python
my_list = [1, 2, 3, 4, 5]
```

```python
scores = [82,79, 95, 88, 82, 93]
emails = ['info@berkeley.edu','facts@wikipedia.com', 'support@irs.com']
colors = ["red", "green", "blue", "yellow"]
```

```python
[]
[,]
```

### Lists Functions

```python
list(container)
# return a list from a given container
```

### Inherited Lists Operators

```python
| lst[index] | index operator
| lst[start:stop] | slice index operator
| lst1==lst2 | equality operator
| lst1!=lst2 | inequality operator
| item in lst | membership operator
| lst1+lst2 | append operator

```

### Assignment

```python
lst[index]=value
# set value at index in lst
```

### Delete

```python
del lst[index]
# delete an item in lst at index
# deltes an item at a specified index in a list

del lst[start:stop]
# delete a slice from start to stop
```

### Examples

```python
todo = ['homework', 'groceries']
todo = todo+'exercise'
# Typeerror: can only concatenate list (not str) to list
todo = todo+['exercise']
todo
['homework', 'groceries', 'exercise']
todo[-2:]
['groceries', 'exercise']
todo[1]='haircut'
todo
['homework', 'haircut', 'exercise']
```
