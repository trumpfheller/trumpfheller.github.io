---
title: 07_OOP_CreatingObjects
layout: default
---

Objective
* Learn what objects and instances are.
* Learn how to create and use objects.


### Creating Objects (Instances)

* a class provides a template for an object
* instantiation
  * creating an instance of a class
  * create an object from a class
* each object has their own properties (instance variables)


### Create objects using Constructors

* The constructor has the name of the class
  * allocates space in memory
  * initialized object's instance variables

Syntax

```python
class ClassName:
    def __init__(self, parameter1, parameter2, ...):
        # Initialize instance variables
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        # Add more initialization as needed

# Creating an object of the class
object_name = ClassName(value1, value2, ...)
```

### Example 1

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating an object of the class Person
person1 = Person("Alice", 30)
print(person1.name)  # Output: Alice
print(person1.age)   # Output: 30
```

### Example Rectangle Constructor

create a rectangle object with width and height

```python
# Instantiation Example

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
# he will explain the class defintion later
# this is just the instantiation

r1 = Rectangle(200,100)
```

when we call the rectangle constructor with a width of 200 and 100 it will instantiate and return a rectangle object with those dimensions

### Accessing Instance Variables

* Using dot notation consisting of
  * object name
  * dot
  * property name (or instance variable)

```python
obj.myvar

# the rectangle example we have two properties
rect.width # the width of a rectangle object rect
rect.height
rect.area() # return the area of a rectangle object rect
```

### Instance Variables Example

```python
#to access the instance variable
r1 = Rectangle (200,100)
print(r1.width)
#Output 200
print(r1.height)
#Output 100
```

### Invoking Instance Methods

* Using dot notation consiting of
  * object name
  * dot
  * method name
  * arguments list

```python
obj.mymethod(arg1,arg2)
```

### Instance Method Example

```python
r1 = Rectangle(200,100)
print(r1.area())
# Output 20000
```

### Copying Objects

* we need to understand how references work
* when we instantiating a new object we create a new object
* Variables assigned to objects are references
* Each object has a unique reference identity
* Assignment operator copies only the reference identity

```python
variable = Class()
```

### Copying Objects Example 1

* problem with using the assignment operator for copuying objects
* first we create a rectangle object with a width of 200  
and height of 100 and assign it to the variable r1.
* then set the variable r3 to r1

```python
r1 = Rectangle(200,100)
r3 = r1
r3.width = 150
print(r3.width, r3.area())
# Output
150 15000
```

* it looks like r1's value have changed as well

```python
r1 = Rectangle(200,100)
r3 = r1
r3.width = 150
print(r3.width, r3.area())
print(r1.width, r1.area())
# Output
150 15000
150 15000
```

### Identity Function

lokking at an objects identity by using the id function

```python
id(obj)
```

return obj's identity

### Copying Objects Example 2

```python
r1 = Rectangle(200,100)
r3 = r1
# we have not create a new object, we just referencing r1 from r3; any changes to r3 affect r1

r3.width = 150
print(id(r1)==id(r3))
# Output
True
r3= Rectangle(200,100)
print(id(r1)==id(r3))
# Output
False
r3.height = 75
print(r.height, r3.height)
# Output
100 75
```

---

### links

[Object Oriented Design](https://www.youtube.com/watch?v=fJW65Wo7IHI)
[docs](https://docs.python.org/3/tutorial/classes.html)
[special methods docs](https://docs.python.org/3/reference/datamodel.html#specialnames)
[obect __init__](https://docs.python.org/3/reference/datamodel.html#object.__init__)
