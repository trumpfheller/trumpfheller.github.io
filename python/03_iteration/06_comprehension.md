---
title: Python - Iteration - Comprehension
layout: default
---

## Comprehension

* Concise syntax for creating sequences or containers
* Consists of a for loop and an expression for each item
* Brackets determine the comprehension type

### Comprehension restrictions

* Limited to single line
* cannot use control structures

* brackets
* iteration
* Expression
* Conditional

### Comparison

```python
mylist = []
for item in iterable:
    mylist.appen(exp)

# and now the comprehension way

mylist = [exp for item in iterable]
```

* the expression usually contains the item variable

### List Comprehension Example

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]

print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

### List Comprehension other types

```python
numbers = [1, 2, 3, 4, 5]
# Dictionary Comprehension: Creating a dictionary of squares
squared_dict = {x: x ** 2 for x in numbers}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
# Set Comprehension: Creating a set of squares
numbers = [1, 2, 3, 4, 5, 5]  # Note: 5 is repeated
squared_set = {x ** 2 for x in numbers}
print(squared_set)  # Output: {1, 4, 9, 16, 25}
```

### Comprehension with Conditional

```python
mylist = []
for item in iterable:
    if cond_exp:
        mylist.appen(exp)

mylist = [exp for item in iterable if cond_exp]
```

### List Comprehension Example 2

```python
cities = ['Albany', 'berkeley','corte madera','Daly City']
bac = [city.upper() for city in cities]
# comprehension has the square brakets, indicate it is a list
# for city in cities: iterate through the items in the cities list
# expression: city.upper
print(bac)
```

* adding a condition: only if the city consists of more than one word
* boolean expression first splits the city by white space and converts it into a list of strings (returning a list of words): `city.split()`

```python
cities = ['Albany', 'berkeley','corte madera','Daly City']
bac = [city.upper() for city in cities if len(city.split()) > 1]
print(bac)
```
