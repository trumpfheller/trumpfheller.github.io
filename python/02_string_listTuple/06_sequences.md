---
title: Python Sequences
layout: default
---

## Sequences

* Containers with a sequential series of items 
* have a deterministic order (no randomness involved)  (List ? )
* support common operations, funtions and methods
* represent an ordered collection of items. 
* allow you to store and access multiple items of data in a specific order. 

### Main characteristics:

* **Order**: Items in a sequence are stored in a defined order, and you can access them by their position (index).

* **Indexing**: Elements in a sequence can be accessed using indexing. Indexing starts at 0 for the first element, 1 for the second element, and so on.

* **Slicing**: Sequences support slicing, which allows you to access a subset of the sequence by specifying a range of indices.

* **Iterability**: Sequences can be iterated over using loops (e.g., for loop).

* **Immutability or Mutability**: Depending on the specific sequence type, sequences can be mutable (modifiable after creation) or immutable (cannot be changed after creation).

> | Sequence  | Mutable  |
|:---:|:---:|
|  List |  YES  |
|  Tuple |  NO  |
|  String |  NO  |
|  Range |  NO  |

Set and Dictionaries => no sequences.

---

* Sequences Equality and Inequality Operators

```python
seq1 == seq2
# check if same content
seq1 != seq2
# check if not have same content
```

* Sequences Index Operator

```python
sequence[n]
# return nth item in sequence
sequence[start:stop]
# return slice with items between index start and stop (excusive) in sequence
```

* Sequences Membership Operator

```python
item in sequence
# check if an item exists in sequence
```

* Sequence Concatenate Operator

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
# return a list with items sorted in ascending order 
# if reverse is True, sort in descending

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

---

> [back](../)
