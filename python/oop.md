---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
>  [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [OOP](./oop.html) ||

***
### Classes and Objects
- A programmer-defined type is called a class => Defining a class creates a new data type.
- When you create a type MyClass, the class identifier (called class statement) is in CapCase (capitalized).
- when you define a class you define the general behavior a category of objects can have. 
```python
class MyClass:
        """body can be even a docstring"""
```

### instantiation 
-> to create an instance of the class you to create an object (object and instance are interchangable)
- create a new object of the class type:
    ```python
        instance = MyClass()
    ```

What do most dogs have in common? They
- have a name
- age
- sit or walk
- can roll over

```python
class Dog:
    """a dog class"""  
  
    def __init__(self, name, age):
        """Initialize name and age attributes (fields of an instance initialized via **__init__**)."""
        """by convention **self** is always the first argument of __init__"""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
```

### self
- refers to the corresponding instances (objects).
