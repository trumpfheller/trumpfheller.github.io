---
title: UCB Python - lecture -  05_Functions as Objects 
layout: default
---
>> || [back](./index.html)

---

## Functions as Objects

functions are first-class citizens, which means they can be treated like any other object. 
This includes 

- passing functions as arguments to other functions, 
- returning functions from functions, and 
- storing functions in data structures like lists or dictionaries. 

This concept is known as "Functions as Objects" or "First-Class Functions".

---

### Function Properties

* Functions definition stores name and nody in namespace
* Functions name references a function's body
* Function body is a value

```python
def function (args):
    function_body
```

### Assigned to a variable

* since it is just a value we can store it in a variable
* Note: the value of x is not really a copy, but a reference to the fucntion body.

```python
def function (args):
    function_body

x = function
```

### Functions as Objects Example

* counter = len
*

```python
screenshots
```

### Higher Order Functions

* Functions that takes another function (key function) an argument
* Functions that take another function as an argument are called higher order functions.
* Can invoke key function within the higher order function

```python
def key_function(arg):
    function_body

def higher_order_function(f):
    # why the f?
    function_body

higher_order_function(key_function)
```

* the higher order function can execute the keyfunction to perform whatever specialized calculation it needs.
* this makes higher order function more flexible and versatile. 
* no need to rewrite the function itself.

### Max Functions Example

* max function already exists (built in) - we just need to see how it works

```python
coords = [(1,2,3), (-2,4,9), (6,7,4), (3,8,1)]
# 3D coordinates x,y,z
# each coordinate is a tuple - accessible via index

def mymax(seq):
    mx = seq[0]
    for s in seq[1:]:
        if s[0] > mx[0]:
            mx = s
    return mx
print(mymax(coords))

# Output
(6,7,4)
```

* heart of the function is the comparison if s[0] > mx[0]
* change the > to < and you get a mymin function
* we are only comparing the first items in each tuple with the index operator with an index of 0. (1 and -2 and 6 and 3) and 6 is the highest item
* if we wanted the highest values second item, the y coordinate: if s[1] > mx[1]
* might cause problems (I didn't quit get why)

### Key Function

* called on each item before comparison
* this is invoked whenever there is a comparison invoked
* can be a built in function or custom written one

```python
def key_function(arg):
    # (arg) * should accept a single argument and return a converted value
    function_body
```

```python
coords = [(1,2,3), (-2,4,9), (6,7,4), (3,8,1)]

def mymax(seq):
    mx = seq[0]
    for s in seq[1:]:
        if get_y[s] > get_y[m]:
            # comapring the outputs of the functions, not the values themselves
            mx = s
    return mx
print(mymax(coords))

```

* now we write the key function

```python
coords = [(1,2,3), (-2,4,9), (6,7,4), (3,8,1)]

def get_y(c):
    return c[1]

def mymax(seq):
    mx = seq[0]
    for s in seq[1:]:
        if get_y[s] > get_y[mx]:
            # comapring the outputs of the functions, not the values themselves
            mx = s
    return mx
print(mymax(coords))
```

* to make the code more flexible we take a key parameter

```python
coords = [(1,2,3), (-2,4,9), (6,7,4), (3,8,1)]

def get_y(c):
    return c[1]

def mymax(seq, key):
    mx = seq[0]
    for s in seq[1:]:
        if key[s] > key[mx]:
            # comapring the outputs of the functions, not the values themselves
            mx = s
    return mx
print(mymax(coords, get_y))
# in the function call we pass the key function get_y
# Output
(3,8,1)
# 8 is the highest y value of all items
```

* now we can pass a function to mymax function, making it a higher order function.
* we need to make sure our key function is invoked properly and we place them in our comparison.

### Key Function Example

* comparing the magnitude of each coordinate

```python
import math
coords = [(1,2,3), (-2,4,9), (6,7,4), (3,8,1)]

def get_y(c):
    return c[1]

def magnitude(c):
    return math.sqrt()

def mymax(seq, key):
    mx = seq[0]
    for s in seq[1:]:
        if key[s] > key[mx]:
            mx = s
    return mx
print(mymax(coords, magnitude))
# 
# Output
(-2,4,9)
```

### Built-in Higher Order Functions

* they all accept
  * iterables as arguments
  * optional key functions
    * min() function
    * max() function
    * sorted() function
    * sort() method

### Higher Order Functions Example 1

* how do they work with a key function

```python
# length of the city strings
cities = ['Berkeley', 'Oakland', 'San Francisco', 'San Jose']
lengths = [len(city) for city in cities]
print(lengths)
cities.sort(key=len)
print(cities)

# Output
[8,7,13,8]
```

### Higher Order Functions Example 2

* how do they work with a key function

```python
# length of the city strings
city_area = [('Berkeley', 10.4), ('Oakland', 55.93), ('San Francisco', 46.91)]
print(min(city_area))
print(max(city_area))
print(sorted(city_area, reversed=True))

# Output
('Berkeley', 10.4)
('San Francisco', 46.91)
[('San Francisco', 46.91), ('Oakland', 55.93), ('Berkeley', 10.4)]
```

* now lets try this with a key function

```python
city_area = [('Berkeley', 10.4), ('Oakland', 55.93), ('San Francisco', 46.91)]

def get_city_area(city):
    # keyt function to access the area part of the tuple
    return city[1]

print(min(city_area, key=get_area))
print(max(city_area, key=get_area))
print(sorted(city_area, key=get_area, reversed=True))

# Output
('Berkeley', 10.4) # since Berkeley has the smallest area
('Oakland', 55.93) # has the largest area
[('Oakland', 55.93), ('San Francisco', 46.91), ('Berkeley', 10.4)]
```

---

1. Assigning Functions to Variables:
You can assign a function to a variable just like any other object:

```python
def greet():
    return "Hello!"

greet_func = greet
print(greet_func())  # Output: Hello!

```

2. Passing Functions as Arguments:
Functions can be passed as arguments to other functions:

```python
def say_hello(func):
    return func()

print(say_hello(greet))  # Output: Hello!

```

3. Returning Functions from Functions:
Functions can also return other functions:

```python
def outer_func():
    def inner_func():
        return "Inner function"
    return inner_func

inner = outer_func()
print(inner())  # Output: Inner function

```

4. Storing Functions in Data Structures:
Functions can be stored in data structures like lists or dictionaries:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

func_list = [add, subtract]
print(func_list[0](3, 2))  # Output: 5

```

5. Anonymous Functions (Lambda Functions):
Lambda functions are a way of creating small anonymous functions. They can be used where function objects are required:

```python
square = lambda x: x ** 2
print(square(3))  # Output: 9
```

Functions as Objects provide flexibility and enable powerful programming paradigms like functional programming. They allow for cleaner and more modular code by enabling functions to be manipulated and passed around dynamically at runtime. This makes Python a versatile language for various programming styles and paradigms.