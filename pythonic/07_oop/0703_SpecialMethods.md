---
title: 07_OOP_Special Methods
layout: default
---

### What are Special Methods?

- indicated by dunders (double underscore) around the method name
- can be modified to behave differently

### Common Special Methods

| **Invocation** | **Signature** | **Description** |
|----------|----------|----------|
| Classname() | `__init__(self)` | constructor | 
| str(obj) | `__str__(self)` | string representation | 
| repr(obj) | `__repr__(self)` | printable representation | 

str(obj): invokes the dunder str method
repr(obj): whenever an object is evaluated in interactive mode, called the ripper function

### Special Methods Example

```python
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
p1 = Point(10,20)
print(str(p1))
# Output: point object at a memory location
<__main__.Point object at 0x1070322610>
```

```python
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
p1 = Point(10,20)
print(str(p1))
# Output: 
(10, 20)
```

### Arithmetic Operators

- can be overloaded

| **Invocation** | **Signature** | **Description** |
|----------|----------|----------|
| arg1 + arg2 | `__add__(self, arg)` | addition |
| arg1 - arg2 | `__sub__(self, arg)` | substraction |
| arg1 * arg2 | `__mul__(self, arg)` | multiplication |
| arg1 / arg2 | `__truediv__(self, arg)` | division |
| arg1 // arg2 | `__floordiv__(self, arg)` | integer division |
| arg1 % arg2 | `__mod__(self, arg)` | modulo |

- if we try to use these operators without overloading them, we get a type error, unsupported operator.

### Special Methods Example

- we want to create a new point our of the sum of x and y.
  
```python
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, point):
        # overloading
        return Point(self.x + point.x, 
                    self.y + point.y)
'''
we return a new object by calling the constructor
and in passing the sum of self.x and the argument point.x
'''
p1 = Point(10,20)
p2 = Point(30,15)
p3 = p1+p2
print(p3)
# Output  
(40, 35)
```

### Comparison Operators

| **Invocation** | **Signature** | **Description** |
|----------|----------|----------|
| arg1 == arg2 | `__eq__(self, arg)` | equal to |
| arg1 != arg2 | `__ne__(self, arg)` |          |
| arg1 < arg2 | `__lt__(self, arg)` |          |
| arg1 <= arg2 | `__le__(self, arg)` |          |
| arg1 > arg2 | `__gt__(self, arg)` |          |
| arg1 >= arg2 | `__ge__(self, arg)` |          |

```python
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'

p1 = Point(10,20)
p5 = Point(10,20)
print(p1==p5)
# Output  
FALSE
```

```python
class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __eq__(self, point):
        # it accepts a point as an argument
        # we compare self.x with point.x
        return self.x == point.x and
               self.y == point.y
p1 = Point(10,20)
p5 = Point(10,20)
print(p1==p5)
# Output  
# px adn py have the same properties therefore
TRUE
```

