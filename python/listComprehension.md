---
title: List Comprehension
layout: default
---

## List with a comprehension
- creating lists in a shorter way. 
- create new lists based on sequences or ranges.
- create a list based on a range or based on the contents of a list, a tuple, a string or any other Python sequence. 
- The syntax tries to copy how you would express these concepts with natural language. 

**Syntax** 

```
[expression for item in iterable]
```

```
newlist = [expression for item in iterable if condition == True]
```
- incorporates the for/in iteration
- there are no tuple comprehensions, only mutables types can comprehend



When to use a comprehension list
the normal for loop looks like this:
- to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition. - [source: docs.python.org](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)


```python
numbers = [1,2,3,4,5]
results =[]
for i in numbers:
    i = i*2
    results.append(i)

```

With comprehension it is shorter:
```python
numbers = [1,2,3,4,5]
results =[i*2 for i in numbers]
```

```python
number_list = [number for number in range (1, 6)]

> number_list

```

nums = [1,2,3]
[i*2 for i in nums]

### Example with Strings
```python

strings = ["Introduction", "to", "more", "comprehension"]

results = []
for i in strings:
    i = i.upper()
    results.append(i)

print("printing results: ", results)
```



---
> If you use the longer way, it is more readable.

```python
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)

> number_list

```
'''
RESULT

[1,2,3,4,5]
'''

```python
number_list = []
for number in range (1,6):
    number_list.append(number)

> number_list

```
OR

```python
number_list = list(range (1,6))

> number_list

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


