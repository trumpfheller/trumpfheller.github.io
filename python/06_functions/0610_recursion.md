---
title: Function - Recursion
layout: default
---

## recursive function
> Self-referential situation: a function that calls itself.
> [realpython](https://realpython.com/python-recursion/#why-use-recursion)

### A recursive function has:

- a Base Case 
  - a condition that evaluates the current input to stop the recursion from continuing.
- a Recursive Step 
  - one or more calls to the recursive function to bring the input closer to the base case.

### Why Use Recursion?

- tree-like data structures (nested structures), fit a recursive definition
- Recursive implementations often **consume more memory** than non-recursive ones.
- might result in slower execution time.
- **readability** of the code will be the biggest determining factor

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

A function that calls itself recursively must have a plan to eventually stop:
- Each recursive call moves the solution progressively closer to a base case.

```python
>>> def countdown(n):
...     print(n)
...     if n == 0:
...         return             # Terminate recursion
...     else:
...         countdown(n - 1)   # Recursive call
...
```

```text
>>> countdown(5)
5
4
3
2
1
0
```

> at the end I have a test running for this.

* base case (when n is zero) and the recursive call.

in comparison

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

---

### For testing

Recursion I want to test.

```python
>>> def countdown(n):
...     print(n)
...     if n == 0:
...         return             # Terminate recursion
...     else:
...         countdown(n - 1)   # Recursive call
...
```

```text
>>> countdown(5)
5
4
3
2
1
0
```

* Side Effects:
  * countdown primarily uses print to display values.
  * Testing frameworks typically assert on return values or specific conditions, making it hard to verify what's being printed.
* Recursion:
  * The recursive nature adds another layer of complexity.
  * Assertions within the function itself wouldn't easily capture the entire output.

```python
import io
import sys
import unittest

class TestCountdown(unittest.TestCase):
    def test_countdown(self):
        # Capture standard output
        stdout_capture = io.StringIO()
        sys.stdout = stdout_capture

        # Call the function
        countdown(3)

        # Restore standard output
        sys.stdout = sys.__stdout__

        # Get the captured output and assert
        output = stdout_capture.getvalue().strip()
        expected_output = "3\n2\n1\n0"  # Expected output
        self.assertEqual(output, expected_output)
```

### mocking the print function

* gives you finer control over verifying the calls to print. If a function relies heavily on printing or other external effects, you'll need techniques to capture and assert on those actions.
* It is possible to use mocking libraries like `unittest.mock` or `pytest.mock` to replace the print function with a custom function that records the calls:

```python
import unittest
from unittest.mock import patch

class TestCountdown(unittest.TestCase):
    @patch('sys.stdout.write')
    def test_countdown(self, mock_print):
        # Call the function
        countdown(3)

        # Assert that print was called with the expected values
        mock_print.assert_has_calls([
            unittest.mock.call('3\n'),
            unittest.mock.call('2\n'),
            unittest.mock.call('1\n'),
            unittest.mock.call('0\n')
        ])
```

### Refactoring for Testability
> design code with testability in mind: Instead of relying on print, modify countdown to return a list of numbers, making it easier to assert on the result
> it is crucial to write tests that cover various scenarios (e.g., positive numbers, zero, potentially even negative numbers if your function allows it).

```python
def countdown(n):
    result = []  # Collect the numbers in a list
    result.append(n)  # Add current number
    if n == 0:
        return result  # Return the list
    else:
        return result + countdown(n - 1)  # Combine lists
```

* now use standard `assertEqual` assertions in the tests.

```python
  import unittest

class TestCountdown(unittest.TestCase):

    def test_countdown_positive(self):
        expected_result = [3, 2, 1, 0]
        actual_result = countdown(3)
        self.assertEqual(actual_result, expected_result)

    def test_countdown_zero(self):
        expected_result = [0]
        actual_result = countdown(0)
        self.assertEqual(actual_result, expected_result)
```

* assertEqual Assertion:
  * The core of each test method uses `self.assertEqual(actual_result, expected_result)`. This compares the output of your function (actual_result) to `expected_result`.
 

### Test-Driven Development 
> for the countdown function

```python
import unittest

class TestCountdown(unittest.TestCase):

    def test_countdown_positive(self):
        # This test will fail initially, as the function doesn't exist yet
        self.assertEqual(countdown(3), [3, 2, 1, 0]) 

    def test_countdown_zero(self):
        # This test will also fail initially
        self.assertEqual(countdown(0), [0])

# No implementation of countdown() yet!
```

### Simplest Code to Pass the Tests

```python
def countdown(n):
    # Minimal implementation to pass the first test
    if n == 3:
        return [3, 2, 1, 0]
    elif n == 0:
        return [0]
```

### Refactor and Expand for Full Coverage

```python
def countdown(n):
    result = []
    result.append(n)
    if n == 0:
        return result
    else:
        return result + countdown(n - 1)
```

* Red-Green-Refactor: TDD follows a cycle of writing a test (Red), implementing code to make it pass (Green), and then refactoring to improve the code without breaking the tests (Refactor).
* Small Steps: Write and pass tests incrementally, focusing on small, specific behaviors.
* Design for Testability: TDD often encourages design code in ways that make it easier to test.
