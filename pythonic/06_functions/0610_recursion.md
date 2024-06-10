---
title: Function - Recursion
layout: default
---
> [back](./index.html)

---

[realpython](https://realpython.com/python-recursion/#why-use-recursion)

### What is a recursive function

- A function that calls itself is said to be recursive.
- Self-referential situation

### A recursive function has:

- Base Case 
  - a condition that evaluates the current input to stop the recursion from continuing.
- Recursive Step 
  - one or more calls to the recursive function to bring the input closer to the base case.

### Why Use Recursion?

- tree-like data structures (nested structures), fit a recursive definition
- Recursive implementations often consume more memory than non-recursive ones.
- might result in slower execution time.
- readability of the code will be the biggest determining factor

When you call a function in Python, the interpreter creates a new local namespace so that names defined within that function don’t collide with identical names defined elsewhere. One function can call another, and even if they both define objects with the same name, it all works out fine because those objects exist in separate namespaces.

The same holds true if multiple instances of the same function are running concurrently.

```python
def function():
    x = 10
    function()
```

When `function()` executes the first time, Python creates a namespace and assigns x the value 10 in that namespace. Then `function()` calls itself recursively. The second time function() runs, the interpreter creates a second namespace and assigns 10 to x there as well. These two instances of the name x are distinct from each another and can coexist without clashing because they are in separate namespaces.

```python
>>> function()
Traceback (most recent call last):
RecursionError: maximum recursion depth exceeded
```

The interpreter limits the maximum number of times a function can call itself recursively, and when it reaches that limit, it raises a RecursionError exception, as you see above.

 find out what Python’s recursion limit is with a function from the sys module called `getrecursionlimit()`:

```python
>>> from sys import getrecursionlimit
>>> getrecursionlimit()
1000

>>> from sys import setrecursionlimit
>>> setrecursionlimit(2000)
>>> getrecursionlimit()
2000
 ```

a function that calls itself recursively must have a plan to eventually stop:
- here are one or more base cases that are directly solvable without the need for further recursion.
- Each recursive call moves the solution progressively closer to a base case.

```python
>>> def countdown(n):
...     print(n)
...     if n == 0:
...         return             # Terminate recursion
...     else:
...         countdown(n - 1)   # Recursive call
...

>>> countdown(5)
5
4
3
2
1
0
```

* base case (when n is zero) and the recursive call.

Comparison

```python
# recursive
def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)

# non-recursive
def countdown(n):
  while n >= 0:
    print(n)
    n -= 1

>>> countdown(5)
5
4
3
2
1
0
```

```python
def countdown(value):
  call_stack = []
  while value > 0 : 
    call_stack.append({"input":value})
    print("Call Stack:",call_stack)
    value -= 1
  print("Base Case Reached")
  while len(call_stack) != 0:
    print("Popping {} from call stack".format(call_stack.pop()))
    print("Call Stack:",call_stack)
countdown(4)
'''
Call Stack: [{'input': 4}]             
Call Stack: [{'input': 4}, {'input': 3}]         
Call Stack: [{'input': 4}, {'input': 3}, {'input': 2}]     
Call Stack: [{'input': 4}, {'input': 3}, {'input': 2}, {'input': 1}]                                
Base Case Reached                                  
Popping {'input': 1} from call stack                       
Call Stack: [{'input': 4}, {'input': 3}, {'input': 2}]  
Popping {'input': 2} from call stack                   
Call Stack: [{'input': 4}, {'input': 3}]       
Popping {'input': 3} from call stack            
Call Stack: [{'input': 4}]                                 
Popping {'input': 4} from call stack              
Call Stack: []
'''
```

### Factorial n!

```python
def factorial(n):
  return 1 if n <= 1 else n * factorial(n - 1)

>>> factorial(4)
24

# non - recursive version
def factorial(n):
  return_value = 1
  for i in range(2, n + 1):
    return_value *= i
  return return_value

>>> factorial(4)
24
```

### Print the fibonacci series upto n_terms

```python
def recursive_fibonacci(n):
  if n <= 1:
    #  two base cases – when the index is zero or 1
    return n
 else:
  return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 10

# check if the number of terms is valid
if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("Fibonacci series:")
for i in range(n_terms):
  print(recursive_fibonacci(i))
```

```python
# Program to print factorial of a number
# recursively.

# Recursive function
def recursive_factorial(n):
if n == 1:
  return n
else:
  return n * recursive_factorial(n-1)

# user input
num = 6

# check if the input is valid or not
if num < 0:
  print("Invalid input ! Please enter a positive number.")
elif num == 0:
  print("Factorial of number 0 is 1")
else:
  print("Factorial of number", num, "=", recursive_factorial(num))
```

* nested list structure

```python
names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

for index, item in enumerate(names):
  print(index, item)

0 Adam
1 ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert']
2 Alex
3 ['Bea', 'Bill']
4 Ann
```

### Detect Palindromes

* reads the same backward as it does forward.

```python
"""Return True if word is a palindrome, False if not."""
def is_palindrome(word):
  return word == word[::-1]

>>> is_palindrome("foo")
False
>>> is_palindrome("racecar")
True
>>> is_palindrome("civic")
True
```

- The first character is word[0].
- The last character is word[-1].
- The substring between the first and last characters is word[1:-1].

```python
def is_palindrome(word):
  if len(word) <= 1:
    return True
  else:
    return word[0] == word[-1] and is_palindrome(word[1:-1])
```

### Sort With Quicksort

- [realpython](https://realpython.com/python-recursion/#why-use-recursion)

---

```python
def flatten(lol):
    for item in lol:
        if isinstance(item,list):
            for subitem in flatten(item):
                yield subitem
        else:
            yield item

lol = [1,2,[3,4,5], [6,[7,8,9],[]]]
flatten(lol)
[1,2,3,4,5,6,7,8,9]
```