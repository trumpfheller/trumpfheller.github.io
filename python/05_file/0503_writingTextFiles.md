---
title:  Python -  Writing Text Files 
layout: default
---

## Writing Text Files

* Getting a File object 
* Write Mothod
* Write Mothod Example
* Writelines Method
* Writelines Example

### Getting a File object 

* Get a file object with:
  * a filename of filepath
  * write mode ('w')

```text
with open(filename, 'w') as f:
```

### Write Method

Syntax

```text
f.write(s)
```

* passing/write a string s to f

### Write Mothod Example

```python
with open('out.txt', 'w') as f: 
    f.write("Hello, world!")
    f.write("Good morning!\n")
    f.write("Good night!\n")
```

### Writelines Method

Syntax

```text
f.writelines(sequence)
```

* is the counterpart to readlines.
* write each item in a sequence as a string to f
* it accepts a sequence and write each item as a string to a file object

## Writelines Example

* we want to wrote 5 lines to a file called out.txt

```python
with open('out.txt', 'w') as f: 
    lines = [f'line{n}' for n in range(1,6)]
    # list comprehension to generate a list with string items: each item will be the string line 1 to line 5
    f.writelines(lines)
    # there is no new line character, therefore all in one line
```

```python
with open('out.txt', 'w') as f: 
    lines = [f'line{n}\n' for n in range(1,6)]
    f.writelines(lines)
```

---

|| [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
|| [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
|| [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)

---
