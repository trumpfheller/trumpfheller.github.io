---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
>  [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [OOP](./oop.html) ||

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
```

- Dictionaries are used to organize elements into collections (like lists). 
- Dictionaries map keys to values and store them in an array or collection.
- The keys must be of a hashable type, which means that they must have a hash value that never changes during the key’s lifetime.
- For a list the index is always a number, for a dictionary key it can be a different data type:
	- strings, integers, floats, tuples, and more. 

> to test 2 liners use [IDLE](https://realpython.com/python-idle/)

Store the number of files corresponding to each extension.

```python
file_counts ={"jpeg":10, "txt":14, "csv":2, "py":23}
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





```python
	x = {} 
	print(type(x))
	<class 'dict'>
```
