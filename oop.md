---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
>  [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [OOP](./oop.html) ||

***
### Classes and Objects
- Programmer defined types to organize code and data.
- Defining a class in effect creates a new data type.
- When you create a type MyClass, the class identifier (called class statement) is in CapCase (capitalized).

```python
class MyClass:
    """body can be even a docstring"""
    """here to define the variables and methods"""
```

### instantiation
- means to create a new object
- the object is an instance of the class
- Every object is an instance of a class. 
- therefore object and instance are interchangable
- A class instance with a defined set of properties is called an object. 
- data fields don't need to be declared ahead of time - you can create them on the fly
    - define a class 
     ```python
        class MyClass:
    ```
    - create a new object of the class type:
    ```python
        instance = MyClass()
    ```

Fields of an instance are initialized by including **__init__**.

```python
class Circle:
    def __init__(self):
        self.radius = 1
my_circle = Circle()
print(2 * 3.14 * my_circle.radius)
# OUTPUT
31.4        
```
### self
- The term self in the attributes refers to the corresponding instances (objects).
- by convention **self** is always the first argument of __init__.


### __init__ method (is not a constructor)
- to initialize data when a new instance of a class is created (attributes such as title, quantity, author, and price.) 

### __new__ method (like a constructor)
- called on object's creation and returns an initialized object.
