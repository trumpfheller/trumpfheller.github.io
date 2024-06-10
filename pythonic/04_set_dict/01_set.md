---
title: Set
layout: default
---
> [back](./index.html)

***

### What are Sets?

* container of unique items

* Can only contain immutable items
  * numbers
  * strings
  * tuples

* like dict without values, just keys (must be unique, like in a dict)
* You can create a set from a list, string, tuple or dict, discarding any duplicate values
* use it when you want to know if something exists

> [documentation](https://docs.python.org/3/tutorial/datastructures.html#sets)

### Set have a unique property

* Although they are mutable, they follow a set condition
  * adding an item that already exists will be rejected/will not be added.
    This will maintain the set condition (all the items are unique).

* Sets are not sequences.
  * Items are **unordered**. (order of the items is not guaranteed.) Order is not significant.
  * No index operator.
  * if ordered sequences is needed, convert to a list or tuple.
  * With sets we are mostly concerned about membership.
* Sets are iterable:
  * we can use them in a for loop.
  * pass it to a len fucntion

### Set literals

* using curly braces
* items are seperated by comma
* empty set is represented by a set function
* Sets are created using curly braces {} or the `set()` constructor.

```python
set()
#function call

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
```


NOTE: it is not using curly braces to represent an empty set.
Dictionaries are also using curly braces. => an empty set is relegated to a function call.

```python
#no duplicate items
{-0.5,1,2,3,4,8,16}
{"info@berkeley.edu", "help@irs.gov", "data@wikipedia.com"}
{(10,20), (30,40), (40,30),(20,20)}
```

### Set Functions

Syntax

```python
set(container)
```

return a set with unly unique items from containter.

```python
mylist = [1,2,3,3,2,1]
myset = set(mylist)
#passing a sequence as an argument to the set function
print(myset)
# Output
# order of the set may be different on a nother machine or at another time.
{1,2,3}
```

### Set Operations

```python
set1 == set2
set1 != set2
item in set2 #membership operator
```

Compare sets

```python
set1 = {1,2,3,4,4,4,3,3}
print(set1)
# Output => all unique
{1,2,3,4}
```

```python
set1 = {1,2,3,4,4,4,3,3}
print(set1)
print(set1 == {4,1,2,3})
# compare set1 with values
{1,2,3,4}
True
```

### Set Methods

* add item to set only if the item does not already exists
* if it already exists, it does nothing

```python
set.add(item)

s1 = {'a','b','c'}
s1.add('d')
print(s1)
s1.add('a')
print(s1)
#Output
{'a','b','c','d'}
{'a','b','c','d'}
```

* remove item from set of the item does not exist, throw a KeyError exception

```python
set.remove(item)

s1 = {'a','b','c'}
s1.remove('a')
print(s1)
s1.remove('d')
print(s1)
#Output
{'c','b'}
KeyError:'d'
```

* remove all items in set

```python
set.clear()
```

### Set comprehension

Syntax

```python
myset = {exp for item in iteravle if cond_exp}
```

```python
myset{}
for item in iterable:
    if cond_exp:
        myset.add(exp)  
```

Example

```python
mylist = [n // 2 for n in range(10)]
print(mylist)
#Output
[0,0,1,1,2,2,3,3,4,4]
```

```python
mylist = [n // 2 for n in range(10)]
print(mylist)
myset = {n // 2 for n in range(10)}
print(myset)
#Output
[0,0,1,1,2,2,3,3,4,4]
{0,1,2,3,4}
```

```python
a = {x for x in 'abracadabra' if x not in 'abc'}
a
{'r', 'd'}
```

| Data Type  | Content Type  | Sequence  | Mutable  |
|---|---|---|---|
| String  | characters  | yes  | no  |
| list  | anything  | yes  | yes  |
| tubple  | anything  | yes  | no  |
| range  | integers  | yes  | no  |
| set  | immutable items  | no  | yes  |
