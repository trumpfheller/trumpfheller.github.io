---
title: Python - String Indexing and Slicing
layout: default
---

## String Indexing and Slicing

### String Indexing

* Examining parts of a string is a common operation
* Each character is a sting is referred to by an be index
  * 0 refers to the first character
  * length of the string minus 1 refers to the last character

### Index operator

* consists of square brakets

**Syntax**

```python
    string[index]
```

* return the item in string at index

s = "UC Berkeley"

Index         0   1   2     3   4   5   6   7   8   9   10
Character     U   C         B   e   r   k   e   l   e   y

### Negative Indexes

* Indexes can also be negative
  * -1 (last character)
  * -len(s) (first character)
  * -len(s) + n (nth positive index)
  A generatlized formula to convert positive indexes

### Negative Indexes Example

s = "UC Berkeley"

Index         -11   -10  -9   -8   -7   -6   -5   -4   -3   -2   -1
Character     U     C          B   e    r    k    e    k    e    y

### String slicing

* A range or substring of characters
* a Slice has two indexes:
  * start index - beginning of a slice
  * stop index - the end of a slice (exclusive)
    * character under the stop index itself is excluded

s = "UC Berkeley"

Index         0   1   2     3   4   5   6   7   8   9   10
Character     U   C         B   e   r   k   e   k   e   y

```python
s[3:11]
#Output
Berkeley
```

### Index operator (Slice) 

```python
string[start:stop]
```

* return the slice of string starting at index start and ending at index stop(exclusive)

### Default Slice Values Examples

* stop index

```python
s[:stop]
# equivalent
s[0:stop]
```

* Default Slice Example

```python
s = "University of California"
print(s[0:10])
print(s[:10])
# Output
University
University
```

### Default Slice Values 

```python
s[start:]
# equivalent
s[start:len(s)]
# stop index of the length of s
```

* Slice Default Example

```python
s = "University of California"
print(s[11:len(s)])
print(s[11:])
# Output
of California
of California
```
