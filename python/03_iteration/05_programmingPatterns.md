---
title: Python - Programming Patterns
layout: default
---

## Programming Patterns

* Tranform Pattern
* Filter Pattern
* Nested Loops

### Tranform Pattern

* Change the value each item in a sequence (list, tuple, range, string) using an expression
* Input: sequence
* Processing: expression/function 
* Output: sequence of transformed values

### Tranform Example

* take a list and raise to the second power

```python
mylist = [1,2,3,4,5,6,7,8]
newlist = []
for n in mylist:
    newlist.append(n ** 2)
print(newlist)
```

### Filter Pattern

* Select items that meet specitied conditions
* Input: Sequence
* Processing: if statement
* Output: sequence subset

### Filter Pattern Example

```python
mylist = [1,2,3,4,5,6,7,8]
newlist = []
for n in mylist:
    if n% 2 == 0:
        newlist.append(n)
print(newlist)

# Output
[2,4,6,8]
```

set into an item in mylist:

* first iteration n is set to 1

### Nested Loops

* A way for combining every item in multiple sequences
* more of a construct than a direct input processing output pattern that the transform and filter a combination og every item in every sequence

* Loop inside a loop
  * an inner loop is completed for each iteration of an outer loop


* outer loop
  * inner loop
    * innerer loop body
  * outer loop body

* for each iteration of an outer loopall possible combinations or words in two sequences

```python
adjectives = ['frozen','cooked','roasted','boiled']
nouns = ['fish','veggies','chicken']

for adj in adjectives:
    # outer loop
    for noun in nouns:
        # inner loop
        print(f"{adj} {noun}", end="\t")
    print()

# Output
frozen fish frozen veggies frozen chicken
cooked fish cooked veggies cooked chicken
roasted fish roasted veggies roasted chicken
```
