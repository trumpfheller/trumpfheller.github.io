---
title: ggl python List methods
layout: default
---

## List methods

### Modifying Lists
* lists are mutable (we can add, remove, or modify elements in a list.) 
* strings are not mutable. 
* Changing the list means, keep the same box and add, remove, or change the elements inside that box.

| [method](https://www.w3schools.com/python/python_ref_list.asp) | what it does |  
|:-------------|:------------------| 
| list[i] = x | Replaces the element at index i with x |  
| list.append(x) | Inserts x at the end of the list |  
| list.insert(i, x) | Inserts x at index i |  
| list.remove(x) | Removes the first occurrence of x in the list | 
| list.sort(<key=None>, <reverse=False>) | Sorts the items in the list | 
| list.reverse() | Reverses the order of items of the list | 
| list.clear() | Removes all the items of the list | 
| list.copy() | Creates a copy of the list | 
| list.extend(other_list) | Appends all the elements of other_list at the end of list | 

	
<br>

**returns values - pop() method** 
* list.pop(i)
* remove elements 
* method receives an index.
* returns the element that was removed at the index that was passed.
* to change an item by assigning something else to that position 
* Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.

```python
fruits = ["Orange", "Pineapple", "Banana", "Apple"]
fruits.pop(3)
print(fruits)
["Orange", "Pineapple", "Banana"]
```

**returns values - count() method** 
```python 
li.count('b') # number of occurrences
2
```
**returns values - index() method** 
* list.index(<obj>[,<start>[, <end>]]) 
	
**returns values - count(<obj>) method** 
* list.count(<obj>) 

<br>
	

	
**append() method** 
- adding an element to a list (adds a new element at the end of the list.)
- list.append("New data") would add the string "New data" to the end of the list.
- mylist.append(<object>)

	
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
['apple', 'banana', 'cherry', 'orange']
```

	
<br>

**insert() method**
- to add an element to a list in a specific position, instead of at the end.
- two parameters: 
    - mylist.insert(<index>,<object>)an index as the first parameter 
    - element as the second parameter. 

```python
list.insert(0, "New data") 
```

- would add the string "New data" to the front of the list. 
- This wouldn't overwrite the existing element at the start of the list. 
- It would just shift all the other elements by one. 
- If you specify an index that’s larger than the length of the list, the element will simply be added to the end of the list.

```python
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0,"Orange")
print(fruits)
["Orange", "Pineapple", "Banana", "Apple", "Melon"]
```

**use a number larger than the length of the list**
```python
fruits.insert(25,"Peach")
print(fruits)
["Orange", "Pineapple", "Banana", "Apple", "Melon", "Peach"]
```

No errors. If an index higher is than the current length, the element just gets added to the end. Y
- usually, you either 
    - add at the beginning using insert() at the zero index 
    - add at the end using append(). 

```python 
fruits = ["Orange", "Pineapple", "Banana", "Kiwi","Peach"]
fruits[2] = "Strawberry"
print(fruits)
["Orange", "Pineapple", "Strawberry", "Banana", "Kiwi","Peach"]
```

**remove() method**
```python 
li.remove('b') # remove first occurrence
li
['a', 'b', 'c']
```
**sort() method**
```python 
strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs)) 
## ['BB', 'CC', 'aa', 'zz'] (case sensitive)

print(sorted(strs, reverse=True))   
## ['zz', 'aa', 'CC', 'BB']

li.sort() # sort the list *in place*
li
[2, 5, 6, 8]
```

**reverse() method**
```python 
li = [5, 2, 6, 8] #reverses the list in place (does not return it)
li.reverse() 
li
[8, 6, 2, 5]
```

**extend() method**
- adds the specified list elements (or any iterable) to the end of the current list.
- mylist.extend(<iterable>)

```python
	fruits = ['apple', 'banana', 'cherry']
	cars = ['Ford', 'BMW', 'Volvo']
	fruits.extend(cars)
	print(fruits)
	['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']
```


**slice method**
- use indexes to create a slice of the list. 

```python
# the range starts at index one and goes up to the second index minus one.

