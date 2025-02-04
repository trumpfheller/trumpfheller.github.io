---
title: Python - Dictionary method
layout: default
---

## Dictionary method

* length function
* content methods
* manipulation methods
* get methods

### `len` function

```python
# len(dict)

my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_length = len(my_dict)
print("Length of dictionary:", dict_length)  # Output: 3
```

* you could also create a length function

```python
def custom_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

# Example usage:
my_list = [1, 2, 3, 4, 5]
print("Length of list:", custom_length(my_list))  # Output: 5
```

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
