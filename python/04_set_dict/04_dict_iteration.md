---
title:  Python - Dictionary iteration
layout: default
---

## Dictionary iteration

* Iteration by keys
* Iteration by values
* Iteration by items
* Dictionary Comprehension

### Iteration by keys

* iterate though keys of a dict using key()
* retrieve value with the key using indexing

**Syntax**

```python
value = dictionary[key]
```

**Example1**

```python
d={'b':2,'a':1,'c':3,}
for key in d.keys():
    value=d[key]
    print(f"d['{key}']={value}")
# Output
d['b']=2
d['a']=1
d['c']=3
```

**Example2**

```python
d={'b':2,'a':1,'c':3,}
for key in sorted(d.keys()):
    value=d[key]
    print(f"d['{key}']={value}")
# Output
d['a']=1
d['b']=2
d['c']=3
```

### Iteration by values

* iterate through values using values()
* Note that because of the way dictionaries work, we cannot retrieve the key using only a dictionary's value.

**Example1**

```python
d={'b':2,'a':1,'c':3}
total = 0
for value in d.values():
    total += value
print(total)
# Output
# 6
```

### Iteration by items

* iterate though items using items() method
* items() returns an iterable of key-value tuples
  * [(key1, value1),(key2, value2),(key3, value3)]

```python
for key, value in [(key1, value1), 
                    (key2, value2), 
                    (key3, value3), ]
```

**Example**

```python
    d={'a':1,'b':2,'c':3}
    for key,value in d.items():
        print(f"d['{key}']={value}")
# Output
#   
```

* d.items returns a sequence containing tuples of key value pairs
* with tuple assignment, key is set to a and value is set to 1
key, value is set to a tuple

| expression  | value |
|:-------------|:------------------|
| key,value | ('a',1)
| d.items() | [('a':1),('b':2),('c':3)]

## WHY

* "with the tuple assignment, key is set to a and value is set to 1."
* Now why is the key in a list ['{key}'] again?

--

### Dictionary Comprehension

* like set comprehension (index expression is replaced with key-value expression)
* uses key-value pair for item expression

**Syntax**

```python
{key: vlaue for item in iterable if cond_exp}
```

(he is presenting is for the sake of completion, but he doesn't feel it is very useful per se since it complex nature)


```python
fruits=['apple', 'banana', 'cherry', 'durian']
d={fruit[0].lower(): fruite.capitalization() for fruit in fruits}
print(d)

# Output
# {'a': 'Apple', 'b':'Banana', 'c':'Cherry', 'd':'Durian'}
```
