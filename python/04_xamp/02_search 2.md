---
title: Python - Examples of Application - Search 
layout: default
---

## Examples - Search 

1. Searching in a List

```python
numbers = [21, 1, 45, 78, 3, 5, 8, 2, 50, 4]

# Element to search for
element = 45

# Check if element is in the list
if element in numbers:
    print(f"{element} is in the list at index {numbers.index(element)}")
else:
    print(f"{element} is not in the list")
```

2. Searching in a Set

```python
numbers_set = {21, 1, 45, 78, 3, 5, 8, 2, 50, 4}

# Element to search for
element = 45

# Check if element is in the set
if element in numbers_set:
    print(f"{element} is in the set")
else:
    print(f"{element} is not in the set")
```

3. Searching in a Dictionary

```python
numbers_dict = {21: 'a', 1: 'b', 45: 'c', 78: 'd', 3: 'e'}

# Key to search for
key = 45

# Check if key is in the dictionary
if key in numbers_dict:
    print(f"Key {key} is in the dictionary with value {numbers_dict[key]}")
else:
    print(f"Key {key} is not in the dictionary")
```

4. Searching in a Min-Heap (Using heapq)

* Searching for an element in a heap is less straightforward since heaps are designed for efficient access to the smallest element. You would need to check the presence of an element linearly.

```python
import heapq

# Sample list and convert it to a heap
numbers = [21, 1, 45, 78, 3, 5, 8, 2, 50, 4]
heapq.heapify(numbers)

# Element to search for
element = 45

# Check if element is in the heap
if element in numbers:
    print(f"{element} is in the heap")
else:
    print(f"{element} is not in the heap")
```

5. Searching in a Tuple

```python
numbers_tuple = (21, 1, 45, 78, 3, 5, 8, 2, 50, 4)

# Element to search for
element = 45

# Check if element is in the tuple
if element in numbers_tuple:
    print(f"{element} is in the tuple at index {numbers_tuple.index(element)}")
else:
    print(f"{element} is not in the tuple")
```

Summary of Search Methods
Lists: Use in operator or index() method.
Sets: Use in operator (very efficient due to hash table implementation).
Dictionaries: Use in operator for keys.
Heaps: Use in operator (no efficient way to directly search; must check linearly).
Tuples: Use in operator or index() method.

Example 

```python
# List example
numbers_list = [21, 1, 45, 78, 3, 5, 8, 2, 50, 4]
print(f"List: {45 in numbers_list}")

# Set example
numbers_set = {21, 1, 45, 78, 3, 5, 8, 2, 50, 4}
print(f"Set: {45 in numbers_set}")

# Dictionary example
numbers_dict = {21: 'a', 1: 'b', 45: 'c', 78: 'd', 3: 'e'}
print(f"Dictionary: {45 in numbers_dict}")

# Heap example
import heapq
heap = [21, 1, 45, 78, 3, 5, 8, 2, 50, 4]
heapq.heapify(heap)
print(f"Heap: {45 in heap}")

# Tuple example
numbers_tuple = (21, 1, 45, 78, 3, 5, 8, 2, 50, 4)
print(f"Tuple: {45 in numbers_tuple}")
```
