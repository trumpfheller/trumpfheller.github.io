---
title: Dictionary methods
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)

> [List Methods](./listmethods.html) ||[Dictionary Methods](./dictionarymethods.html) ||

***

| Operations        |  what it does          | 
|:-------------|:------------------|
| len(dictionary)           | Returns the number of items in the dictionary | 
| for key in dictionary | Iterates over each key in the dictionary   | 
| for key, value in dictionary.items() | Iterates over each key,value pair in the dictionary | 
| if key in dictionary           | Checks whether the key is in the dictionary | 
| dictionary[key] | Accesses the item with key key of the dictionary | 
| dictionary[key] = value | Sets the value associated with key | 
| del dictionary[key] | Removes the item with key key from the dictionary | 


| Methods        | what it does         |
|:-------------|:------------------|
| dict.get(key, default) | Returns the element corresponding to key, or default if it's not present |
| dict.keys() | Returns a sequence containing the keys in the dictionary   | 
| dict.values() | Returns a sequence containing the values in the dictionary  | 
| dict.update(other_dictionary) | Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added. | 
| dict.clear()           | Removes all the items of the dictionary | 

[documentation for dictionary operations and methods](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

### Iterating Through .keys() method

Need to go through this one more time!!!

```python
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
keys = a_dict.keys()
keys
dict_keys(['color', 'fruit', 'pet'])
```

```python
for key in a_dict.keys():
    print(key)
#OUTPUT
color
fruit
pet
```

```python
for key in a_dict.keys():
    print(key, '->', a_dict[key])
#OUTPUT
color -> blue
fruit -> apple
pet -> dog
```

values() and .keys() return view objects just like .items(),


### Iterating through .values() method

```python
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
values = a_dict.values()
values
dict_values(['blue', 'apple', 'dog'])
```

```python
for value in a_dict.values():
    print(value)
# OUTPUT
blue
apple
dog
```

Store the number of files corresponding to each extension.

```python
file_counts ={
	"jpeg":10,
	"txt":14,
	"csv":2,
	"py":23
	}
print(file_counts)
{'jpeg': 10, 'txt': 14, 'csv': 2, 'py': 23}
```

Find out how many text files there are in the dictionary. use the key txt to access its associated value. 
```python
file_counts = {"jpeg": 10, "txt": 14, "csv": 2, "py": 23}
file_counts["txt"]
#OUTPUT 
14
```

To check if a key is contained in a dictionary using the **in** keyword. <br>
It will return True if the key is found in the dictionary; otherwise it will return False.
```python
file_counts = {"txt": 14, "csv": 2, "py": 23}
"jpeg" in file_counts
True
"html" in file_counts 
False
```


Dictionaries are mutable, (can be modified by adding, removing, and replacing elements in a dictionary, similar to lists). 

#### add entry
- Dictionaries are mutable (can add remove and replace entries). 
- To add an entry in a dictionary, just use the square brackets to create the key and assign a new value to it. 

```python
file_counts = {'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8} 
file_counts["cfg"] = 8 
print(file_counts)
# OUTPUT
{'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8} 
```

#### **modify** the value of an existing key  
- keys inside of a dictionary are unique. 
- When you use a key that already exists to set a value, the value that was already paired with that key is replaced. 

```python
file_counts["csv"] = 17
print(file_counts)
# Before
{'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}
# After
{'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}
```

#### delete entry
- delete elements from a dictionary with the del keyword by passing the dictionary and the key to the element as if we were trying to access it. 
```python
file_counts ={'jpeg': 10, 'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}
del file_counts["cfg"]
print(file_counts)
file_counts ={'jpeg': 10, 'txt': 14, 'csv': 17, 'py': 23}
```


### Iterating over the Contents of a Dictionary

```python
file_counts ={'jpeg': 10, 'txt': 14, 'csv': 17, 'py': 23}
for key in file_counts: 
	print(key)
#OUPUT
jpg
txt
csv
py
```

#### to get access to the values

```python
>>> for key in a_dict:
...     print(key, '->', file_counts[key])
	# indexing operator []
jpeg -> 10
txt -> 14
csv -> 17
py -> 23
```

### Iterating Through .items() method 
- returns a new view of the dictionary’s items:

```python
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
d_items = a_dict.items()
d_items  # Here d_items is a view of items
dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])
```
- d_items provides a dynamic view on the dictionary’s entries => when the dictionary changes, the views reflect these changes.
alternative using the **view object** returned by .items():

```python
for item in a_dict.items():
...     print(item)
...
('color', 'blue')
('fruit', 'apple')
('pet', 'dog')
```

```python
for item in a_dict.items():
	print(type(item))
#OUTPUT
('color', 'blue')
<class 'tuple'>
('fruit', 'apple')
<class 'tuple'>
('pet', 'dog')
<class 'tuple'>
```

Now you can do tuple unpacking to iterate through the keys and values.

```python
for key, value in a_dict.items():
...     print(key, '->', value)
...
color -> blue
fruit -> apple
pet -> dog
# now more readable and Pythonic.
```

values() and .keys() return view objects just like .items(),

### Iterating Through .keys() method

```python
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
>>> keys = a_dict.keys()
>>> keys
dict_keys(['color', 'fruit', 'pet'])
```
```python
for key in a_dict.keys():
...     print(key)
...
color
fruit
pet
```
```python
for key in a_dict.keys():
...     print(key, '->', a_dict[key])
...
color -> blue
fruit -> apple
pet -> dog
```

### Iterating Through .values() method

```python
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
values = a_dict.values()
values
dict_values(['blue', 'apple', 'dog'])
```
```python
for value in a_dict.values():
...     print(value)
...
blue
apple
dog
```

### a dictionary in a for loop, 
- the iteration variable will go through the keys in the dictionary.
- to access the associated values,
	- use the keys as indexes of the dictionary 
	or 
	- use the items method which returns a tuple for each element in the dictionary. 
		- The tuple's first element is the key. 
		- Its second element is the value. 

```python
file_counts ={'jpeg': 10, 'txt': 14, 'csv': 2, 'py': 23}
for ext, amount in file_counts.items(): 
  print("there are {} files with the .{} extension".format(amount, ext)) 

#OUTPUT
> there are 10 files with the .jpgextension
> there are 14 files with the .txtextension
> there are 2 files with the .csvextension
> there are 23 files with the .pyextension
```

To access the keys of a dictionary or the values with their corresponding dictionary methods
 
```python
print(file_counts.keys())
dict_keys(['jpg', 'txt', 'csv', 'py'])

print(file_counts.values())
dict_values([10, 14, 2, 23])
```
These methods return special data types related to the dictionary. => just iterate them as you would with any sequence.
```python 
for value in file_counts.values(): 
   print(value)
10
14
2
23
```
* use items to get key value pairs, file_counts.items()
* keys to get the keys, and file_counts.keys()
* values to get the values. file_counts.values()

*** 
