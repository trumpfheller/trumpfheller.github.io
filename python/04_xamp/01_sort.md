---
title: Python - Examples of Application - Sorting 
layout: default
---

### Sorting Data Structures

### 1. Sorting Lists

* `sorted()` function or the `sort()` method for one-time sorting.

```python
numbers = [21, 1, 45, 78, 3, 5, 8, 2, 50, 4]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)
```

### 2. Sorting Sets

* Sets automatically handle unique elements but do not maintain any order. 
* For sorted operations, convert to a list and then sort.

```python
numbers_set = {21, 1, 45, 78, 3, 5, 8, 2, 50, 4}
sorted_numbers = sorted(numbers_set)
print("Sorted set:", sorted_numbers)
```


### 3. Sorting Dictionaries

* sort a dictionary by keys or values.

```python
numbers_dict = {21: 'a', 1: 'b', 45: 'c', 78: 'd', 3: 'e'}

# Sort by keys
sorted_by_keys = dict(sorted(numbers_dict.items()))
print("Sorted by keys:", sorted_by_keys)

# Sort by values
sorted_by_values = dict(sorted(numbers_dict.items(), key=lambda item: item[1]))
print("Sorted by values:", sorted_by_values)
```

### 4. Sorting using Heaps

```python
import heapq

# Sample list
numbers = [21, 1, 45, 78, 3, 5, 8, 2, 50, 4]

# Create an empty heap
heap = []

# Add all elements to the heap
for number in numbers:
    heapq.heappush(heap, number)

# Pop elements from the heap to get them in sorted order
sorted_numbers = [heapq.heappop(heap) for _ in range(len(heap))]

print("Sorted numbers:", sorted_numbers)
# Output
Sorted numbers: [1, 2, 3, 4, 5, 8, 21, 45, 50, 78]
```

---

### Sorting using Heaps `heapq.heapify` followed by repeated `heapq.heappop`

```python
import heapq

# Sample list
numbers = [21, 1, 45, 78, 3, 5, 8, 2, 50, 4]

# Convert the list into a heap
heapq.heapify(numbers)

# Pop elements from the heap to get them in sorted order
sorted_numbers = [heapq.heappop(numbers) for _ in range(len(numbers))]

print("Sorted numbers:", sorted_numbers)

# Output
Sorted numbers: [1, 2, 3, 4, 5, 8, 21, 45, 50, 78]
```
