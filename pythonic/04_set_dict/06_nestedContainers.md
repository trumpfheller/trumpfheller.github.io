---
title: UCB Python - lecture - Nested containers 
layout: default
---
|| [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
|| [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
|| [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)

---

## Nested containers

* what are nested containers?
* Nested containers Examples
* Nested Container indexing
* Nested Container Iteration

### what are nested containers?

* Containers that have containers as items
* each level of nesting indicates the depth of the containers
* Matryoshka dolls

### Nested list Examples

* collection of test scores (list of lists)

```python
[[55,,60,93,28], [77,45,23,95],[23,88,62]]
```

* list of 3D coordinates (list of tuples)

```python
[(1,1,1), (10,20,10),(-10,-10,-10),(20,0,0)]
```

* list of employee records (list of dictionaries)

```python
[{'name':'James", 'hire_date':'2017/10/5'}, 
{'name':'Jana", 'hire_date':'2021/10/5'}, 
{'name':'Jae", 'hire_date':'2016/10/5'}, 
]
```

* Grocery Categories (dictionary of lists)

```python
{
    'dairy':['milk', 'cheese','yoghurt'],
    'fruit':['apple', 'banana','grapes','durian'],
    'vegetable':['carrot', 'kale','lettuce','eggplant']
}
```

the keys are the categories, and the values are lists of items

* state information (dictionary of dictionaries)

```python
{
    'CA':{'name': 'California', 'capital': 'Sacramento','area':'163696'},
    'OR':{'name': 'Oregon', 'capital': 'Salem','grapes','area':'93381'},
    'WA':{'name': 'Washington', 'capital': 'Olympia','area':'71362'}
}
```

### Nested Container indexing

* Access parts of a nested container
* Consists of a series of index operators(a,b,c)

* the left most index represent the shallowest levels
* while the rightmost indexes represent the deepest levels.
variable = [[[..]]]
variable [a][b][c]

coord = [(-2,1),(2,-1),(3,4)]

|| 0 | 1 | 2 |
| (-2,1) | (2,-1) | (3,4) |

||expression | value |
| at coord[0]  | we get the tuple (-2,1)


||expression | value |
| at coord[0]  | we get the tuple (-2,1)

||expression | value |
| at coord[0][0]  | -2
| at coord[0][1]  | 1
| at coord[1][0]  | 2
| at coord[1][1]  | -1

https://ucbx.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=19fa5338-360a-4065-8821-aeef00c648ad

```python

```

### Nested Container Iteration

* with nested containers, accessing every element requires nested iteration
* an iteration for every level of nesting
* each item is handed of the next level for further iteration

```python
scorelist = [[38,62,93], [28], [64,76]]
#a list of lists
for outer_item in scorelist:
    #the outerloop
    for inner_item in outer_item:
        #inner loop
        print(inner_item, end='')
    print()

# Output
```

first iteration of the outer loop

|| name | value |
| outer_item  | [38,62,93]
 inner_item | 38