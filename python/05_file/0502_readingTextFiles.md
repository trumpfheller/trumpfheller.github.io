---
title: Python -  Reading Text Files 
layout: default
---

## Reading Text Files

* File Objects
* Context manager
* Read method
* Readlines Method
* File object iterator

Syntax

```text
fileopbj = open(filename, mode)
```

* fileopbj is the fileopbject returned by open()
* filename is the string name of the file
* mode is a string indicating the file's type and what you want to do with it

| mode | operation | 
|---|---|---
| 'r' | read |  
| 'w' | write |  
| 'a' | append |  
| 'x' | write but only if it doesn exists |
| 't' | text |
| 'b' | binary |

* "x" - Create - will create a file, returns an error if the file exist
* 'w' - Create a new file if it does not exist:

### File Objects

* provide acces to a file
* have read and write methods
* have a filepointer
  * is like an indiex, it tells us position in the data while reading or writing

#### open() function

You need to cal the open() before you:

* read an existing file
* write a new file
* append to an exiting file
* overwrite an exiting file

Syntax

```text
open(filename, mode='r')
```

* return a file object from filename
* made sets the file type and either read or write mode
* default mode is read mode

| operation | mode | 
|---|---|---
| 'r' | read |  
| 'w' | write |  
| 'a' | append |  

'a' "a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content

#### Write a Textfile with print()

```python
fout = open(oops.txt, 'wt')
print('Oops, I created a file.', file=fout)
fout.close()
```

#### Using file argument to print

without the file argument to print, print just writes to standard output > terminal.
[unless you have told the shell program to redirect output to a file with > or piped it to another program with | ]

#### Write a Textfile with write()

```python
poem = '''There was a yong lady named Bright, 
Whose pseed was faster then light;'''

fout = open('speed', 'wt')
fout.write(poem)
# Output
fout.close()
```

Write() returns the number od bytes written. It does not add any spaces or newlines, as print does.
To make print() work like write(), you pass the arguments sep - called seperator (' ') and end called end string (\n)

* you can print a multiline string to a text file

```python
poem = '''There was a yong lady named Bright, 
Whose pseed was faster then light;'''

fout = open('speed', 'wt')
print(poem, file=fout)
# print(poem, file=fout sep'', end='')
fout.close()
```

```python
try:
  fout = open('relativity', 'xt')
  fout.write('stomp, stromp, stomp')
excpt FileExistsError:
  print("relativity already exists. overriding prevented")
```

#### Getting a File Object (read mode)

```python
f = open(filename, mode='r')
file_access_codeblock
f.close()
```

closing the file object releases resources

### Context manager

* prefered way to work with file objects
* idiomatic way to access files
* it does the same thing but it makes the code clear.
* Automatically closes file object

Syntax

```text
with open(filename, 'r') as f:
    file_access_codeblock
```

* with keyword indicates the start of a contect manager
* open() function
* as keyword think of it as a assignment operator but reversed

### Read method

Syntax

```text
f.read()
```

Example1

```python
f = open("demofile.txt", "r")
print(f.read())
```

Example2

```python
fin = open("relativity", "rt")
poem = fin.read()
fin.close()
```

* slurp up the entire file at once 
* read from f and return its entire contents as a string

```python
with open('lines.txt', 'r') as f: 
    contents = f.read()
    print(contents)
```

* The read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
* Now read 100 characters at a time and append each chunk to a poem string

```python
poem = ''
fin = open("relativity", "rt")
chunk = 100
while True: 
  fragment = fin.read(chunk)
  if not fragment: 
    break
  poem += fragment
fin.close()
len(poem)
# Output
# # 150)
```

### Readlines Method

* reading a line at a time

Syntax

```text
f.readlines()
```

* read from f and return its entire contents as a list of strings
* each string is delimited by a newline(inclusive)
* file pointer moves to the end of the file

```python
with open('lines.txt', 'r') as f: 
    lines = f.readlines()
    print(lines)
    # Output
    # ['On your marks.\n', 'Get set.\n'.'Go!\n']
``` 

#### Write a Test File with write()

* just like print 

### File object iterator

* Files objects are also iterators
  * file is read line by line, and not all at once
  * at each iteration a string is returned
  * String contents start from the file pointer up to and including a newline
  * filepointer is placed after the end of the new line ready for the next read operation.

### File object iterator Example  

```python
# using the file object as an iterator
with open('lines.txt', 'r') as f: 
    for line in f:
        # we iterate though the file object using a for loop
        # each iteration the variable line will be set to a line from lines.txt
        print(line, end='')
        # file pointer has moved to a next line.
```
=> page 263


## From the book [O'Reilly, Introducing Python]

### flat files

* read form a file into memory and write from memory to the file.

---

  || [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
|| [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
|| [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)

---
