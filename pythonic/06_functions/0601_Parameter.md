---
title: Python - Functions 
layout: default
---

||[back](./index.html)

### Paramter

Syntax

```python
def function_name(parameter):
    """ function takes parameter and does stuff."""
    Body is intended
    return [expression]
	# passing back an expression to the caller
 
function_name()
# the caller gets the function going
```

Example

```python
def names():
    return ['Augustus', 'Tiberius', 'Diocletian']
names()
# Output
# ['Augustus', 'Tiberius', 'Diocletian']
```

```python
def greet(name):
    """
    This function greets the user with the given name.
    """
    return "Hello, " + name + "!"

# Function call
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```

---

```python
# no_params.py

shopping_list = {
    "Bread": 1,
    "Milk": 2,
    "Butter": 1, 
    "Coffee": 1,
}
# shopping_list is a global variable
def show_list():
    for item_name, quantity in shopping_list.items():
        print(f"{quantity} x {item_name}")

show_list()
```

=> Global Variables like this is not Good Practice
=> multiple functions accessing same data structure => hard to find bugs
=> Example: pass the dictionary to a function as an argument

```python

# required_params.py

shopping_list = {}

def add_item(item_name, quantity): 
    #this function has two parameters
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else: 
        shopping_list[item_name] = quantity

add_item("Bread", 1)
add_item("Blueberry Pies", 5)

print(shopping_list)
    
```

```python
# optional_arguments with default values
# you can call with or without Argument
# Use Dfault Value if no Argument provided

#Default values assigned to input parameters

shopping_list = {}

def add_item(item_name, quantity=1): 
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else: 
        shopping_list[item_name] = quantity

add_item("Bread")
add_item("Strawberry Pies", 5)

print(shopping_list)
```

you can pass required and optional arguments as Keyword Arguments (named arguments)

```python
add_item(item_name = "Strawberry Pies", quantity = 5)
```

you refactor previous code so that it also process both

```python
shopping_list = {}

def show_list(include_quantities=True):
    for item_name, quantity in shopping_list.items():
        if include_quantities:
            print(f"{quantity}x {item_name}")
        else:
            print(item_name)

def add_item(item_name='', quantity=1): 
    if item_name in shopping_list.keys():
        shopping_list[item_name] += quantity
    else: 
        shopping_list[item_name] = quantity

add_item("Bread")
add_item("Strawberry Pies", 5)
show_list()
print()
show_list(False)
# only the items are displayed

```

---
