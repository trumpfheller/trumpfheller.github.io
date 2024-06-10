---
title: 07_OOP_Defining Classes
layout: default
---

### Designing Classes Example Rectangle Class

```text
- Properties
  - width
  - height

- Methods
  - area
  - perimeter
  - draw
```

### Class Definition

Syntax for defining a class.

```python
class ClassName:
    """Docstring for the class."""
    
    def __init__(self, attribute1, attribute2):
        """Constructor method to initialize the object's attributes."""
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    
    def method1(self):
        """A method that performs an action."""
        # Method implementation
        pass
    
    def method2(self, param):
        """Another method that performs an action."""
        # Method implementation
        pass
```
* `__init__` is a special method called a **constructor** that initializes the object's attributes.
* `self` is a reference to the current instance of the class and is used to access variables and methods associated with the instance.
* `attribute1` and `attribute2` are parameters that are passed to the constructor to initialize the object's attributes.


### Initializer Method

* a special method invoked when the constructor is called.
* called when we isntantiate an object of this class
* double underscore [called dunders] indicates a special method 

```python
class Classname:
    def __init__(self, param):
        init_body
```

### Instance Variables Definition

- has to be defined within the initializer
- must be prefixed by self variable
- can be accessed anywhere within the class using the self prefix.

```python
class Classname:
    def __init__(self, param):
        init_body
        self.variable = value
```

### Instance Method Definition

```python
class Classname:
    def __init__(self, param):
        method_body
```

- self is automatically set in method calls
def __init__(self, param):
- self: obj
- param: Classname(100)
- obj=Classname(100)

### Self Variable

- the special self variable refers to the object itself within the class code

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
```

- An object's instance members can be accessed from it
  - self.width in def init and self.width in def area   

- Declared as a paramter in instance methods
  - def __init__(self,
  - def area(self

- it is always the first parameter.
 
### Self Variable Example

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
r1 = Rectangle(200,100)
# instantiated a Rectangle object and assigned it r1
```


### Class Definition Example 

```python
class Car:
    """A simple class to represent a car."""

    def __init__(self, make, model, year):
        """Initialize the car with make, model, and year."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Default value for the odometer reading

    def get_description(self):
        """Return a neatly formatted descriptive name for the car."""
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        """Print the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def __str__(self):
        """Return a string representation of the car."""
        return self.get_description()

# Creating an instance of the Car class => instantiating
my_car = Car("Tesla", "Model S", 2023)

# Using methods on the instance
print(my_car)  # Output: 2023 Tesla Model S
my_car.read_odometer()  # Output: This car has 0 miles on it.

# Updating the odometer and reading it again
my_car.update_odometer(150)
my_car.read_odometer()  # Output: This car has 150 miles on it.

# Incrementing the odometer
my_car.increment_odometer(100)
my_car.read_odometer()  # Output: This car has 250 miles on it.
```


- how to define attributes (variables) and methods (functions) within a class.
- difference between instance attributes and class attributes.
- start thinking about the properties (instance variables)
- then about the methods to operate on the properties