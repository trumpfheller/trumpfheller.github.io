---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
>  [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [OOP](./oop.html) ||

***

## Defining Functions

### Syntax
```python
def function_name(parameter):
  """ function takes parameter and does stuff."""
	Body is intended
	return [expression]
	# passing back an expression to the caller
 
function_name()
# the caller gets the function going
```
#### docstring vs comments
> ***docstring*** describes the function's external behavior, and the parameters it takes.

>  ***comments*** should document internal info about how the code works.


### Default Parameter
- allow some arguments to be omitted when the function is called.
- You declare a default variable by assigning

```python
def func_name(arg1, arg2=default2)
```
#### Example

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
- must agree in order and number with the parameters declared in the function definition.
- When the function is called, the parameters used in the calling code are matched to the function's parameter variables based on their order.

```python
def function_name(parameter1,parameter2,parameter3):
	Body is intended
	return [expression]

function_name(parameter1,parameter2,parameter3)
```