x[1:3]

# First value defaults to zero and the second value to the length of the list.

x[:2] 
```

**split() method**
- splits a string into a list.

```python
# Example 1
txt = "welcome to the wild"
x = txt.split()
print(x)

#OUTPUT
#['welcome', 'to', 'the', 'wild']
```

**replace via indexing**
you can change an element in a list
- to overwrite the value stored at the specified index. 
- to overwrite the first element in a list with the new string "Old data".
```python
    list[0] = "Old data" 
```

**remove() method**
- remove elements from the list using the value of the element we want to remove. 
- removes the first occurrence of the element from the list.
- If the element is not in the list - we get a value error ("element isn't in the list"). 
Takes an element as a parameter, and removes the first occurrence of the element. 
If the element isn’t found in the list, you’ll get a ValueError error explaining that the element was not found in the list.

```python
list.remove(elmnt)
mylist.remove(<object>)

fruits = ["Orange", "Pineapple", "Banana", "Apple"]
fruits.remove("Apple")
print(fruits)
["Orange", "Pineapple", "Banana"]
```

**same result accomplished with pop()**
```python
	fruits = ['apple', 'banana', 'cherry']
	fruits.pop(1)
	print(fruits)
	['apple', 'cherry']
```

This method differs from the remove method in that it takes an index as a parameter, and returns the element that was removed. 
This can be useful if you don't know what the value is, but you know where it’s located. 
This can also be useful when you need to access the data and also want to remove it from the list.

**Use cases**
- If the list contains hosts on a network, you could add or remove hosts as they come online or offline. 
- If the list contains users authorized to run a certain process, you could add or remove users when permissions are granted or removed and so on. 
- you'll use a list whenever you need to write a program that'll handle a variable amount of elements
- You will use whenever you need to write a programm that'll handle a sequence of a fixed amount of elements.

**reversed() method**
-  specify the sequence in a forward direction
```python
    for i in reversed(range(1, 10, 2)):
        print(i)
#OUTPUT
9
7
5
3
1
```

### Print out
```python
my_list = [1, 2, 3, 4, 5]
print(my_list)
# Output: [1, 2, 3, 4, 5]
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

**Using list comprehension**
```python
my_list = [1, 2, 3, 4, 5]
print(*my_list)
# Output
1, 2, 3, 4, 5
```

**Using the join() method**
```python
my_list = [1, 2, 3, 4, 5]
print(' '.join(map(str, my_list)))
# Output
1 2 3 4 5
```

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

**Use zip to write a for loop**
```python
```

**Zip Lists to a Dictionary**
```python
```

**Unzip Tuples**
```python
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

## List Comprehensions
- creating lists in a shorter way. 
- create new lists based on sequences or ranges.
- create a list based on a range or based on the contents of a list, a tuple, a string or any other Python sequence. 
- The syntax tries to copy how you would express these concepts with natural language. 

**Syntax** 
```
newlist = [expression for item in iterable if condition == True]
```

**Example #1**
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

=> action item more examples

#### List comprehensions and conditional clause. 
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



appending an if statement to the end of the comprehension. 
 ```python
	x for x in range(1,101) if x % 10 == 0 
```

* would generate a list containing all the integers divisible by 10 from 1 to 100. 
* if statement evaluates each value in the range from 1 to 100 to check if it’s evenly divisible by 10. 
* If it is, it gets added to the list.

List comprehensions can be powerful, but also be super complex, resulting in code that’s hard to read. 


[expression for variable in sequence] 
- Creates a new list based on the given sequence. Each element is the result of the given expression.

[expression for variable in sequence if condition] 
- Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true. 




## List-specific methods 
- [w3](www.w3schools.com/python/python_ref_list.asp)
	
***

> [Data Structure](./datastructure.html) <br>
> [Lists](./lists.html) <br>
> [List methods](./listmethods.html) <br>
> [Tuples](./tuples.html) <br>
> [Tuples methods](./tuplemethods.html) <br>
> [Dictionary](./dictionary.html) <br>
> [Dictionary methods](./dictionarymethods.html) <br>
> [back](../)

***
