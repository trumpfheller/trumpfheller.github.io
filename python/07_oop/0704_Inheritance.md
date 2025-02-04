---
title: Python OOP_Inheritance
layout: default
---

## Inheritance

- Creating a new class from an existing class, inheriting its attributes and methods.

### Base class

- can be any existing class
- No modification required 


### Example Base Class: Shape

```python
class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        return f"{self.__class__.__name__}"
```

- The Shape class defines the blueprint for shapes.
- The `__init__` method is a constructor that initializes the object. Here, it doesn't do anything but can be extended by subclasses.
- The `area` method is intended to be overridden by subclasses. It raises a `NotImplementedError`, indicating that subclasses should provide their own implementation of this method.
- The `__str__` method provides a string representation of the shape, which defaults to the class name.
- `NotImplementedError` is a built-in exception that is commonly used in abstract base classes or methods to indicate that the method or function being called is intended to be overridden by subclasses, but has not been implemented yet in the current class.

### Derived class

- Is more specific and specialized than its base class
- can have its own members
- can use base class members
- can modify or override a base class members  

Syntax

```python
class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        # child initializer calls parent initializer
```

> If you forget to invoke the `__init__()` of the parent class then its instance variables would not be available to the child class.

### Initializer Method

- use `super()` function to refer (give reference) to a base class. 
- We would then invoke the base's initializer method and pass in any required arguments.



### Example Derived Class: Rectangle

```python
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
```

### Example Derived class 2

```python
class Parent:
    def func1(self):
        print("This is function 1")
class Child(Parent):
    def __init__(self, name):
        self.name = name

    def func2(self):
        super().func1()
        print(f"This is function 2 for {self.name}")

ob = Child("Alice")
ob.func2()
```

OR

```python
class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          super().func1()
          print("this is function 2")
ob = Child()
ob.func2()
```

* A class does not require an `__init__()` method in order to be inherited from or instantiated. 
* The presence of an `__init__()` method in a `Parent` class is not mandatory for its `Child` classes to function correctly, especially when you're not initializing any attributes specific to instances of the parent class.

Let's break down why the script works without an __init__() method in the Parent class:

Parent Class (Parent):
* Since Parent does not have an `__init__()` method, Python provides a default constructor that does nothing implicitly.

Child Class (Child):
* inherits from Parent using class Child(Parent).
* It defines its own `__init__()` method that initializes `self.name`.
* It defines `func2()`, which calls `super().func1()` to invoke `func1()` from the `Parent` and then prints "This is function 2 for {self.name}".

Instance Creation and Method Invocation:
* `ob = Child("Alice")` creates an instance of Child with name attribute set to "Alice".
* `ob.func2()` calls `func2()` method of Child, which in turn calls `func1()` from Parent using `super().func1()`, and then prints "This is function 2 for Alice".


---

### Easy Example 1 

> Shape is the base class 

> Rectangle and Triangle are the derived classes.

```python
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0  # Default implementation returns 0

    def __str__(self):
        return f"{self.__class__.__name__}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

def create_rectangle():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    return Rectangle(width, height)

# Create a rectangle with user input
rectangle = create_rectangle()
print(rectangle) 
# Calls Rectangle's __str__ method
print(f"Area of the {rectangle}: {rectangle.area()}") 
# Calls Rectangle's area method
# Since create_rectangle() always returns a Rectangle object 
# when valid input is provided, there is no need for an additional check.
```

### Easy Example #2 - Base Class: Shape & Derived Class: Rectangle

```python
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0  # Default implementation returns 0

    def __str__(self):
        return f"{self.__class__.__name__}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

# Prompt user for dimensions of the rectangle
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))

# Create a Rectangle object
rectangle = Rectangle(width, height)

# Print the Rectangle object and its area
print(rectangle)  
# Calls Rectangle's __str__ method
print(f"Area of the {rectangle}: {rectangle.area()}")  
# Calls Rectangle's area method

```

### Advanced Example Base Class: Shape & Derived Class: Rectangle

