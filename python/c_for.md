---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [Conditional](./c_conditional.html) || [while loop](./c_while.html) 
> [OOP](./oop.html) || [back](./)


***

## for loop
- to iterate over a sequence of elements.
- to iterate over a sequence of values. 

### for loop in range() method
- iterate through a sequence of numbers generated using the range function
- variable(x) will take each of the values in the sequence that loop iterates through.
```python
for x in range(5):
    print(x)
#OUTPUT
0
1
2
3
4
```
### for loop in a function 
- use a for loop to sum the squares of the numbers in a range.

```python
def square(n):
    """function to calculate the square of a number"""
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += int(square(n))
    return sum

print(sum_squares(10)) # Should be 285
```
[maybe add an user input?]
