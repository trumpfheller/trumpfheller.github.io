---
title: 06
_lec_function_decoraters
layout: default
---

### Decorators

-  to modify or enhance the behavior of functions or methods without changing their code. 
- implemented using functions and the @ symbol followed by the decorator name, which is then placed above the function definition.

```python
# Decorator function definition
def uppercase_decorator(func):
    # Inner function that modifies the behavior of the original function
    def wrapper(*args, **kwargs):
        # Call the original function and convert its result to uppercase
        result = func(*args, **kwargs)
        return result.upper()
    # Return the inner function
    return wrapper

# Function decorated with the uppercase_decorator
@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"

# Calling the decorated function
print(greet("Alice"))  # Output: HELLO, ALICE!

```

- We define a decorator function uppercase_decorator that takes another function func as its argument.
- Inside the decorator function, we define an inner function wrapper that modifies the behavior of the original function by calling it and converting its result to uppercase.
- The decorator function returns the inner function wrapper.
- We decorate the greet function by placing @uppercase_decorator above its definition. This means that whenever greet is called, it will actually call uppercase_decorator(greet) and use the modified behavior defined in the wrapper function.
- When we call the decorated greet function with an argument "Alice", it prints "HELLO, ALICE!". The decorator has modified the behavior of the original greet function by converting its result to uppercase.
- used for tasks such as logging, authentication, caching