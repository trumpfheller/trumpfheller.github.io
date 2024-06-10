---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)
||[Dictionary Methods](./dictionarymethods.html) ||
***

### SEQUENCES
- are iterables that support element access using integer indices 

### Dictionaries 
- Data in a dictionary is organized into pairs of keys and values. 
- use the key to access the corresponding value (indexed by keys).
- Keys have to be unique always.

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
	x = {} 
	print(type(x))
	<class 'dict'>
```

### Example

```python
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


*** 


### Tutorial 
*  [docs.python.org](http://docs.python.org/tutorial/)

### Style Guide for Python Code
* [python.org](http://www.python.org/dev/peps/pep-0008/)

> to test 2 liners use [IDLE](https://realpython.com/python-idle/)


