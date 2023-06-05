---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
>  [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [OOP](./oop.html) ||

***

## Algorithms

### Sorting Algorithms:

### Bubble Sort
- define a function bubble_sort that takes a list as an argument. 
- The outer loop runs n times, where n is the length of the list. 
- The inner loop compares adjacent elements and swaps them if they are in the wrong order. 
- This process is repeated until the entire list is sorted. 
- Finally, we call the bubble_sort function with an example list and print the sorted list.

```python
def bubble_sort(lst):
    n = len(lst)
    
    # Traverse through all elements in the list
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Compare adjacent elements
            if lst[j] > lst[j+1]:
                # Swap elements if they are in the wrong order
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Example
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Sorted list:", my_list)
# OUTPUT
# Sorted list: [11, 12, 22, 25, 34, 64, 90]
```

### Insertion Sort
```python
```
### Selection Sort
```python
```
### Merge Sort
```python
```
### Quick Sort
```python
```

***

### Searching Algorithms

- Linear Search
```python
```

- Binary Search
```python
```
