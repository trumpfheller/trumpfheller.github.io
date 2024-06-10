---
title: Python 0706_polymorphism
layout: default
---

## Polymorphism

- ability of different objects to respond to the same message or method call in different ways. 
- It allows objects of different types to be treated as if they were instances of a common superclass, enabling more flexible and dynamic code.

two main types of polymorphism in Python:

Method Overriding: 
This occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. When the method is called on an object of the subclass, the subclass's implementation is executed instead of the superclass's implementation.

Duck Typing: 
This is a concept in Python where the type or the class of an object is less important than the methods it defines. If an object implements a particular method or set of methods, it can be used wherever that method or set of methods is expected, regardless of its actual type.

```python
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

'''
Both Dog and Cat classes inherit from the Animal class and override its speak() method with their own implementations.
'''
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Function that uses polymorphism
def make_sound(animal):
    return animal.speak()

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the function with different objects
print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!

'''
The make_sound() function accepts any object that has a speak() method (duck typing), allowing it to work with both Dog and Cat objects interchangeably.
When make_sound() is called with a Dog object, it executes the speak() method of the Dog class, and when called with a Cat object, it executes the speak() method of the Cat class.
'''
```