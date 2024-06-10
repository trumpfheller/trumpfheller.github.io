
- It can take any number of arguments, but can only have one expression. 
- Lambda functions are often used when you need a simple function for a short period of time and don't want to define a full-fledged function using the def keyword.

### Syntax 

```python
lambda arguments: expression
```


### Example 1: 
- Adding two numbers using a lambda function

```python
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

```

### Example 2: 
- Squaring a number using a lambda function

```python
square = lambda x: x ** 2
print(square(4))  # Output: 16
```


### Example 3: 
- Checking if a number is even using a lambda function

```python
is_even = lambda x: x % 2 == 0
print(is_even(7))  # Output: False
print(is_even(10)) # Output: True
```


```python
def edit_story(words, func):
	for word in words: 
		print(func(word))

stairs = ['thud', 'meow', 'thud', 'hiss', ]

def enliven(word):
	 # enhance prose
	 return word.capitalized() + '!'
edit_story(stairs, enliven)

edit_story(stairs, lambda word: word.capitalized() + '!')
```