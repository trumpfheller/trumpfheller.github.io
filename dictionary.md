---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
>  [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [OOP](./oop.html) ||

***

### SEQUENCES
- are iterables that support element access using integer indices 

### Dictionaries 

### Syntax
 ```python
	x = {key1:value1, key2:value2} 
	# a key value pair
```
- use the key to access the corresponding value (indexed by keys).
- but data in a dictionary isn't accessed based on its position. 
- Data in a dictionary is organized into pairs of keys and values. To get a dictionary value we use its corresponding key.
- Dictionaries are used to organize elements into collections (like lists). 
- Dictionaries map keys to values and store them in an array or collection.
- The keys must be of a hashable type, which means that they must have a hash value that never changes during the key’s lifetime.
- different data types as keys are available:
	- strings, integers, floats, tuples, and more. (in a list the index must be a number)

In an English language dictionary the word comes with a definition.
In a Python dictionary, the word would be the key and the definition would be the value.




```python
	x = {} 
	print(type(x))
	<class 'dict'>
```
