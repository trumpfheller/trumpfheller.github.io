---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)

***

## Defining Functions

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

docstring vs comments
> ***docstring*** describes the function's external behavior, and the parameters it takes.

>  ***comments*** should document internal info about how the code works.


### Default Parameter
- allow some arguments to be omitted when the function is called.
- You declare a default variable by assigning

```python
def func_name(arg1, arg2=default2)
```
Example

```python
def power (x, y=2):
  r = 1
  while y > 0:
    r = r * x
    y = y - 1
  return r

power(3, 3)
```
- if y isn't given in the call to the function, the default value is 2 (square function)


### Positional Parameter
- When the function is called, the parameters used in the calling code are matched to the function's parameter variables based on their order.

```python
def function_name(parameter1,parameter2,parameter3):
	Body is intended
	return [expression]

function_name(parameter1,parameter2,parameter3)
```

```python
def greeting(firstName, lastName):
  """Welcome function with user input"""
	print("Welcome" + firstName )
	print("Welcome" + lastName )

firstName = input("What is your first name? ")
lastName = input("What is your last name? ")

greeting(firstName, lastName)
```

### Passing Arguments by Parameter Name
- suited for functions with very complex behavior (graphical user interface; Tkinter package)

```python
def power(x,y):
# x to the power of y
  r = 1
  while y>0:
    r = r*n
    y = y-1
  return r

power(3,3)
#OUTPUT: 27
power(y=2,x=3)
# when you call it by name, the order is irrelevant
#OUTPUT
``` 
### Variable Numbers of Arguments
```python
def multiplier(*num):
    prod = 1
#initialize prod variable with zero    
    for i in num:
        prod = prod * i

    print("Product:",prod)

multiplier(3,5)
multiplier(1,2,4)
multiplier(2,2,6,7)

# OUTOUT
Product: 15
Product: 8
Product: 168
```

```python
def multiply_numbers(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

print(multiply_numbers(1,2,3))
#OUTPUT 9
```

### Indefinite Number of Positional Arguments
- task: find maximum number in the argument (3,2,8,1,1,5) 
- steps: collect them in a [tuple](./tuples.html) and then use list to find the max.

```python
def maximum(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
        return maxnum
    
    
print(maximum(3,2,8,1,1,5))
#OUTPUT 8
```

### Indefinite Number of Arguments Passed By Keywords
- prefix ** collects all keyword arguments into a dictionary

```python
def foo(**kwargs):
  print("Learn coding with {0} using {1}!".format(kwargs["org"],kwargs["tech"]))
foo(org = "w3", tech = "Python")
#OUTPUT
Learn coding with w3 using Python!
```

### Two types of variable-length arguments
- Non - Keyworded Arguments denoted as (*args)
- Keyworded Arguments denoted as (**kwargs)


### lambda Expressions
- can take any number of arguments, but can only have one expression.
- use them as an anonymous function inside another function.

Syntax
```python
lambda argument1, argument2 : expression
```
Example
```python
x = lambda a, b: a * b
print(x(5, 6))
# OUTPUT
30
```
```python
def myfunc(n):
  return lambda a : a * n
```

```python
"""doubles the number you send in"""
1 def myfunc(n):
2  return lambda a : a * n
3
4 mydoubler = myfunc(2)
5 
6 print(mydoubler(11))
```
