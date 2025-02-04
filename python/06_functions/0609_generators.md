---
title: Python || function_generators
layout: default
---

## Generators 

- Generators are particularly useful when dealing with large datasets or when you need to generate values on-the-fly without storing them all in memory at once. 
- A generator is an iterator produced by a generator function.
_ It represents a sequence of values that are lazily evaluated and generated on-the-fly.
- Generators can be iterated over using a for loop or by calling next() on them.
- Unlike regular functions, generator functions don't return a single value and exit; they yield values one at a time as requested.
- Generators are particularly useful for generating large datasets or infinite sequences without requiring a lot of memory.

```python
sum(range(1,101))
```

### generators functions

- A generator function is a special type of function in Python that uses the yield keyword instead of return to return values one at a time. 
- When a generator function is called, it returns a generator object, which can be iterated over to produce values.
- A generator function is a special type of function in Python that uses the yield keyword instead of return.
- When called, a generator function returns a generator object, which is an iterator.
- Generator functions are defined using the def keyword, just like regular functions.
- They can yield multiple values over time, and execution of the function is paused and resumed between yields.
- Generator functions are typically used to create custom iterators in a concise and memory-efficient way.

```python
# Generator function to generate squares of numbers up to n
def square_generator(n):
    for i in range(n):
        yield i ** 2

# Using the generator function
gen = square_generator(5)

# Iterating over the generator to get the squares of numbers up to 5
for square in gen:
    print(square)

# Output:
# 0
# 1
# 4
# 9
# 16

```


### iterate over a generator object

```python
def my_range(first=8, last=10 step=1):
	number = first
	while number < last: 
		yield number
		number += step
```



### generator comprehension (aka generator expression)

- provide a concise way to create generators in Python. 
- They are similar to list comprehensions, but instead of creating a list, they create a generator object that yields values lazily.

```python
# List comprehension to create a list of squares of numbers up to 5
squares_list = [i ** 2 for i in range(5)]
print(squares_list)  # Output: [0, 1, 4, 9, 16]

# Generator comprehension to create a generator of squares of numbers up to 5
squares_generator = (i ** 2 for i in range(5))
print(squares_generator)  # Output: <generator object <genexpr> at 0x7f75a7f086d0>

# Iterating over the generator to get the squares of numbers up to 5
for square in squares_generator:
    print(square)

# Output:
# 0
# 1
# 4
# 9
# 16

```

- The list comprehension [i ** 2 for i in range(5)] creates a list containing the squares of numbers from 0 to 4.
- The generator comprehension (i ** 2 for i in range(5)) creates a generator object that lazily yields the squares of numbers from 0 to 4.
- When printed, the generator object is shown as <generator object <genexpr> at ...>.
- We can iterate over the generator object using a for loop to obtain each square value. 
- The generator lazily generates the next square value only when requested, resulting in memory-efficient code.
