---
title: 0708_OOP_SetterGetter
layout: default
---

### Setters and getters 

- are methods used to access and modify the attributes of an object in a controlled manner. 
- They are part of the concept of encapsulation, which allows for better control over the access to attributes of a class.

### Getter (getter method, accessor method): 

- is used to retrieve the value of a private attribute of a class. It typically has the naming convention `get_attribute_name()` and is used to access the value of a private attribute without directly accessing it. Getters allow for controlled access to the attribute, enabling validation or computation before returning the value.

### Setter (Setter method, also known as a mutator method):

- is used to modify the value of a private attribute of a class. 
- It typically has the naming convention `set_attribute_name(value)` and is used to modify the value of a private attribute. Setters allow for controlled modification of the attribute, enabling validation or computation before assigning the new value.

```python
class Person:
    def __init__(self, name):
        self._name = name  # Private attribute

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Name must be a string.")

# Usage
person = Person("Alice")
print(person.get_name())  # Output: Alice
person.set_name("Bob")
print(person.get_name())  # Output: Bob
person.set_name(123)  # Raises ValueError
```

- `_name` is a private attribute of the Person class. 
- `get_name()` is the getter method used to retrieve the value of `_name`, and `set_name()` is the setter method used to modify the value of `_name`. They provide controlled access to the `_name` attribute, allowing validation of input values.