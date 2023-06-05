---
title: Tuples
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./)

***
### SEQUENCES
- **Strings** 
	- are sequences of characters 
	- are immutable. 
- **Lists** 
	- are sequences of elements of any type 
	- are mutable. 
- **Tuples** 
	- are sequences of elements of any type 
	- are immutable. (position of the element can have meaning.)
- **Tuples** and **lists** can contain elements of any data type.
	
- Methods used
    - iterating over them using **for-loops**, 
    - indexing using the **len** function to find the length of the sequence, 
    - using **plus** to concatenate two sequences and 
    - using **in** to verify if the sequence contains an element. 

- Sequences have similar properties, like 
    * being able to iterate over them using **for** loops; 
    * support **indexing**; 
    * using the **len** function to find the length of the sequence; 
    * using the **plus** operator + in order to concatenate; and 
    * using the **in** keyword to check if the sequence contains a value.

#### Common sequence operations
* len(sequence) 
    - Returns the length of the sequence
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


### Tuples 
- in parentheses (not square brackets)
- assinging a sequence of values to a variable.
- Since tuples are indexed, they can have items with the same value.

	```python
	thistuple = ("apple", "banana", "cherry", "apple", "cherry")
	print(thistuple)
```  

#### position has meaning
A lists can hold any number of elements and we can add, remove and modify their contents as much as we want, but 
there are cases when we want to make sure an element in a certain position or index refers to one specific thing and won't change.  

##### Example
we have a tuple that represents someone's full name.
- The first element of the tuple is the first-name.
- The second element is the middle initial, and 
- the third element is the last-name. 

```python
fullname = ('Grace', 'M', 'Hopper')
```

#### the return value of functions. 
- When a function returns more than one value, it's actually returning a tuple. 

```python
def convert _seconds(seconds): 
	hours = seconds // 3600
	minutes = (seconds -  hours * 3600) // 60
	remaining_seconds = seconds - hours*3600 - minutes*60	
	return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)
```
This function returns three values - it returns a tuple of three elements. 

```python
def convert _seconds(seconds): 
	hours = seconds // 3600
	minutes = (seconds -  hours * 3600) // 60
	remaining_seconds = seconds - hours*3600 - minutes*60	
	return hours, minutes, remaining_seconds
result = convert_seconds(5000)

type(result)
<class'tuples'>
print(result)
# OUTOUT
# (1,23,20)
```
The order matters: 
* The first element represents the hours, 
* the second one represents the minutes, and 
* the third represents the seconds. 

#### **unpacking**  
- Storing the elements of a tuple in separate variables is called unpacking. This allows you to take multiple returned values from a function and store each value in its own variable.
we can turn a tuple of three elements into three separate variables. 
Because the order won't change, we know what those variables present:

```python
def convert _seconds(seconds): 
	hours = seconds // 3600
	minutes = (seconds -  hours * 3600) // 60
	remaining_seconds = seconds - hours*3600 - minutes*60	
	return hours, minutes, remaining_seconds
hours, minutes, seconds = result
print(hours, minutes, seconds)
1 23 20
```

We can also do this directly when calling the function without the intermediate result variable.
```python
def convert _seconds(seconds): 
	hours = seconds // 3600
	minutes = (seconds -  hours * 3600) // 60
	remaining_seconds = seconds - hours*3600 - minutes*60	
	return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)
0 16 40
```



#### Iterating over Lists and Tuples
When we looked at for loops, we said they iterate over a sequence of elements. One of the examples we checked out was iterating over a list. 
We will make a list of animals:

```python
animals = ['Lion', 'Zebra', 'Dolphin', 'Monkey']
chars = 0
for animal in animals:
	chars += len(animal)
	print('Total characters: {}, Average length: {}'.format(chars, chars/len(animals)))
#OUTPUT
#Total characters: 22, Average length: 5.5
```
In this code, we're 
- iterating over a list of strings. 
- For each of the strings, we get its length and add it to the total amount of characters. 
- At the end we print the total and the average which we get by dividing the total by the length of the list. 

#### To see the index of an element while going through the list: 
- use the **range function** and then use indexing to access the elements at the index that range returned. 
You could use a range function and then use indexing to access the elements at the index that range just returned or 
you could just use the enumerate function. 

```python
winners = [ 'Ashley', 'Dylan', 'Reese'] 
for index, person in enumerate (winners)
	print ("{} - {}".format(index + 1, person)
1 - Ashley
2 - Dylan
3 - Reese
```

#### The **enumerate function** 
- returns a tuple for each element in the list. 
	- The first value in the tuple is the index of the element in the sequence. 
	- The second value in the tuple is the element in the sequence. 
>> examples

#### create tuples
```python
x = ('a', 'b', 'c')
x + x
# OUTPUT
('a', 'b', 'c', 'a', 'b', 'c')

2 * x
# OUTPUT
('a', 'b', 'c', 'a', 'b', 'c')
```
#### make a copy
```python

```
- Tuples can't be modified BUT if they contain any mutable objects (list, dictionary) these objects maybe be changed if they are still assigned to their own variables.

#### one-element tuples need a comma
### still 2do

#### converting between lists and tuples

