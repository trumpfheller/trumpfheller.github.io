---
layout: default
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [OOP](./oop.html) || [Algorithm](./algorithm.html) ||[Data Structure](./datastructure.html) ||[back](./index.html)


***

## Handling Exceptions || file and exception

<dl>
<dt>The try block</dt>
<dd> lets you test a block of code for errors.</dd>
<dt>The except block</dt>
<dd> lets you handle the error.</dd>
<dt>The else block</dt>
<dd> lets you execute code when there is no error.</dd>
<dt>The finally block</dt>
<dd> lets you execute code, regardless of the result of the try- and except blocks.</dd>
</dl>

Example
- open a file without write permission
```python
# 
try:
   fh = open("testfile", "r")
   fh.write("My test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
```

```python
try:
   fh = open("testfile", "w")
   try:
      fh.write("My test file for exception handling!!")
   finally:
      print "Going to close the file"
      fh.close()
except IOError:
   print "Error: can\'t find file or read data"
```

## Handling Exceptions || def/program and exception

```python
try:
    value = int(input("Enter a number between 1 and 10: "))
    #try block handles exceptions (getting input from the user)
except ValueError:
    # except block looks for a specific exception: ValueError.
    print("You must type a number between 1 and 10!") 
else:
    #else block - executed when try block doesn’t generate an exception (is successful). 
    if (Value > 0) and (Value <= 10): 
        print("You entered: ", value)
    else:
        print("Wait, wat? You entered the wrong digits!")
```

```python
try:
    Value1 = int(input("Type the first number: ")) 
    Value2 = int(input("Type the second number: ")) 
    Output = Value1 / Value2
except ValueError:
    print("You must type a whole number!")
except KeyboardInterrupt: 
    print("You pressed Ctrl+C!")
except ArithmeticError:
    print("An undefined math error occurred.")
except ZeroDivisionError: 
    print("Attempted to divide by zero!")
else:
    print(Output)
```

## for more visuality - maybe I should put it in a def and doc string?
