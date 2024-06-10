0307_iterator.md

### Iterating Over Collections

- Iterators are commonly used to iterate over collections like lists, tuples, dictionaries, etc.

```python
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
```

### Iterator Protocol

- Iterators implement the iterator protocol, which consists of two methods: `__iter__()` and __next__(). The __iter__() method returns the iterator object itself, and __next__() returns the next item in the sequence.

```python
my_iter = iter(my_list)
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
```

### Built-in Iterators: 

- Python provides several built-in iterators and functions to work with iterators, such as range(), enumerate(), zip(), etc.

```python
for i in range(5):
    print(i)  # Output: 0 1 2 3 4
```


```python
for index, value in enumerate(my_list):
    print(index, value)
```