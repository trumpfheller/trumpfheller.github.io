---
title: Python OOP_Encapsulation
layout: default
---

## Encapsulation

* bundling the data (attributes) and methods (functions) that operate on the data into a single unit (a class). This helps in hiding the internal state of objects and restricting direct access to some of their components.
* helps in keeping the internal state of objects safe from unintended modifications and allows for better control over how attributes are accessed and modified.
* is a principle of object-oriented programming that hides the internal state (attributes) of an object and restricts direct access to them from outside the class. 
* is achieved by making attributes private and providing controlled access to them through methods like getters and setters.

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


### # Example 2

```python

class Car:
    def __init__(self, make, model, year):
        self.__make = make  # private attribute
        self.__model = model  # private attribute
        self.__year = year  # private attribute
        self.__odometer_reading = 0  # private attribute

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_odometer_reading(self):
        return self.__odometer_reading

    def set_odometer_reading(self, mileage):
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def drive(self, miles):
        print(f"The car has driven {miles} miles.")
        self.__update_odometer(miles)

    def __update_odometer(self, miles):
        self.__odometer_reading += miles


# Creating an instance of Car
my_car = Car("Toyota", "Corolla", 2020)

# Accessing public methods to interact with private attributes
print(f"My car is a {my_car.get_year()} {my_car.get_make()} {my_car.get_model()}.")

# Using encapsulated methods to update and access private attribute
my_car.drive(100)
print(f"Current odometer reading: {my_car.get_odometer_reading()} miles.")

# Trying to directly access a private attribute (will raise an error)
# print(my_car.__odometer_reading)  # This line will raise an AttributeError
```

* Private Attributes: In the Car class, attributes like `__make`, `__model`, `__year`, and `__odometer_reading` are prefixed with double underscores (`__`). This convention in Python indicates that these attributes are intended to be private, meaning they **should not be accessed directly from outside the class**.

* Public Methods: Methods like `get_make()`, `get_model()`, `get_year()`, `get_odometer_reading()`, `set_odometer_reading(mileage)`, and `drive(miles)` provide controlled access to these private attributes. These methods serve as the interface through which external code interacts with the internal state of the Car object.

* Encapsulation in Action: The encapsulation here ensures that the internal state of the `Car` object (make, model, year, odometer_reading) is protected from accidental or unauthorized modification. Access to these attributes is mediated through well-defined methods (`get_*` and `set_*` methods), which enforce any necessary validation or business rules (e.g., not allowing odometer reading to be rolled back).

* Usage Example: The example demonstrates how you can create an instance of Car, access its attributes indirectly through **getter** methods (`get_year()`, `get_make()`, etc.), update its state using `set_odometer_reading()` and `drive()` methods, and ensure that attempts to directly access private attributes (__odometer_reading) from outside the class result in errors.

