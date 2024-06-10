---
title: 07_OOP_Inheritance
layout: default
---

### What is Inheritance?

- ability to reuse exizting class members in another class
- Class being inherited from is a parent class or superclass
- Class that inherits from the parent class is a child class or subclass

### Parent Class

- can be any existing class
- becomes a perant class id a child class inherits from it
- No modification requiered 

### Child Class

- any class that declares another clas to inherit from
- Is more specific and specialized thatn its parent class
- can have its opwn members
- can use parent class members
- can modify or override a parent class members  

### Class Relationships Relationships

- Child object has multiple types
  - declared class type
  - parent class type
  - grandparent class type (if available)
- Reverse is not true - parent object is not a child class type.
  
### Is-a Relationship Examples

> screenshot

### Child Class Definition

* class keyword
* child class name
* parent class name surrounded by parenthesis
* colon
* class body
  
```python
class ChildClass(ParentClass):
    classbody
```

### Initializer Method

- child initializer should call the parent initializer
```python
class Child(Parent):
    def __init__(self):
        super().__init__()
```

- to refer to a parent class we would need to use the super function. This gives a refernce to our parent class. 
- We would then invoke the parent's initializer method and pass in any required arguments.
  
### Member Access

- a member is accessed from the child class
- If it is not available in the child class, it is searched for in the parent class

```python
class Employee:
    def hello(self):
        print('The person is already an employee.')
class Manager(Employee):
    def manage(self):
        print('Managing')
manager = Manager()
manager.manage()
# Output
Managing
```

### Member Access Example

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width * self.height) *2

class Square:
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side    
    def perimeter(self):
        return self.side * 4
```

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width * self.height) *2

class Square(Rectangle):
    # square is a specialized rectangle
    def __init__(self, side):
        super().__init__(side,side)
        self.side = side
    # area and perimeter are handled in the parent

s1 = Square(9)
print(s1.side, s1.width, s1.height)
print(s1.area(), s1.perimeter())
# Output
9 9 9 
81 36
r1 = Rectangle(10,20)
print(r1.width, r1.height)
print(r1.side)
# Output
10 20
AttributeError: Recatangle object has no attribute 'side'
# inheritance doesn't go from child to parent
```

### Class Hierarchies

- consist of many classes and their children
- shows the relationship of classes
- Top level class is called the root class
- screenshot

### Exception Hierarchy Example

- screenshot

```python
try:
    with open('doesnotexist.txt') as f:
        print(f.read())
except FileNotFoundError:
    print('.txt not found')

```

### NumPy Type Hierarchy

- screenshot

