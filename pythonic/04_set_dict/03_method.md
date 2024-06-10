---
title: UCB Python - lecture - Dictionary method
layout: default
---
|| [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
|| [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
|| [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)

---

* length function
* content methods
* manipulation methods
* get methods

### length function

```python
len(dict)
```

* return the number of items the dict contains

### content methods

* Access dictionary items, keys or values
* these methods return a view object
  * Dynamic view of a dictionar's items (when the dict changes it will be reflected inthe view)
  * there are containers and iterable so we can use them in for loops

```python
dict.keys()
# returns a view object of keys
dict.values()
# returns a view object of values
dict.items()
# returns a view object of items
```

### Examples

```python
d={'a':1,'b':2,'c':3,}
print(d.keys())
print(d.values())
print(d.items())
# Output
# dict_keys(['a','b','c'])
# dict_values([1,2,3])
# dict_items(['a',1),('b', 2),('c', 3)])
# notice each item is a tuple containing key nd value
```


### manipulation methods

```python
dict.clear()
# removes all items in dict

dict.update(dict2)
# merge dict2 with dict, dup-keys overwritten by dict2
d={'a':1,'b':2,'c':3}
d2={'e':5,'f':6,'c':100}
# Output
# {'a':1,'b':2,'c':100, 'e':5,'f':6}

dict.copy()
# returns a copy of a dict
d={'a':1,'b':2,'c':3}
d2=d.copy()
d2['a']=100
print(d2)
print(d)
# Output
# {'a':100,'b':2,'c':3}
# {'a':1,'b':2,'c':3}
```

### get methods

```python
dict.get(key, default=None)
print(d.get('b'))
print(d.get('d'))
# return the value of key in dict, retrieves the value given the key
# if key doesn't exist, it will return a None vlaue by default
# if key doesn't exist return default instead => can be changed to a different value
# Output
# 2
# None
```

| Intent        |  Method         |
|:-------------|:------------------|
| create |
| convert |
| Add/change |
| get |
| combine |
| delete |
| test |
| assign |
| copy |
| compare |
| iterate |
| comprehension |