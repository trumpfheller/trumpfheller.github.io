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

 
example. 




```python
	x = {} 
	print(type(x))
	<class 'dict'>
```
