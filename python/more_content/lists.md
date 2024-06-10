---
title: Lists
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)


***

## List

```python
	list = ["This", "is", "a", "list"] 
```
> ["This", "is", "a", "list"] is called a list literal.

- are **ordered**, an ordered collection of items/objects (an **innate** characteristic of the list).
    - the items have a defined order, 
    - that order will not change.
    - lists with the same elements in a different order are not the same.
- are sequences of elements of **any type** (like complex objects)
    - Functions
    - Classes
    - Module
- may contain any number of elements/objects (constrained by the computer’s memory, of course), of any type (can store heterogeneous data types). 
- Does not have to be unique: same object may occur any number of times.
- are **mutable**, meaning you can add, remove, or modify elements in-place.


**Ordered example**
```python
[1, 2, 3, 4] == [4, 1, 3, 2]
False
a = ['spam', 'egg', 'bacon', 'tomato']
b = ['egg', 'bacon', 'tomato', 'spam']

a == b
False
a is b
False
```

> Action item
- can be nested to arbitrary depth
- dynamic


### Common list operations

**len(list)** 

```python
my_list = [1, 2, 3, 4, 5]
length = len(my_list)

print(length)  # Output: 5
print(len(my_list))  # Output: 5
```

```python
my_list = [1, 2, 3, 4, 5]
length = len(my_list)
print("Length of the list is:", length)  
# Output: Length of the list is: 5
```

```python
my_list = [1, 2, 3, 4, 5]
if len(my_list) > 0:
    print("The list is not empty")
else:
    print("The list is empty")
```

**Using a loop**
```python
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
# Output:
1
2
3
4
5
```

**Printing - Using a loop**
```python
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
# Output:
1
2
3
4
5
```

**Printing - Using list comprehension**
```python
my_list = [1, 2, 3, 4, 5]
print(*my_list)
# Output
1 2 3 4 5
print(my_list)
# OUPUT
[1, 2, 3, 4, 5]
```

**Formatting**
- oldstyle (Python2 and 3)
- new style (Python2.6 and up)
- f-string (Python3.6 and up)

**Checking the type**
```python
type(x)
<class list>
```

**keyword “in”** 
- to check if a list contains a certain element 
 * If the element is present, it will return a True boolean. 
 * If the element is not found in the list, it will return False.  
- result of this check is a Boolean, which we can use as a condition for branching or looping.
  
```python
x = ["This", "is", "a", "list"]
"Today" in x
    #OUTPUT
False
    #"This" in list would return True.
```


**Slicing**

**slice method**
- use indexes to create a slice of the list. 

```python
# the range starts at index one and goes up to the second index minus one.

x[1:3]

# First value defaults to zero and the second value to the length of the list.

x[:2] 
```

**[:]** extracts the entire sequence from start to end

```
letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
letters[:]
'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
```

**[start:]** from the start offset to the end
```
letters[20:]
'U V W X Y Z'
```

**[start:end]** from the start offset to the end offset minus 1
range starts at index 12 and goes up to the second index minus one (14).

```
letters[12:15]
'M N O'
```

**[:end]** from the beginning to the end offset minus 1
First value defaults to zero and the second value to the length of the list.
``` 
x[:2] 
```

**[start:end:step]** extracts from the start offset to the end offset minus 1 skipping characters by step

**index() method** 
```python 
li = ['a', 'b', 'c', 'b']
li.index('b') # index of first occurrence*
# OUTPUT
1
```


***

> [Data Structure](./python/datastructure.html) || 
> [Lists](./lists.html) || [List Methods](./listmethods.html) || 
> [Tuples](./tuples.html) || [Tuple Methods](./tuplemethods.html) || 
> [Dictionary](./dictionary.html) || [Dictionary Methods](./dictionarymethods.html) ||


***

#### For more info 
* [pythong.org - lists](https://docs.python.org/3/library/stdtypes.html#lists)
* [pythong.org - mutable-sequence-type](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
* [w3schools - comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)




