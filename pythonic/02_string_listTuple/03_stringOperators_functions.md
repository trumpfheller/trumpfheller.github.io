---
title: lec_03 String Operators and Functions
layout: default
---

## String Function and Operators

### String Length function

* return the length of string (total number of characters)

```python
len(string)
```

### Comparison operator

str1 == str2 equality
str1 !== str2 non equality
str1 > str2 greater than
str1 < str2 less than
str1 >= str2 greater than or
str1 <>= str2 less than or equal

* compared character by character
* start at index 0
* Two strings are equal when they have
  * the same order of characters
  * the same number characters

### Ord Function

* return integer Unicode of character
* internally, comparison operators use the ord function

```python
ord(character)
```

### Comparison operator Example

```python
print("apple" < "banana")
print(ord("a"), ord("b"))
print("apple" < "Blueberry")
print(ord("a"), ord("B"))
# Output
True
97 98
False
97 66
```

### Concatenation operator

str1 + str2

### String Append Examples

```python
a = "UC"
b = "Berkeley"
c = a + " " +b
print(c)
# Output
UC Berkeley
```

### Membership operator

* check if substr is contained in string
* returns a boolean string

```python
substr in string
```
```python
s = "UC Berkeley"
print("Berkeley" in s)

# Output
True
```

---

||[back](../index.html)