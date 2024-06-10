---
title: Python - FunctionFunction Arguments 
layout: default
---

||[back](./index.html)

---

## Function Arguments

### Arguments and Parameters

- Argument = value you pass to the function
- Parameter = witin the function

---

### Positional Arguments

* Number of arguments match the number of parameters
* Order is significant - each arguments corresponds to each parameter

```python
def name_joiner(first, last, title):
    return title + ' ' + first + ' ' + last
print(name_joiner('Stephen', 'Strange','Dr.')) 
print(name_joiner('Dr.'. 'Stephen', 'Strange')) 
```

```python
def my_function(arg1, arg2, arg3):
    """
    This function takes three positional arguments.
    """
    print("Argument 1:", arg1)
    print("Argument 2:", arg2)
    print("Argument 3:", arg3)

# Calling the function with positional arguments
my_function("Hello", 42, True)
```

### Keyword Arguments

* parameter name can be specified
  * parameter=argument

```python
def function(param1, param2):
    function body

function(param2=arg2, param1=arg1)
```

* beause the arguments have associated keywords, it does not need to follow the order of the parameters.


```python
def greet(name, age):
    """
    This function greets the person with the given name and age.
    """
    print("Hello,", name + "!", "You are", age, "years old.")

# Calling the function with keyword arguments
greet(name="Alice", age=30)
```

### Keyword Argument Examples

```python
def name_joiner(first, last, title):
    return title + ' ' + first + ' ' + last
print(name_joiner(title='Dr.', first='Stephen', last='Strange'))
# Output
Dr. Stephen Strange
```

### Mix positional and keyword arguments

```python
def name_joiner(first, last, title):
    return title + ' ' + first + ' ' + last
print(name_joiner('Stephen', title='Dr.',last='Strange'))
# Output
Dr. Stephen Strange
```

### Default Arguments

* Argument can be omitted

```python
def function(param1, param2=value):
    function body

function(arg1)
```

### Default Argument Example 1

```python
def name_joiner(first, last, title=''):
    # title is now optional and an empty string
    return title + ' ' + first + ' ' + last
print(name_joiner('Stephen', 'Strange'))
# Output
Stephen Strange
```

### Default Argument Example 2

```python
def name_joiner(first, last, title=''):
    # title is now optional and an empty string
    return title + ' ' + first + ' ' + last
print(name_joiner('Stephen', 'Strange', 'Mr.'))
# Output
Mr. Stephen Strange
```

* if not omitted, the argument overrides default value

### Variable Number of Arguments

* Call a function with any number of arguments

```python
def function (*params):
    function body
function(1,2,3)
```

* collects arguments into a tuple

### Variable Number of Arguments Example1

```python
def mean(*numbers, prec=2):
    # round our mean by default precision of 2
    m=sum(numbers)/len(numbers)
    # sum and len accept sequences
    return round(m,prec)

print(mean(3,3,4,1,2,6))
# Output
# 3.17

print(mean(16, 11, 431, pres=1))
# Output
# 152.7
```

### Variable Number of Arguments Example2

* sum_all = adding all the numbers in all sequences

```python
def sum_all(*sequences):
    # all arg have to be #s of sequences
    total = 0
    for seq in sequences:
        for n in seq
        total +=n
    return total

print(sum_all())
print(sum_all([1,2,3]))
# sequence is a tuple ([1,2,3])
print(sum_all([1,2],[3], [4,5,6]))
# passing 3 lists
```

---

### Call a function with parenthesis

* no value but returns a string

```python
def make_a_sound():
    print('quack')
```

* returns a value

```python
def agree():
    True
```

```python
def agree():
    if agree():
        print('Splendid')
    else:
        print('That was to be expected.')
```

### Arguments and Parameters

Argument = value you pass to the function
Parameter = witin the function
Function should only be responsible for one thing

```python
def echo(anything):
    return anything + ' / ' + anything

echo('Rumplestiltskin')
```

* If a function doesn't call return explicitly, the caller gets the result None.

### None is usefull

* None, True, or False
* You need None to distinguish a missing value from an empty value.
* False (not the same as None): Zero valued integers, floats, empty strings (''), lists([]), tuple((,)), dictionaries({}) and sets (sets())

