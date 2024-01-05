> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
>  [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [OOP](./oop.html) ||

***

## Types of Data Structures/Sequences 
    - container#1: Lists 
    - container#2: Tuples 
    - container#3: Sets 
    - container#4: Dictionaries

[docs](https://docs.python.org/3/tutorial/datastructures.html)


***
## Container - List
***

- are **ordered**, an ordered collection of items/objects (an **innate** characteristic of the list).
    - the items have a defined order, 
    - that order will not change.
    - lists with the same elements in a different order are not the same.
- are sequences of elements of any type (like complex objects)
    - Functions
    - Classes
    - Module
- may contain any number of elements/objects (constrained by the computer’s memory, of course), of any type(can store heterogeneous data types). 
- Does not to be unique: same object may occur any number of times.
- are **mutable**, meaning you can add, remove, or modify elements in-place.

**Common sequence operations**
* **len(sequence)** 
    - Returns the length of the sequence
* using **in** to verify if the sequence contains an element. 
* for element in sequence 
    - Iterates over each element in the sequence
* if element in sequence 
    - Checks whether the element is part of the sequence
* sequence[i] 
    - Accesses the element at index i of the sequence, starting at zero
* sequence[i:j] 
    - Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
* for index, element in enumerate(sequence) 
    - Iterates over both the indexes and the elements in the sequence at the same time
* iterating over them using **for-loops**, 
* using **plus** to concatenate two sequences

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
**Access example**
```python
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(months[-1]) # December
print(months[25]) # IndexError: list index out of range

q3 = months[6:9]
print(q3) # [ 'July', 'August', 'September']
first_half = months[:6]
print(first_half) # ['January', 'February', 'March', 'April', 'May', 'June']
second_half = months[6:]
print(second_half) # ['July', 'August', 'September', 'October', 'November', 'December']
```
***

**in OR not in**

```python
'this' in 'this is a string'
# True
5 not in [1, 2, 3, 4, 6]
# True
5 in [1, 2, 3, 4, 6]
# False

x = ["This", "is", "a", "list"]
"Today" in x
    #OUTPUT
    False
#"This" in list would return True.
```

**pop() method** 
* list.pop(i)
* remove elements 
* method receives an index.
* returns the element that was removed at the index that was passed.
* to change an item by assigning something else to that position, 

```python
fruits = ["Orange", "Pineapple", "Banana", "Apple"]
fruits.pop(3)
print(fruits)
["Orange", "Pineapple", "Banana"]
```
	
**index() method** 
* list.index(<obj>[,<start>[, <end>]])

```python 
li = ['a', 'b', 'c', 'b']
li.index('b') # index of first occurrence*
# OUTPUT
1
```

**count() method** 
* list.count(<obj>)

```python 
li.count('b') # number of occurrences
2
```

***
## Container - Tuples
***

- similar to lists but are immutable, meaning they cannot be modified once created. 
- used to represent fixed collections of related data.
	- are sequences of elements of any type 
	- are immutable.


***
## Container - Dictionaries
***

- are key-value pairs and provide a way to store and retrieve data based on a unique key. 
- also known as associative arrays or hash maps. 
- are useful for mapping one value to another and are highly efficient for data retrieval.


***
## Container - Sets
***

- unordered collections of unique elements. 
- to eliminate duplicate values or perform set operations such as union, intersection, or difference.


***

> [Data Structure](./python/datastructure.html) <br>
> [Lists](./python/lists.html) <br>
> [List methods](./python/listmethods.html) <br>
> [Tuples](./python/tuples.html) <br>
> [Dictionary](./python/dictionary.html) <br>
> [Dictionary methods](./python/dictionarymethods.html) <br>
> [back](../)

***
