---
title: Lists
layout: default
---

## List

```python
	list = ["This", "is", "a", "list"] 
```

- are **ordered**, an ordered collection of items/objects (an **innate** characteristic of the list).
    - the items have a defined order, 
    - that order will not change.
    - lists with the same elements in a different order are not the same.
- are sequences of elements of **any type** (like complex objects)
    - Functions
    - Classes
    - Module
- may contain any number of elements/objects (constrained by the computer’s memory, of course), of any type(can store heterogeneous data types). 
- Does not to be unique: same object may occur any number of times.
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


**slice method**

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



## Zip and Enumerate
- when dealing with loops

## Zip 
```python
list(zip(['a', 'b', 'c'], [1, 2, 3])) 
# Output 
[('a', 1), ('b', 2), ('c', 3)].
```

```python
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))
    # tuple is unpacked using * in the format method

for point in points:
    print(point)

# OUTPUT
F: 23, 677, 4
J: 53, 233, 16
A: 2, 405, -6
Q: -12, 433, -42
Y: 95, 905, 3
B: 103, 376, -6
W: 14, 432, 23
X: -5, 445, -1
```


## Enumerate 
- use this when you want the index along with each element of an iterable in a loop.
- [Iterating Over Lists](https://docs.python.org/3/tutorial/datastructures.html?highlight=enumerate)
- position index and corresponding value can be retrieved at the same time.
- to access the elements in a list, along with the index of the element in question.
- takes a list as a parameter and **returns a tuple for each element in the list**. 
    - First value of the tuple is the index 
    - Second value is the element itself.

```python
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
0 tic
1 tac
2 toe

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
    0 a
1 b
2 c
3 d
4 e
```

**Use enumerate to modify the list**
```python
index = 0
for value in values:
    print(index, value)
    index += 1
# OUTPUT
0 a
1 b 
2 c

for index in range(len(values)):
    value = values[index]
    print(index, value)
# OUTPUT
0 a
1 b
2 c

fruits = ['apple', 'banana', 'orange', 'grape']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

Index: 0, Fruit: apple
Index: 1, Fruit: banana
Index: 2, Fruit: orange
Index: 3, Fruit: grape

my_list = [1, 2, 3, 4, 5]
for index, value in enumerate(my_list):
    my_list[index] = value * 2

print(my_list)
[2, 4, 6, 8, 10]
```

### Enumerate - [Iterating Over Lists](https://docs.python.org/3/tutorial/datastructures.html?highlight=enumerate)
- When looping through a sequence, the position index and corresponding value can be retrieved at the same time.
- to access the elements in a list, along with the index of the element in question.
- takes a list as a parameter and returns a tuple for each element in the list. 
The first value of the tuple is the index and the second value is the element itself.

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
0 tic
1 tac
2 toe
```

### List Comprehensions
- creating lists in a shorter way. 
- create new lists based on sequences or ranges.
-  to create a list based on a range like in this example. Or based on the contents of a list a tuple a string or any other Python sequence. 
- The syntax tries to copy how you would express these concepts with natural language. 

**Syntax** 
```
newlist = [expression for item in iterable if condition == True]
```

to create a list with multiples of 7 from 7 to 70.
```python
multiples = []
	for x in range(1,11):
	multiples.append(x*7)
print(multiples)
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
```
=> same in just one line - with list comprehension.
```python
multiples = [ x * 7 for x in range(1,11)] 
print(multiples)
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
```


**Example #2**
* a list of strings with the names of programming languages 
* generate a list of the length of the strings. 

We could iterate over the list and add them using a pen like we did before. 
```python
languages = ["Python", "Ruby", "Java", "Perl", "Go"]
lengths = [len(language) for language in languages]
print(lengths)
[6, 4, 4, 4, 2]
```
Or we could use a list comprehension like this

### List comprehensions and conditional clause. 
* all the numbers that are divisible by 3 between 0 and a 100. 

```python
z = [x for x in range(0,101) if x % 3 == 0] 
print(z)
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
```

Using list comprehensions can make the code look nicer and more readable, 
at other times it can have the opposite effect, 
especially if we try to pack too much information together. 


iterate over the range 1 to 10, and multiply each element in the range by 2. This would result in a list of the multiples of 2, from 2 to 20.
to create a new list from a sequence or a range in a single line 
[You can create lists from sequences using a for loop].

```python
	x*2 for x in range(1,11) 
```

Appending an if statement to the end of the comprehension. 
 ```python
	x for x in range(1,101) if x % 10 == 0 
```

would generate a list containing all the integers divisible by 10 from 1 to 100. The if statement we added here evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. If it is, it gets added to the list.

List comprehensions can be powerful, but also be super complex, resulting in code that’s hard to read. 



[expression for variable in sequence] Creates a new list based on the given sequence. Each element is the result of the given expression.
[expression for variable in sequence if condition] Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true. 



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




