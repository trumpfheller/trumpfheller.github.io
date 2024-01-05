---
title: Dictionary methods
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)

> [List Methods](./listmethods.html) ||[Dictionary Methods](./dictionarymethods.html) ||

***

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
