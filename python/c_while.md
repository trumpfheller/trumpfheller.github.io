---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [Conditional](./c_conditional.html) || [for loop](./c_for.html)
> [OOP](./oop.html) || [back](./)

***

## while loop

- execute a set of statements in iterations as long as a condition is true 
- to continuously execute code based on the value of a condition. 
- code block can be executed multiple times instead of just once; used for an indefinite number of iterations
- performing an action over and over until a condition has changed.
- Boolean expression determines the execution of the codeblock: code block will keep executing as long as the evaluation 
statement is true. Once the statement is no longer true, the loop exits and the next line of code will be executed.

> a loop is a control structure for codeblock iteration.

### Syntax


```pythyon
while boolean_exp:
    codeblock
```

### Use case
- use them to keep asking for a username if the one provided isn't valid
- try an operation until it succeeds.

```python
1 x=0 #initializing
2 while x<5:
3    print("Not there yet, x=" + str(x))
4    x = x+1
5 print("x=" + str(x))
# OUTPUT
Not there yet, x=0
Not there yet, x=1
Not there yet, x=2
Not there yet, x=3
Not there yet, x=4
x=5
```

***

### while loop inside of a function. 
```python
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)
```

* Step1: 
    * initializing a variable called x (1).
* Step2: 
    * the function received a value and the while loop checks if the value inside of the x variable is less than the parameter n. 
        * If that comparison evaluates to true, then the code inside the while block is executed. 
* Step3: 
    * think it through: 
        - pass a value of 5 as a parameter to this function. In the first pass through the loop, x is always equal to 1, so the comparison: 1 smaller than or equal to 5 would be true and we then enter the body of the loop. 
In the body, we first print a message indicating that the current attempt number and then we increase the value of x by 1. 


The process continues until the result of the comparison isn't true anymore, which happens when x is bigger than n. 
In this example, when the value of x is 6. 
 
#### Example - to call a separate function that evaluates the condition. 

```python
username = get_username()
while not valid_username(username):
    print("invalid username")
    username = get_username()
```

### get_username() function 
- asks the user for a username and a valid_username function that validates that username. 
- here the body of the while loop will be executed until the user enters a valid username. 
=> the condition used by the while loop needs to evaluate to true or false. 

Most common pitfalls when writing loops. 


If you have a loop that's not behaving as expected, check if all the variables are correctly initialized. 
In this example, we need to set x back to 1 before starting the second loop. 

```python
1 def count_down(start_number):
2  while (current > 0):
3    print(current)
4   current -= 1
5  print("Zero!")

count_down(3)

# Line 2: Using variable 'current' before assignment
```

The fix: 

```python
def count_down(start_number):
  current = 3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
#OUTPUT
3
2
1
Zero!
```

***

### Infinite Loops 
- the code block in the loop will continue to execute and never stop (condition being evaluated in a while loop doesn't change). 

```python
# using the modulo operator
while x%2 ==0:
    x = x/2
```

- try different values a variable can take (unexpected values, like zero).
What would happen if x was zero? 
The remainder of 0 divided by 2 is 0, and the condition would be true. 
The result of dividing 0 by 2 would also be zero, so the value of x wouldn't change. 
This loop would go on forever, and so we'd get an infinite loop.

Solution: nest this while loop inside an if statement.
so that the while loop is executed only when x is not zero

```python
if x != 0:
    while x%2-=-=0:
        x = x/2
```

Alternatively, 
* add the condition directly to the loop using a logical operator:

```python
while x != 0 and x % 2 == 0:
    x = x /2
```
We only enter the body of the loop for values of x that are both different than zero and even. 

#### the break keyword 
- to signal that the current loop should stop running. We can use it not only to stop infinite loops but also to stop a loop early if the code has already achieved what's needed. 

 ```python 
while True:
    do_something()
    if user_requested_to_stop():
        break
```

* remember to initialize your variables
* check that your loops won't run forever.
* break the loop by pressing Ctrl+C

***
