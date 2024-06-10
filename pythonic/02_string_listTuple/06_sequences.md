---
title: lec_06 Sequences
layout: default
---

 ||[back](../index.html)

## Sequences

* Containers with a sequential series of items 
* Have a deterministic order (no randomness involved) =>>? List ? 
* Support common operations, funtions and methods

### Sequence Types

|   | Sequence  | Mutable  |
|:---|---|---|
|  List | YES  | YES  |
|  tuple | YES  | NO  |
|  String | YES  | NO  |
|  Range | YES  | NO  |
|  Set | NO | YES  |
| Dict  |  NO | YES  |

### Sequences Equality and Inequality Operators
```python
seq1 == seq2
# check if same content
seq1 != seq2
# check if not have same content
```

### Sequences Index Operator

```python
sequence[n]
# return nth item in sequence
sequence[start:stop]
# return slice with items between index start and stop (excusive) in sequence
```

### Sequences Membership Operator

```python
item in sequence
# check if an item exists in sequence
```

### Sequence Concatenate Operator

```python
sequence1 + sequence2
# must be of the same type
```

### Sequence Functions

```python
len(sequence)
# return length

max(sequence)
# return largest value

min(sequence)
# return the smallerst value

sorted(sequence, reverse=False)
# return a list with items sorted in ascending order if reverse is True, sort in descending

reversed(sequence)
# return a copy of a sequence in reverse order
```

### Sequence Methods

```python
sequence.count(item)
# return the number of times item occurs in sequence

sequence.index(item)
# return the index of item in sequence, ValueError if not found
```
