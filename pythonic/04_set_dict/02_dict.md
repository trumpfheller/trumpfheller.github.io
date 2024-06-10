---
title: UCB Python - lecture - Dictionary 
layout: default
---
|| [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
|| [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
|| [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)

***

What are Dictionaries?

* Container similar to sets
* items are key-Value pairs 
* Are not sequences but iterables
* also known as associative arrays or maps

### Used for

* mapping
* counting
* accumulating
* categorizing

### Dictionary items

* [key is mapped to a value]
* keys are unique, can be strings, numbers or tuples
* Values can be any type

### Dictionary Literals

* surrounded by curly braces {}
* items are key-value pairs seperated by a colon 
* Items are seperated by a comma

### Examples

* state => capital
{'California':'Sacramento', 'Texas':'Austin', 'New York':'Albany'}

* id => employee
{1:'Alex', 2:'Lin', 3:'Miranda'}

* Postal code => city
{'94720':'Berkeley', '94104':'Berkeley', '94105':'Berkeley'}

 * File Types(category => list of files)
 {'images':[flower.jpg, 'logo.png', 'python.png'],'music':['beethoven-5th.mp3', 'do-you-feel-it.flac']}

* Grades (letter grade => test scores)
 {'A':[98,95,97,92],'B':[88,82,85], 'C':[75,78]}

### Dicitonary operators

* Index
* assignment
* memebership
* delete

### Index Operator

```python
d[key]
```

return value associated with key

* if key doesn't exist, a KeyError exception is thrown

### Example

```python
d={'a':1,'b':2,'c':3,}
print(d['a'])

#Output
# 1
```

### Membership Operator

```python
key in d
```

* return Boolean on whether key exists as a key in d.

```python
d[key]=value
```

### Assignment Operator

* to put items in the dictionary, we use the assignment operator
* if key exists, update key's value to value
* if key doesn't exist, add a new key-value item

```python
d={'a':1,'b':2,'c':3,}
d['a']=100
print(d)
d['e']=5
print(d)

#Output
# {'a':100,'b':2,'c':3}
# {'a':100,'b':2,'c':3,'e':5}
```

### Delete Operator

```python
del d[key]
```

* delete item with key
* KeyError if not found
* removes an item with a specific key.

| Data Type | Content Type | Sequence | Mutable |
|:-------------|:------------------|:-------------|:------------------|
| String | characters | yes | no |
| list | anything | yes | yes |
| tuple | anything | yes | no |
| range | integers | yes | no |
| set | anything | no | yes |
| dictionary | name-value pairs | no | yes |

***
