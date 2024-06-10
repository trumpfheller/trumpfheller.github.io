---
title: lec_07 Lists Methods
layout: default
---

 ||[back](../index.html)

## String Methods

### Manipulation Methods

* change the list
* do not return a value

```python
lst.append(item)
# add item to the end of lst

mylist = [2,4,8,16]
mylist.append(32)
print(mylist)
# Output
[2,4,8,16,32]
```

### Insert Methods

```python
lst.insert(index,item)
# insert item at index in lst
mylist = [2,4,8,16]
mylist.append(0,100)
print(mylist)
# Output
[100,2,4,8,16]

```

### Clear Methods

```python
lst.clear()
# remove all the items in lst
mylist = [2,4,8,16]
mylist.clear()
print(mylist)
# Output
[]
```

### Remove Methods

```python
lst.remoce(item)
# remove item from lst, ValueError when item is not found
mylist = [2,4,8,16]
mylist.remove(8)
print(mylist)
# Output
[2,4,16]
```

### Sort Methods

```python
lst.sort(reverse=False)
# sort the items in lst, if reverse is True, sort in descending order
mylist1 = [3,2,4,-1,7]
mylist1.sort()
print(mylist1)
# Output
[-1,2,3,4,7]
mylist2 = ['c','d','a','b']
mylist2.sort(reverse=True)
print(mylist2)
# Output
['d','c','b','a']

```

### Reversed Method

```python
mylist1 = [2,4,8,16,2]
mylist.reverse()
print(mylist)
# Output
[2,16,8,4,2]

```

### Conversion Methods

* Convert a string to a list
* Convert a list to string
* conversation methods are sting methods that work with lists

### Split method

```python
string.split()
# return a list of strings seperated by one or more spaces from string

print("Monday Wednesday Friday".split())
# Output
['Monday', 'Wednesday', 'Friday']
```

### Split Method

```python
string.join(string_list)
# return a string of each item in string_list joined by a given string

months = ["Jan", "Feb", "Mar", "April"]
months_string = ",".join(months)
print(months_string)
# Output
Jan, Feb, Mar, April
```
