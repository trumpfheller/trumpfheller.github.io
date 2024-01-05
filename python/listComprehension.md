---
title: List Comprehension
layout: default
---

## List with a comprehension
- incorporates the for/in iteration
- there are no tuple comprehensions, only mutables types can comprehend


### Syntax

```
[expression for item in iterable]
```

When to use a comprehension list
the normal for loop looks like this:
- to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition. - [source: docs.python.org](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)


```python
numbers = [1,2,3,4,5]
results =[]
for i in numbers:
    i = i*2
    results.append(i)

```

With comprehension it is shorter:
```python
numbers = [1,2,3,4,5]
results =[i*2 for i in numbers]
```

```python
number_list = [number for number in range (1, 6)]

> number_list

```

nums = [1,2,3]
[i*2 for i in nums]

### Example with Strings
```python

strings = ["Introduction", "to", "more", "comprehension"]

results = []
for i in strings:
    i = i.upper()
    results.append(i)

print("printing results: ", results)
```



---
> If you use the longer way, it is more readable.

```python
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)

> number_list

```
'''
RESULT

[1,2,3,4,5]
'''

```python
number_list = []
for number in range (1,6):
    number_list.append(number)

> number_list

```
OR

```python
number_list = list(range (1,6))

> number_list

```