```python
class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        return f"{self.__class__.__name__}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

def create_rectangle():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    return Rectangle(width, height)

# Create a rectangle with user input
rectangle = create_rectangle()
if rectangle:
    print(rectangle)
    print(f"Area of the {rectangle}: {rectangle.area()}")
'''
Enter the width of the rectangle: 3
Enter the height of the rectangle: 3
Rectangle(width=3.0, height=3.0)
Area of the Rectangle(width=3.0, height=3.0): 9.0
'''
```

### Example User can pick Rectangle and Triangle from Shape

```python
class Shape:
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def __str__(self):
        return f"{self.__class__.__name__}"

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height})"

def create_shape():
    shape_type = input("Enter the type of shape (rectangle/triangle): ").lower()
    
    if shape_type == "rectangle":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        return Rectangle(width, height)
    
    elif shape_type == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return Triangle(base, height)
    
    else:
        print("Invalid shape type")
        return None

# Create a shape with user input
shape = create_shape()
if shape:
    print(shape)
    print(f"Area of the {shape}: {shape.area()}")
```

--- 

### Types Of Inheritance

* Single Inheritance

```python
class Parent:
      def func1(self):
           print("this is function one")
class Child(Parent):
      def func2(self):
            print(" this is function 2 ")
ob = Child()
ob.func1()
ob.func2()
```

* Multiple Inheritance
  * child inherits from more than one

```python
class Parent:
     def func1(self):
         print("this is function 1")
class Parent2:
      def func2(self):
           print("this is function 2")
class Child(Parent , Parent2):
     def func3(self):
          print("this is function 3")
ob = Child()
ob.func1()
ob.func2()
ob.func3()
```

* Multilevel Inheritance
  * child class becomes a parent class for another child class

```python
class Parent:
      def func1(self):
           print("this is function 1")
class Child(Parent):
      def func2(self):
      print("this is function 2")
class Child2(Child):
      def func3("this is function 3")
ob = Child2()
ob.func1()
ob.func2()
ob.func3()
```

* Hierarchical Inheritance
  * multiple inheritance from the same base

```python
class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Parent):
     def func3(self):
         print("this is function 3")
ob = Child()
ob1 = Child2()
ob.func1()
ob.func2()
```

* Hybrid Inheritance
  * multiple inheritances taking place in a single program.

```python
class Parent:
      def func1(self):
          print("this is function one")
class Child(Parent):
      def func2(self):
           print("this is function 2")
class Child1(Parent):
      def func3(self):
       print(" this is function 3"):
class Child3(Parent , Child1):
      def func4(self):
           print(" this is function 4")
ob = Child3()
ob.func1()

```

### information flow


```python
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age # inheriting the properties of parent
        super().__init__("Mike", age)

    def displayInfo(self):
        print(self.sName, self.sAge)

obj = Student("Maya", 53) # Object Creation
obj.display()
obj.displayInfo()
```

1. When `Student("Maya", 53)` is executed, the `__init__` method of the `Student` class is called with `name="Maya"` and `age=53`.
2. Inside the Student's `__init__` Method:
  * `self.sName` is set to "Maya".
  * `self.sAge` is set to 53.
  * The `super().__init__("Mike", age)` call invokes the `__init__` method of the `Person` class with `name="Mike"` and `age=53`.
3. Inside the Person's `__init__` Method:
  * `self.name` is set to "Mike".
  * `self.age` is set to 53.
  * The control returns back to the Student's `__init__` method, completing the initialization of the `obj`.
4. Calling `obj.display()`:
  * The `display` method of the `Person` class is called.
  * It accesses `self.name` and `self.age`, which are "Mike" and 53 respectively.
  * It prints: Mike 53.
5. Calling `obj.displayInfo()`:
  * The `displayInfo` method of the `Student` class is called.
  * It accesses `self.sName` and `self.sAge`, which are "Maya" and 53 respectively.
  * It prints: Maya 53.

---

### Key Points of Inheritance:
* Code Reuse: Common functionality (like `area` and `__str__`) is defined in the base class (`Shape`), reducing code duplication.
* Extensibility: New shapes can be added by creating new subclasses of Shape and implementing the required methods.
* Polymorphism: Objects of different subclasses (Rectangle, Triangle) can be treated as objects of the base class (Shape), allowing for flexible and interchangeable code.

https://www.geeksforgeeks.org/inheritance-in-python/
