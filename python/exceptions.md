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

- this will save an IndexError exception in the variable err
- any other exceptoion in the variable other
  

```python
short_list = [1,2,3]
while True:
   value = input('Position [q to quit]?')
   if value == 'q':
      break
   try:
      position = int(value)
      print(short_list[position])
   except IndexError as err:
      print('Bad Index', position)
   except Exception as other:
      print('Something else broke: ', other)
```
## for more visuality - maybe I should put it in a def and doc string?


|| Exception | Description |
 | ArithmeticError | Raised when an error occurs in numeric calculations
 | AssertionError	Raised when an assert statement fails
 | AttributeError	Raised when attribute reference or assignment fails
 | Exception	Base class for all exceptions
 | EOFError	Raised when the input() method hits an "end of file" condition (EOF)
 | FloatingPointError	Raised when a floating point calculation fails
 | GeneratorExit	Raised when a generator is closed (with the close() method)
 | ImportError	Raised when an imported module does not exist
 | IndentationError	Raised when indentation is not correct
 | IndexError	Raised when an index of a sequence does not exist
 | KeyError	Raised when a key does not exist in a dictionary
 | KeyboardInterrupt	Raised when the user presses Ctrl+c, Ctrl+z or Delete
 | LookupError	Raised when errors raised cant be found
 | MemoryError	Raised when a program runs out of memory
 | NameError	Raised when a variable does not exist
 | NotImplementedError	Raised when an abstract method requires an inherited class to override the method
 | OSError	Raised when a system related operation causes an error
 | OverflowError	Raised when the result of a numeric calculation is too large
 | ReferenceError	Raised when a weak reference object does not exist
 | RuntimeError	Raised when an error occurs that do not belong to any specific exceptions
 | StopIteration	Raised when the next() method of an iterator has no further values
 | SyntaxError	Raised when a syntax error occurs
 | TabError	Raised when indentation consists of tabs or spaces
 | SystemError	Raised when a system error occurs
 | SystemExit	Raised when the sys.exit() function is called
 | TypeError	Raised when two different types are combined
 | UnboundLocalError	Raised when a local variable is referenced before assignment
 | UnicodeError	Raised when a unicode problem occurs
 | UnicodeEncodeError	Raised when a unicode encoding problem occurs
 | UnicodeDecodeError	Raised when a unicode decoding problem occurs
 | UnicodeTranslateError	Raised when a unicode translation problem occurs
 | ValueError	Raised when there is a wrong value in a specified data type
 | ZeroDivisionError	Raised when the second operator in a division is zero
