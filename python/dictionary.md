---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)

***

### SEQUENCES
- are iterables that support element access using integer indices 

### Dictionaries 
- Data in a dictionary is organized into pairs of keys and values. 
- use the key to access the corresponding value (indexed by keys).

Image to remember:
In an English language dictionary the word comes with a definition.<br>
In a Python dictionary, the word would be the key and the definition would be the value. 

### Syntax
```python
	x = {key1:value1, key2:value2} 
	# a key value pair
	x = {
		key1:value1,
		key2:value2
		} 
	# for readability

	x = dict(bodystyle="truck", make="Ford", drivetrain="Four-wheel Drive")
	#no empty spaces allowed here
	y = dict('bodystyle': 'truck', 'make': 'Ford', 'drivetrain': 'Rear-wheel Drive')
	# empty spaces are ok here
	# using the dict() constructor
```

```python
### Example
f150_2018 = {
    'XLT': {
        'cabin_size': 'SuperCab',
        'bed_size': '5.5ft',
        'payload': 1800,  # in pounds
        'drive_train': '4x4',
        'engine_size': '2.7L V6'
    },
    'Lariat': {
        'cabin_size': 'SuperCrew',
        'bed_size': '6.5ft',
        'payload': 2200,  # in pounds
        'drive_train': '4x4',
        'engine_size': '5.0L V8'
    },
    'King Ranch': {
        'cabin_size': 'SuperCrew',
        'bed_size': '5.5ft',
        'payload': 1900,  # in pounds
        'drive_train': '4x2',
        'engine_size': '3.5L V6 EcoBoost'
    },
    'Platinum': {
        'cabin_size': 'SuperCrew',
        'bed_size': '6.5ft',
        'payload': 2100,  # in pounds
        'drive_train': '4x4',
        'engine_size': '3.5L V6 EcoBoost'
    }
}
```

- Dictionaries are used to organize elements into collections (like lists). 
- Dictionaries map keys to values and store them in an array or collection.
- The keys must be of a hashable type, which means that they must have a hash value that never changes during the key’s lifetime.
- For a list the index is always a number, for a dictionary key it can be a different data type:
	- strings, integers, floats, tuples, and more. 

> to test 2 liners use [IDLE](https://realpython.com/python-idle/)

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

*** 


### Tutorial 
*  [docs.python.org](http://docs.python.org/tutorial/)

### Style Guide for Python Code
* [python.org](http://www.python.org/dev/peps/pep-0008/)


#### Formatting
- single for the dict and double for formatting. 

```python
>>> comedian = {'name': 'Eric Idle', 'age': 74}
>>> f"The comedian is {comedian['name']}, aged {comedian['age']}."
The comedian is Eric Idle, aged 74.
```


```python
	x = {} 
	print(type(x))
	<class 'dict'>
```
