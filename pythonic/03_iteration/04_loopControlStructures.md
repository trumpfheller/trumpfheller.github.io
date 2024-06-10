---
title: 03_ Iteration_lec_04_Loop Control Structures
layout: default
---

## Loop Control Structures

* Infinte Loops
* Break
* Continue

### Infinte Loops

* common programming idiom
* infinite Loop that executes forever
* Example: While loop set to True

```python
while True:
    codeblock
```

### Break

* exits a loop
* Example: to exit an infinite loop
* works for either a for - or a while loop
* used in conjunction with a conditional statement
  * if True, exit loop and go back to main flow
  * if False, remain in loop

```python
if boolean_exp:
    break
```

```python
string = "apple,banana,orange"

# Splitting the string using comma as separator
result = string.split(',')

print(result)  # Output: ['apple', 'banana', 'orange']
```

```python
while True:
    s = input("Enter a sentence: ")
    if len(s) == 0:
        break
    words = s.split()
    #If no separator is provided to the split(), it splits the string based on whitespace characters by default.
    print(f"{len(words)} words")
    print("done")
```

### Continue

* Skips to the next iteration without leaving the loop
* used in conjunction with a conditional statement
  * if True, go back to the top of the loop codeblock
  * If False, 


```python
if boolean_exp:
    continue
```

```python
while True:
    s = input("Enter a sentence: ")
    if len(s) == 0:
        continue
    words = s.split(
        print(f"{len(words)} words")
    print("done")
    )
```

* now I have to hit Control C to exit the infinite loop.
