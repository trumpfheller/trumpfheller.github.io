---
title: 0707_OOP_Encapsulation
layout: default
---


### Encapsulation

- helps in keeping the internal state of objects safe from unintended modifications and allows for better control over how attributes are accessed and modified.
- is a principle of object-oriented programming that hides the internal state (attributes) of an object and restricts direct access to them from outside the class. 
- is achieved by making attributes private and providing controlled access to them through methods like getters and setters.

```python
class Car:
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

# Usage
my_car = Car("Toyota", "Camry")
print(my_car.get_make())  # Output: Toyota
print(my_car.get_model())  # Output: Camry

my_car.set_make("Honda")
my_car.set_model("Accord")
print(my_car.get_make())  # Output: Honda
print(my_car.get_model())  # Output: Accord

# Directly accessing private attributes raises an error
# print(my_car.__make)  # This line raises an AttributeError
```

- the attributes `'__make'` and `'__model'` are private, denoted by the double underscores (`'__'`). This means they cannot be directly accessed from outside the class. Instead, access is provided through getter and setter methods `(get_make()`, `set_make()`, `get_model()`, `set_model()`, which enable controlled interaction with the attributes.
