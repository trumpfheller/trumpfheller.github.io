---
title: Python - File operations
layout: default
---

## File Operations

### `os.path` module

* to verify if file and or dictionary exist

1. String-Based Operations: The `os.path` module primarily works with paths represented as strings.

2. Platform Independence: It provides functions for common path-related operations like joining paths, splitting paths, getting the basename, dirname, and more. These functions are designed to work across different operating systems (Windows, Unix, macOS).

3. Legacy: `os.path` has been around for a long time and is considered part of the legacy file path handling system in Python.

```python
import os
os.path.exists('oops.txt')
# Output
# True
os.path.exists('./oops.txt')
# Output
# True
os.path.exists('.')
# Output
# True
os.path.exists('..')
# Output
# True

# Joining paths
path = os.path.join('folder', 'file.txt')

# Splitting paths
dirname, filename = os.path.split(path)

```

* single dot stands for current directory 
* double dots stand for parent directory

### `pathlib` module

1. Object-Oriented Approach: The pathlib module provides an object-oriented approach for working with paths. It represents paths as objects.

2. Rich API: It offers a rich API for path manipulation, making code more readable and expressive. Path objects have methods for various path operations.

3. Pure Path: Path objects in pathlib can represent both absolute and relative paths. They are platform-independent and provide consistent behavior across different operating systems.

4. Modern: pathlib is a more modern and preferred way of handling paths in Python, especially for new code.

```python
from pathlib import Path

# Creating a path object
path = Path('folder') / 'file.txt'

# Getting parent directory
parent_dir = path.parent
```

Key Differences:
Syntax: os.path uses string-based operations, while pathlib uses object-oriented syntax.

Object-Oriented vs. Functional: pathlib provides an object-oriented interface, making code more readable and allowing for method chaining. os.path uses functional programming style with standalone functions.

Ease of Use: pathlib is often considered more intuitive and easier to use for path manipulation, especially in modern Python code.

In summary, while both `os.path` and `pathlib` serve the purpose of working with filesystem paths,

- `pathlib` offers a more modern, object-oriented approach with a richer API, making it preferred for new development and cleaner code. 
- `os.path` is still widely used, especially in legacy codebases.

---

### `isfile()` [to check type]

wether a name refers to a file, directory, or symbolic link

```python
name='oops.txt'
os.path.isfile(name)
# Output
# True
```

### `isdir()` [to determine directory]

```python
name='oops.txt'
os.path.isdir('.')
# Output
# True
```

* `isabs()` determines wether its argument is an absolute pathname

```python
os.path.isabs(name)
# Output
# False
os.path.isabs('/big/fake/name')
# Output
# True
```

### `copy()` [for Copying]

* copying the file oops.txt to ohno.txt


```python
import shutil
shutil.copy('oops.txt, ohno.txt')
```

### `shutil.move()`[link](https://docs.python.org/3/library/shutil.html)

* copies a file and then removes the original
* will raise an exception when your destination's directory already has a file with the same name as the source.  

### `rename()` [to change file name]

```python
import os
os.rename('nm.txt','name.txt')
```

### Link with `link()` or `symlink()`

* hardlink: a file exists in one place but it can have multiple names, called links
  * link() call creates a hard link

Syntax

```python
os.link('target.txt', 'link.txt')
os.isfile('link.txt')
# Output
# True

os.islink('link.txt')
# Output
# False

```

* symbolic link stores the new name as its own file, making it possible to get both the original and new names at once
  * `symlink()` call creates a symbolic link
* `islink()` checks wehter the dile is symbolic

Syntax

```python
os.symlink(target, link)
```

```python
import os
os.symlink('/path/to/target', '/path/to/link')
```

```python
import os
is_symlink = os.path.islink('/path/to/link')

```

### `chmod()` [to change permission]

* read, write, exucute permissions
* to make a file readable

```python
os.chmod('oops.txt', 0o400)

# OR

import stat
os.chmod('oops.txt', stat.S_IRUSR)
```

### `chown()` [to change ownership]

* numeric user ID (uid)
* group ID (gid)

```python
uid = 5
gid = 22
os.chown('oops', uid,gid)
```

### `remove()` [to delete a file]

```python
import os
os.remove("oops.txt")
os.path.exists("oops.txt")
# OUTPUT
# False
```

## Dictionary Operations

* container of all files and directories => filesystem is sometimes called volume

### `mkdir()`

```python
import os
os.mkdir('poems')
os.path.exists("poems")
# OUTPUT
# True
```

### `rmdir()`

```python
os.rmdir('poems')
os.path.exists("poems")
# OUTPUT
# False
```

### `listdir()`

```python
import os
os.mkdir('poems')

#get a list of its content
os.listdir('poems')
[]

# create subdirectory
os.mkdir('poems/goethe')
os.listdir('poems')
['goethe']

# create a file in this subdirectory
fout = open('poems/goethe/faust', 'wt')
fout.write(''' Two souls, alas, are housed within my breast,
And each will wrestle for the mastery there.''')
fout.close()

os.listdir('poems/goethe')
# OUTPUT
# ['faust']
```

### `chdir()`

* going from one directory to another
```python
import os
os.chdir('poems')
os.listdir('.')
# OUTPUT
# ['faust']
```

### `globdir()` [for list matching] 

* matches file or directory names by using Unix shell rules:
* matches everything
* ? matches single character
* [abc] matches character a,b, or c
* [!abc] matches any character except a,b, or c

* getting all files or directories that beginn with f

```python
import glob
glob.glob('f*')
# OUTPUT
# ['faust']

# any two letter files
import glob
glob.glob('??')
# OUTPUT
# ['']
```

## Pathnames

* Mac uses forward slash

### `abspath()`

```python
os.path.abspath('oops.txt')
# OUTPUT
# [/usr/mike/oops.txt]
```

### `realpath()` [to get a symlink Pathname]

* expands a relative name to an absolute one

```python
os.path.abspath('oops.txt')
# Output
'/usr/mike/oops.txt'
```

### `os.path.join()` [to build a pathname]

* combine multipart pathnames pairwise with proper patch seperation character

```python
import os
my_file = os.path.join("eek", "urk")
my_file = os.path.join(my_file, "snort.txt")

> my_file
'eek/urk/snort.txt'
```

=> need to research this, no idea what this is about

### pathlib

* it is an alternative to os.path module

```python
import os

```

---

## From the exercises in the book

### List the files in current dir

```python
import os
os.listdir('.')
['bears', 'lions', 'tigers']
```

### List the files in parent dir

```python
import os
os.listdir('..')
```

### assign the string to the variabl test1, ane write test1 to a file called test.txt

```python
test1 = 'this is a test string'
outfile = open('test.txt', 'wt')
outfile.write(test1)
outfile.close

# alternitavely
with open('test.txt', 'wt') as outfile:
  outfile.write(test1)
```

* To avoid getting an error, you might want to check if the file exists before you try to delete it

```python
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```

---

> [back](./index.html)

---
