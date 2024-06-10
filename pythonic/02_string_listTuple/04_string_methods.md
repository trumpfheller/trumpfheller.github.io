---
title: lec_04 String Methods
layout: default
---

||[back](../index.html)

## String Methods

* Comparison Methods
* Search Methods
* Replacement Method
* Strip Method
* Validation Methods
* Case Conversion

### Comparison Methods

```python
s.startswith(substr)
# check if s starts with substr (as an argument)

s.endswith(substr)
# check if s ends with substr
```

### Comparison Methods Example

```python
s = "UC Berkeley"
print(s.startswith("UC"))
print(s.endswith("LEY"))
# Output
True
False
```

### Search Methods

```python
s.index(substr)
# return the index of substr in s, valueError when not found
s.count(substr)
# return the number of times substr appears in s
```

### Search Methods Examples

```python
s = "UC Berkeley"
print(s.index("Berkeley"))
print(s.index("a"))
# Output
3
ValueError: substring not found

# orrurrences of the substring e
print(s.count("e"))
# Output
3
```

### Replacement Method

* retun a string with substring old replaced with new in s

```python
s.replace(old,new)
```

```python
print(s.replace("UC", "University of California, "))
# Output
University of California, Berkeley
```

### Strip Method

* return a string without leading and trailing whitepsaces (extraneous characters) in s

```python
s.strip()
```

### Strip Method Example

```python
s = " UC Berkeley    \n"
print("*" + s + "*")
print("*" + s.strip() + "*")
# Output
* UC Berkeley
* 
*UC Berkeley*
```

### Validation Methods

* Check the compistion of a string anreturn a Boolean calue
* There are two categories: 
  * character validation
  * Case validation

```python
s.isalnum()
# check if a s is all aphanumeric

s.isalpha()
# check if a s is all aphabetic

s.isdigit()
# check if a s is all numeric

s.isspace()
# check if a s is all white spaces
```

### Validation Methods Examples

```python
s = "UC"
print(s.isalpha())
# Output
True

s.isalnum()
# Output
True

s.isdigit()
# Output
True

s.isspace()
# Output
True
```

### Case Validation Method

```python
s.isupper()
# check if a s is all uppercase
s.islower()
# check if a s is all lowercase

s = "UC"
print(s.isupper())
# Output
True
```

### Case Conversion Methods

* Convert characters into different cases
* Return a bew string and does not modify the existing string

```python
s.upper()
# returns s in all uppercase
s.lower()
# returns s in all lowercase
s.capitalized()
# returns s in capitalized format
```

### Case Conversion Method

```python
print("UC Berkeley".upper())
print("UC Berkeley".lower())
print("UC Berkeley".capitalized())
# Output
UC BERKELEY
uc berkeley
Uc berkeley
```
