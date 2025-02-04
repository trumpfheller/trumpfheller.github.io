---
title: Python || OOP_Defining Classes
layout: default
---

## Class Definition

- in python all data types are classes - a class is a data type.

```python
class ClassName:
    body 
    pass
```

```python
class ClassName:
    instance = MyClass()
```

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
        # instance.variable = value
```

```python
class Circle:
    def __init__(self):
        self.radius = 1
        # radius is an instance variable of circle instance
```

- all uses of instance variables require explicit mention of the containing instance. A refrence to a variable by itself is a refernce not to a instance variable, but to a local variable in the executing method.

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

```text
- Properties
  - width
  - height

- Methods
  - area
  - perimeter
  - draw
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

```python
class Car:
    # Class attribute (shared among all instances)
    wheels = 4

    def __init__(self, make, model, year):
        # Instance attributes (unique to each instance)
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        # Instance method
        print(f"The engine of the {self.year} {self.make} {self.model} is now running.")

    def stop_engine(self):
        # Another instance method
        print(f"The engine of the {self.year} {self.make} {self.model} is now off.")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2021)

# Accessing class attribute
print(f"My car has {my_car.wheels} wheels.")

# Accessing instance attributes
print(f"I have a {my_car.year} {my_car.make} {my_car.model}.")

# Calling instance methods
my_car.start_engine()
my_car.stop_engine()
```

1. Class Attribute: wheels is a class attribute, shared by all instances of the class. It is defined directly within the class.

2. Instance Attributes: make, model, and year are instance attributes, unique to each instance of the class. They are defined within the __init__ method, which is a special method called a constructor. The self parameter is a reference to the current instance of the class.

3. Instance Methods: start_engine and stop_engine are instance methods. They operate on the instance attributes and use self to access them.

### Distinguishing Instance Variables from Local Variables

```python
class Example:
    def __init__(self, value):
        self.value = value  # Instance variable

    def display_value(self):
        value = 10  # Local variable
        print(f"Local variable value: {value}")
        print(f"Instance variable value: {self.value}")

# Creating an instance of Example
example = Example(42)

# Calling the method
example.display_value()
```

- Instance Variable: self.value is an instance variable. It is unique to each instance of the class and defined in the __init__ method.
- Local Variable: Inside the display_value method, value = 10 is a local variable. It only exists within the scope of the display_value method.


### difference between instance attributes and class attributes.

Instance Attributes
Scope: Instance attributes are specific to each instance of a class.
Definition: They are typically defined within methods (like __init__) using the self keyword.
Sharing: Each instance of the class has its own copy of the instance attributes.
Access: Accessed and modified using self.attribute_name.

Class Attributes
Scope: Class attributes are shared across all instances of a class.
Definition: They are defined directly within the class body.
Sharing: All instances of the class share the same copy of the class attributes.
Access: Can be accessed using the class name or through an instance. However, modification through an instance creates an instance attribute with the same name, shadowing the class attribute.

```python
class Car:
    # Class attribute
    wheels = 4

    def __init__(self, make, model, year):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year

# Creating instances of Car
car1 = Car("Mercedes", "CL500", 2004)
car2 = Car("Ford", "F150", 2016)

# Accessing class attribute via the class name
print(f"Number of wheels (class): {Car.wheels}")

# Accessing class attribute via instances
print(f"Number of wheels (car1): {car1.wheels}")
print(f"Number of wheels (car2): {car2.wheels}")

# Accessing instance attributes
print(f"Car1: {car1.make}, {car1.model}, {car1.year}")
print(f"Car2: {car2.make}, {car2.model}, {car2.year}")

# Modifying class attribute using the class name
Car.wheels = 6
print(f"Number of wheels after modification (class): {Car.wheels}")
print(f"Number of wheels after modification (car1): {car1.wheels}")
print(f"Number of wheels after modification (car2): {car2.wheels}")

# Modifying instance attribute
car1.wheels = 8
print(f"Number of wheels after modification (car1 instance): {car1.wheels}")
print(f"Number of wheels after modification (car2 instance): {car2.wheels}")
```

- start thinking about the properties (instance variables)
- then about the methods to operate on the properties

Step 1: Define the Properties (Instance Variables)
We need to identify the properties that each bank account will have:

account_number: The unique identifier for the account.
account_holder: The name of the account holder.
balance: The current balance of the account.

Step 2: Define the Methods to Operate on the Properties
Next, we think about the operations that we might want to perform on a bank account:

deposit(amount): Adds a specified amount to the balance.
withdraw(amount): Subtracts a specified amount from the balance, if sufficient funds are available.
get_balance(): Returns the current balance.
display_account_info(): Prints the account details.

This structured approach helps to clearly separate the definition of the properties 
from the methods that operate on them, 
making the class easier to understand and maintain.

```python
class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        # Define the instance variables (properties)
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance is ${self.balance}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to get the current balance
    def get_balance(self):
        return self.balance

    # Method to display account information
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

# Example usage
account = BankAccount("12345678", "Alice", 1000)
account.display_account_info()

account.deposit(500)
account.withdraw(200)
print(f"Current balance: ${account.get_balance()}")
```

### Example

```python
# car_data.py

car_dict = {
    'Toyota': {
        'model': 'Corolla',
        'year': 2020,
        'color': 'Blue'
    },
    'Honda': {
        'model': 'Civic',
        'year': 2019,
        'color': 'Red'
    }
}
```

```python
# main.py

# Import the car data from the external module
from car_data import car_dict

# Define the base class
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, 
                                    Year: {self.year}, 
                                    Color: {self.color}")

# Define a derived class for Electric Cars
class ElectricCar(Car):
    def __init__(self, brand, model, year, color, battery_capacity):
        super().__init__(brand, model, year, color)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")

# Define a derived class for Gasoline Cars
class GasCar(Car):
    def __init__(self, brand, model, year, color, fuel_type):
        super().__init__(brand, model, year, color)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")

# Create instances of the derived classes using data from the car_dict
def create_cars():
    cars = []
    for brand, info in car_dict.items():
        if brand == 'Toyota':
            car = GasCar(brand, info['model'], 
                                info['year'], 
                                info['color'], 
                                'Petrol')
        elif brand == 'Honda':
            car = ElectricCar(brand, info['model'], 
                                     info['year'], 
                                     info['color'], 
                                     75)  
            # Assuming a battery capacity
        cars.append(car)
    return cars

# Main function to display car information
def main():
    cars = create_cars()
    for car in cars:
        car.display_info()
        print()  # Print a newline for better readability

if __name__ == "__main__":
    main()
```

1. class `Car` defines a base with
* attributes `brand`, `model`, `year`, and `color` 
* method `display_info`.
2. derived class `ElectricCar` adds an attribute `battery_capacity` and overrides `display_info`.
3. derived class `GasCar` adds an attribute `fuel_type` and overrides `display_info`.
4. `create_cars` function creates instances of `ElectricCar` and `GasCar` using data from `car_dict`.
5. `main` function displays the information of each car instance.