```python
def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else: 
        print(thing, "is False")
whatis(None)
whatis(True)
whatis(False)
# try with real values
whatis(0)
whatis(0.0)
whatis('')
whatis(())
whatis([])
whatis({})
whatis([0])
whatis(set())
whatis([''])
```

### Positional Arguments

* copied to their corresponding parameters in order

```python
def menu(wine, entree, dessert):
    return{'wine':wine, 'entree': entree, 'dessert': dessert}

menu('Chardonnay', 'chicken', 'cake')
```

Another example

```python
def f(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')

f('bananas', 1.74, 6)
```

* you need to remember the meaning of each position

### Keyword Arguments

* to avoid confusion with positional arguments
* specify arguments by the names of their corresponding parameters, even in differnt order from their definition in the function

```python
menu(entree='beef', dessert= 'Streuselkuchen', wine='Bordeaux')
#Output
{'wine':'Bordeaux', 'entree': 'beef', 'dessert': 'Streuselkuchen' }  

```

* you can mix positional and keyword argument

functions is expected to run each time with a fresh result list

### specify Default Paramter Values

```python
def buggy():

```

```python
def works(arg):

```

```python
def nobuggy(arg, result=None):

```

### Explode/Gather Positional Arguments with *

grouping a variable number of postional arguments into a single tuple or parameter values.
(tuples are non mutable)

```python
def print_args(*args):
    print('Positional tuple: ', args)

```

* whatever you give it it will be printd as a args tuple

```python
def print_args(*args):
    print('Positional tuple: ', args)
    
print_args(3,2,1, 'wait!'. 'uh..')
# Output
Positional tuple: (3,2,1, 'wait!'. 'uh..')
```

* If you function has required positional arguments, put them first; *args goes at the end and grabs all the rest

```python
def print_more(required1, required2, *args):
    print('this is required 1: ', required1)
    print('this is required 2: ', required2)
    print('all the rest: ', args)

print_more('cap', 'gloves', 'monocole', 'mustach wax')
# Output
```

* You can use the * syntax in a a function call or definition.

### puff-args (values are exploded)

* Outside of a function: *args explodes the tuple args into comma-seperated positional parameters

### inhale-args (values are gathered)

* Inside of a function: *args gathers all the positional arguments into a singles args tuple, You could use the names*params and params, but it's common practice to use *args foe both the ourside argument and inside parameter.

### Explode/Gather Positional Arguments with **

* to group keyword arguments into a dictionary. where the arguments names are the keys, and their values are the corresponding dictionary values.

```python
def print_kwargs(**kwargs):
    print('keyword arguments: ' , kwargs)
print_kwarks()
# Output
keyword arguments: {}

print_kwargs(wine='Bordeaux', entree='mutton', dessert= 'macaroon' )
# Output
keyword arguments: {dessert= 'macaroon', wine='Bordeaux', entree='mutton'}
```

* inside the function, kwargs is a dictinary parameter
Argument order is:
* required positional arguments
* optional positional arguments (*args)
* optional keyword arguments (**args)

* The *8 syntax is valid only in a function call or definiton.

#### Summarizing

* You can pass keyword argument to a function, which will match them inside to keyword parameter
* You can pass a dictionary argument to a function, and inside it will be dictionary parameters
* You can pass one or more keird arguments (name=value) to a functions, and gather them inside as **kwargs, which resolves to the dictionary parameter called kwards
* Outside of a function, **kwargs explodes a dictionary kwargs into name=value arguments
Inside function,**kwargs gathers name=value arguments into the sindle dictionary parameter kwarg.

### Keyword-Only Arguments

```python
def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)

data = ['a','b','c','d','e','f',]
print_data(data)

# Output

a
b
c
d
e
f
```

### Mutable and Immutable Arguments

page 151
passing arguments to functions:

* if argument is mutable, its value can be cahgend from inside the function via its corresponding parameter.

```python
outside = ['one','fine','day']
def mangle(arg):
    arg[1] = 'terrible!'

>>> outside
# Output
['one','fine','day']
>>> mangle(outside)
outside
['one','terrible!','day']
```

---
