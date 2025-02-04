---
title: Python - Tuples
layout: default
---

## Tuples

* Immutable sequence
* Like lists but cannot be modified
* Inherit all the sequence operators, functions and methods

| Type | Sequence  | Mutable  |
|---|---|---|
| tuple | YES  | NO  |
| String | YES  | NO  |
| Range | YES  | NO  |
| List | YES  | YES  |
| Set | NO | YES  |
| Dict  |  NO | YES  |

### you need tuples when you have to deal with

* Dates
* Coordinates
* Birthdays
* Logging information
* Grouping data (person's name, place of birth)

### Tuple Advantages

* Speed
* Security
* Compact code
* Keys in a dictionary

### Tuple Literals

```python
()
(,)
```

### Single item Tuple

```python
(item,)
# single item requires a comma
(item) == item
# distinguishes a tuple from a single item
```

### Tuple Function

```python
tuple(container)
# return a tuple from a given container
# returns a tuple version of it
```

### Tuple Assignment

* set multiple variables in one statement
  * `var0, var1, var2, = value0,value1,value2, `
* Variables are on the left of the assignment
* correspond with values on the right

### Tuple Assignment Example

```python
t = (1,20,300)
a,b,c = t

# Output
1
20
300
```

### Tuple Conversion

* Automatically converts items separated by commas into a tuple
  * var0, var1, var2, = value0,value1,value2, ..
* Tuple items are indexed
  * var0 = value0

### Example membership operators

```python
# Sample tuple
numbers = (1, 2, 3, 4, 5)

# Check if 3 is in the tuple
print(3 in numbers)  # Output: True

# Check if 10 is not in the tuple
print(10 not in numbers)  # Output: True
```

---

 ||[back](../index.html)
