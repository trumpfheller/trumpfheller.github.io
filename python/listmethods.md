---
title: ggl python List methods
layout: default
---

## List methods

### Modifying Lists
* lists are mutable (we can add, remove, or modify elements in a list.) 
* strings are not mutable. 
* Changing the list means we keep the same box and we add, remove, or change the elements inside that box.

| method | returns values |  
|:-------------|:------------------| 
| list.pop(i) | Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed. | 
| list.index(<obj>[,<start>[, <end>]]) | . | 
| list.count(<obj>) | . | 
| list.copy() | . | 

<br>
**pop() method** 
* remove elements 
* method receives an index.
* pop method returns the element that was removed at the index that was passed.
* to change an item by assigning something else to that position, 

```python
fruits = ["Orange", "Pineapple", "Banana", "Apple"]
fruits.pop(3)
print(fruits)
["Orange", "Pineapple", "Banana"]
```

**count() method** 
```python 
li.count('b') # number of occurrences
2
```

| method | what it does |  
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


## List-specific methods 
- [w3](www.w3schools.com/python/python_ref_list.asp)
	
***

> [Data Structure](./datastructure.html) <br>
> [Data Structure_](./datastructure00.html) <br>
> [Lists](./lists.html) <br>
> [List methods](./listmethods.html) <br>
> [Tuples](./tuples.html) <br>
> [Tuples methods](./tuplemethods.html) <br>
> [Dictionary](./dictionary.html) <br>
> [Dictionary methods](./dictionarymethods.html) <br>
> [back](../)

***
