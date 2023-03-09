---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [OOP](./oop.html) ||
> [Conditional](./c_conditional.html) || [for loop](./c_for.html)

***


### while loop
- execute a set of statements as long as a condition is true
- to continuously execute code based on the value of a condition. 
- code block can be executed multiple times instead of just once.
- performing an action over and over until a condition has changed.
- code block will keep executing as long as the evaluation 
statement is true. Once the statement is no longer true, the loop exits and the next line of code will be executed.

#### Use case
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

#### while loop inside of a function. 
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


The process continues until the result of the comparison isn't true anymore, which happens when x is bigger than n. In our current example, this would be when the value of x is 6. 
 
#### Example - to call a separate function that evaluates the condition. 

```python
username = get_username()
while not valid_username(username):
    print("invalid username")
    username = get_username()
```

 a lot of code hidden behind functions. 
#### get_username() function 
- asks the user for a username and a valid_username function that validates that username. 
- In this case, the body of the while loop will be executed until the user enters a valid username. 
The important thing to remember is that the condition used by the while loop needs to evaluate to true or false. 

rundown of some of the most common pitfalls that you may come across when writing your own loops. Head on over to the next video to get started.


If you have a loop that's gone rogue and is not behaving as expected, it's a good idea to check if all the variables are correctly initialized. 
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



#### recap 
- whenever you're writing a loop check that you're initializing all the variables you want to use before you use them. 

***

#### Infinite Loops 
- what's called an infinite loop, a loop that keeps executing and never stops. 

```python
while x%2 ==0:
    x = x/2
```
It uses the modulo operator that we saw a while back. This cycle will finish for positive and negative values of x. But what would happen if x was zero? The remainder of 0 divided by 2 is 0, so the condition would be true. The result of dividing 0 by 2 would also be zero, so the value of x wouldn't change. This loop would go on forever, and so we'd get an infinite loop. 

If our code was called with x having the value of zero, the computer would just waste resources doing a division that would never lead to the loop stopping. 

. To avoid this, we need to think about what needs to happen for a loop to be successful.

```python
if x != 0:
    while x%2-=-=0:
        x = x/2
```
 In this example, we said that x needs to be different than zero. So we could nest this while loop inside an if statement just like this. 
With this approach, the while loop is executed only when x is not zero. 

Alternatively, we could add the condition directly to the loop using a logical operator like in this example.

```python
while x != 0 and x % 2 == 0:
    x = x /2
```
This makes sure we only enter the body of the loop for values of x that are both different than zero and even. 

#### sum up
- An infinite loop means the code block in the loop will continue to execute and never stop. 
- This can happen when the condition being evaluated in a while loop doesn't change. 
- take a moment to consider the different values a variable can take - Think about unexpected values, like zero.
- the break keyword to signal that the current loop should stop running. We can use it not only to stop infinite loops but also to stop a loop early if the code has already achieved what's needed. 
First, remember to initialize your variables, and second, check that your loops won't run forever.
- break the loop by pressing Ctrl+C

 ```python 
while True:
    do_something()
    if user_requested_to_stop():
        break
```

***
