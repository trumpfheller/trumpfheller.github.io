---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [while loop](./c_while.html) || [for loop](./c_for.html)
> [OOP](./oop.html) || [back](./)
***

### Conditional 

Syntax
```python
if <expression-boolean>:
    <statement>
```

```python
if x < y:                           
if x or y:                           
if x and y:                           
if 'aul' in 'grault': 
if 'quux' in ['foo', 'bar', 'baz']:
    print('yes')
```

#### Equality (equal to each other)
```python
print("cat" == "dog")
False
```
```python
print("cat" > "Cat")
# OUTPUT
True
```
=> uppercase letters are alphabetically sorted before lowercase letters.

```python
print(1<"1")
# OUTPUT
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(1<"1")
TypeError: '<' not supported between instances of 'int' and 'str'

print(1 == "1")
False
```


### if-else conditional
Syntax
```python
	if <expr>:
    		<statement(s)>
	else:
    		<statement(s)>
```

```python
if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
    ...
else:
    <statement(s)>
```

```python
def hint_username(username):
	if len(username) < 3:
		print("Invalid username")
	elif len(username) > 15:
		print("Invalid username - 15 char minimum, dude.")
		
	else:
		print("FullblownValid")

def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "negative"
  else:
    return "Zero"

print(number_group(10)) # Positive
print(number_group(0)) # Zero
print(number_group(-5)) #Should be Negative
```
#### One-Line if Statements || Ternary Operator (Short Hand If)

```python
#standard
if <expr>:
    <statement>

# shorter
if <expr>: <statement>
if <expr>: <statement_1>; <statement_2>; <statement_n>
```

### Example

```python
if 'f' in 'foo': print('1'); print('2'); print('3')
#Output
1
2
3
```
### if-else short hand
Syntax
```python 
<expr1> if <conditional_expr> else <expr2>
```

Example
```python
'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'
#OUTPUT
'no'
```
```python
>>> raining = False
>>> print("Let's go to the", 'beach' if not raining else 'library')
Let's go to the beach
>>> raining = True
>>> print("Let's go to the", 'beach' if not raining else 'library')
Let's go to the library
```
### short hand in a function
```python
def main():
	x,y = 10,8
	st = "x is less than y" if (x < y) else "x is greater than or equal to y"
	print(st)
	
if __name__ == "__main__":
	main()

#OUPUT

```

```python
if a > b:
...     m = a
... else:
...     m = b
#becomes
>>> m = a if a > b else b
```

***

#### Boolean
```python
print(10>1)
True
```
