---
title: Python OOP_Special Methods
layout: default
---

## _Special__ Methods

- are indicated by dunders (double underscore) around the method name
- can be modified to behave differently

### Common Special Methods

| **Invocation** | **Signature** | **Description** |
|----------|----------|----------|
| Classname() | `__init__(self)` | constructor | 
| str(obj) | `__str__(self)` | string representation | 
| repr(obj) | `__repr__(self)` | printable representation | 

`str(obj)`: invokes the dunder str method
`repr(obj)`: whenever an object is evaluated in interactive mode, called the ripper function

---

### `__init__` Methods Example

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

### `__str__()` Methods Example

Purpose: 
* to provide a "user-friendly" or informal string representation of an object.
Usage: 
* when you use str(obj) or print(obj).
* or creating output intended for end users, where readability and clarity are important.

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

### `__repr__()` Methods Example

Purpose: 
* to provide an "official" or formal string representation of an object that ideally could be used to recreate the object using `eval()`.
Usage: 
* when you use `repr(obj)` or when the interpreter needs a string representation of the object, such as in debugging.
*  used more for debugging and development, where the focus is on obtaining detailed information about the object.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def __repr__(self):
        return f'Car(make={self.make}, model={self.model}, year={self.year})'

# Creating a list of 10 cars
cars = [
    Car("Toyota", "Camry", 2020),
    Car("Honda", "Accord", 2018),
    Car("Ford", "Mustang", 2022),
    Car("Chevrolet", "Malibu", 2019),
    Car("BMW", "X5", 2021),
    Car("Audi", "A4", 2017),
    Car("Mercedes-Benz", "C-Class", 2023),
    Car("Lexus", "RX", 2016),
    Car("Tesla", "Model S", 2024),
    Car("Subaru", "Outback", 2015)
]

# Printing each car in the list
for index, car in enumerate(cars):
    print(f"Car {index + 1}: {car}")

'''
OUTPUT
Car 1: Car(make=Toyota, model=Camry, year=2020)
Car 2: Car(make=Honda, model=Accord, year=2018)
Car 3: Car(make=Ford, model=Mustang, year=2022)
Car 4: Car(make=Chevrolet, model=Malibu, year=2019)
Car 5: Car(make=BMW, model=X5, year=2021)
Car 6: Car(make=Audi, model=A4, year=2017)
Car 7: Car(make=Mercedes-Benz, model=C-Class, year=2023)
Car 8: Car(make=Lexus, model=RX, year=2016)
Car 9: Car(make=Tesla, model=Model S, year=2024)
Car 10: Car(make=Subaru, model=Outback, year=2015)
'''
```

* When you call `str(obj)` or `repr(obj)` directly, Python internally looks for these special methods (`__str__()` or `__repr__()`) to generate the appropriate string representation based on your implementation.

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

