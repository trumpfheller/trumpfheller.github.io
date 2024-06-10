---
title: 03_ Iteration_lec_03_Range
layout: default
---

### Iterating by Counting

* A common task in programming
* Used with loops
  * iterate a specified number of times
  * accessing indexes
  * creating a sequence of numbers

```python
# initialize counter
i=0

# Loop until counter reaches 10
while i < 10:
    print(i, end='')
    # single quote replaces the default of new lines 
    # => output in one line

    # Increment counter
    i = i+1
```

### What is a Range?

* Generated, `immutable` sequence (string and tubple) of integers
* Inherits sequence functions, methods and operators

```python
range(stop)
# genrates a range of integers starting with 0 and ending with stop(exclusive)
```

### Range examples

```python
# Iterate through numbers from 0 to 9
for i in range(10):
    # no need to initialize (i) since
    # when you use a for loop with the range(), the loop automatically initializes the loop variable (i) for you.
    print(i, end=' ')
# Output

```

### Range function

```python
range(start, stop, step=1)
# generates a range of intefers stareting with staert and ending with stop(explusive), step is an optional and defaults to 1
```

### Range Step Example

```python
r = range(20, 50, 5)
print(r)
# Output
range(20, 50, 5)

# convert it to a list
r = range(20, 50, 5)
print(list(r))
# Output
[20,25,30,35,40,45]
```

### Negative Range Example

```python
r = range(10,0)
print(list(r))
```
