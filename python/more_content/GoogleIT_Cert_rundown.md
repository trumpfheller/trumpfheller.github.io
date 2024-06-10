GoogleIT_Automation_w_Python_Cert

https://docs.python.org/3/tutorial/index.html
https://greenteapress.com/wp/think-python/

https://www.python.org/shell/
https://www.onlinegdb.com/online_python_interpreter
https://repl.it/languages/python3
https://www.tutorialspoint.com/execute_python3_online.php
https://rextester.com/l/python3_online_compiler
https://trinket.io/python3
[Python documentation](https://docs.python.org/3/)


```python
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)
```

* Data Types
```python
print(type(“a”)
<class ‘str’>
print(type(2)
<class ‘int’>
print(type(2.5)
<class ‘float’>
```

* Implicit vs Explicit Conversion
Implicit conversion 
is where the interpreter helps us out and automatically converts one data type into another, without having to explicitly tell it to do so.
Explicit conversion
is where we manually convert from one data type to another by calling the relevant function for the data type we want to convert to. We used this in our video example when we wanted to print a number alongside some text. Before we could do that, we needed to call the str() function to convert the number into a string. Once the number was explicitly converted to a string, we could join it with the rest of our textual string and print the result.


```python
Base = 6
Height = 3
Area = (base*height)/2
print(“the area of the triangle is: “ + str(area))
```

```python
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is:" + str(average))
```

* Defining Functions

```python
def greeting(name):
	print(“Welcome” + name )
def greeting(firstName, lastName):
	print(“Welcome” + firstName )
	print(“Welcome” + lastName )
```

```python
def print_seconds(hours, minutes, seconds):
    print((hours*3600) + (minutes*60)+(seconds))

print_seconds(1,2,3)

```

```python
def lucky_number(name):
	number = len(name)*9
	print(“Hello ” + name + “. Your lucky number is ” + str(number))

lucky_number(“Kay”)
lucky_number(“Marie”)
```
### refactoring 
The names of the variables and the function reflect their purpose, which helps the reader understand the code more quickly. 

```python
def circle_area(radius):
	pi = 3.14
	area = pi * (radius **2)
	print(area)

circle_area(5)
```

```python
def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    print("Distance in kilometers is: " + str(km))
    print("Round-trip in kilometers is: " + str(km * 2))    

convert_distance(55)   
```

```python
# This function compares two numbers and 
# returns them in increasing order.
def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1
bigger, smaller = order_numbers(100, 99)
print(bigger,smaller)

```

- parameter is a value passed into a function

### Conditionals

```python
print("cat" > "Cat")
# uppercase letters are alphabetically sorted before lowercase letters.
```

- To check if two values are the same, we can use the equality operator: == 
- To check if two values are not the same, we can use the not equals operator: != 
- To check if values are greater than or lesser than each other using > and <. 
- If you try to compare data types that aren’t compatible, like checking if a string is greater than an integer, Python will throw a `TypeError`. 


- `Branching` (Ability to alter its execution sequence) with `if` Statements

```python
# Version 1: With the else part
def is_positive(number):
  if number > 0:
    return True
  else:
    return None

def is_positive(number):
  if number > 0:
    return True
  else:
    return False

# Ver2: Without the else part, same effect
def is_positive(number):
  if number > 0:
    return True
```

```python
def is_positive(number):
  if number %2 == 0:
    return True
  return False
```

### elif statement

```python
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "negative"
  else:
    return "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative
```


```python
def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))
```


```python
def fractional_part(numerator, denominator):
''' Operate with numerator and denominator to 
    keep just the fractional part of the quotient
    floor devision'''
	fraction = numerator//denominator
    return 0

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
```

### while loop

- to continuously execute code based on the value of a condition. 
- the body of the block can be executed multiple times instead of just once. 

```python
x=0
while x<5:
    print(“Not there yet, x=” + str(x))
    x = x+1
print(“x=” + str(x))
```


```python
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)
```


```python
def count_down(start_number):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

# The fix: 

def count_down(start_number):
  current = 3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
```

### Infinite Loops 

```python
while True:
    do_something()
    if user_requested_to_stop():
        break
```


```python
def print_range(start, end):
    # Loop through the numbers from start to end
    n = start
    while n <= end:
        print(n)

print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
```


```python
def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = number * multiplier
 
        # additional condition to exit out of the loop
        if result = 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        result += 1

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15

multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25

multiplication_table(8) 
# Should print: 8x1=8 8x2=16 8x3=24
```

### for loop

So as an IT specialist, you'll use for loops to automate: 
- to copy files to machines, 
- process the contents of files, 
- automatically install software, 

```python
# iterate over a sequence of numbers, 
for x in range(5):
    print(x)
OUTPUT
0
1
2
3
4
```


```python
def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += int(square(n))
    return sum

print(sum_squares(10)) # Should be 285
```
```text
* Use `for` loops to iterate over a sequence of elements. 
* Use `while` loops when you want to repeat an action until a condition changes. 
```

```python
product = 1
for n in range (1,10):
    product = product*n
print(product)

def fact(n):
"""Return the factorial of the given number."""    
    r = 1
    while n > 0:
        r = r * n
        n = n - 1
    return r  
# OUTPUT
362880
```

```python
for left in range(7):
    for right in range(left,7):
        print("["+ str(left) + "|" + str(right) + "]", end=" ")
    print()
OUTPUT
[0|0] [0|1] [0|2] [0|3] [0|4] [0|5] [0|6] 
[1|1] [1|2] [1|3] [1|4] [1|5] [1|6] 
[2|2] [2|3] [2|4] [2|5] [2|6] 
[3|3] [3|4] [3|5] [3|6] 
[4|4] [4|5] [4|6] 
[5|5] [5|6] 
[6|6] 

```


```python
teams = [ 'Dragons', 'Wolves', 'Pandas']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + ‘ vs ’ + away_team)

Dragons vs Wolves
Dragons vs Pandas
Wolves vs Dragons
Wolves vs Pandas
Pandas vs Dragons
Pandas vs Wolves
```

### [Recursion](https://en.wikipedia.org/wiki/Recursion)

- A recursive function must include a recursive case and base case. 
- The recursive case calls the function again, with a different value. 
- The base case returns a value without calling the same function.

```python
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
```



```python

```

## Week4 Strings, (Lists, and Dictionaries)

```python
def double_word(word):
	return word + word + str(len(word) * 2)

    return

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
```

For example, 
* we can check if files are named a certain way by looking at the filename and seeing if they match our criteria, or 
* we can create a list of emails by checking out the users of our system and concatenating our domain. 

```python
def first_and_last(message):
    if (message[0] == message[-1]):
        return True
    elif (message[0] != message[-1]):
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(“ "))
TRUE
FALSE
TRUE
Error on line 2:
    if (message[0] == message[-1]):
IndexError: string index out of range

def first_and_last(message):
    if (message[0] == message[-1]):
        return True
    else:
        return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(" "))
Error on line 2:
    if (message[0] == message[-1]):
IndexError: string index out of range
```

```python
word = "supercalifragilisticexpialidocious"
print(word.index(“x"))
#	21
```

### `index` method

* A method is a function associated with a specific class. 
* returns just the first position that matches.
* if the string doesn't have the substring we're looking for, we get a value error 

```python
pets = “Cats & Dogs”
	pets.index(“s”)
	3
```

```python
def replace_domain(email, old_domain, new_domain):
	if “@” + old_domain in email:
		index = email.index(“@” + old_domain)
		new_email = email[:index] + “@” + new_domain
		return new_email
	return email

```

* First, we define the `replace_domain` function which accepts three parameters. The email address to be checked, the old domain, and the new domain. 
* Having all these values as parameters instead of directly in the code, makes our function reusable. We aren't just changing one domain to the other, we have a function that will work with all domains. 
* In the first line of the body of the function, we check if the concatenation of the `@`sign and the `old_domain` are contained in the email address, using the keyword `in`. 
* We check this to make sure the email has old domain on the portion that comes after the `@` sign. If the condition is true, the email address needs to be updated. 
* To do that, we first find out the index were the `old_domain`, including the  `@sign` starts. We know that this index will be a valid number because we've already checked that the substring was present. So, using this index, we create the new email. 
```python
		index = email.index(“@” + old_domain)
		new_email = email[:index] + “@” + new_domain
```
This is a string that contains the first portion of the old email, up until the index we had calculated, followed by the `@` sign and the new domain. 

Finally, we return this new email.
		return email
If the email didn't contain the new domain, then we can just return it, which is what we do in the last line. 

### More String Methods
```python
answer = ‘YES’
	if answer.lower() ==“yes”:
		print(“User said yes”)
```

* Some string methods let you perform transformations or formatting on the string text, like upper, and its opposite, lower: useful when you're handling user input. 

### `strip` method 

- to get rid of any white space

```python
“ yes ”.strip()
	‘yes’
	“ yes ”.lstrip
	‘yes ’
	“ yes ”.rstrip
	‘ yes’
```

### .count() method

```python
“ The number of times e occurs in this string is a 4 ”.count(“e”)
#	4
```

### endswith() method 

- returns whether the string ends with a certain substring

### isnumeric() method 
 
```python
“ Forest ”.isnumeric()
	False
	“1234”.isnumeric()
	True
```
- a string that is numeric => `int` function to convert it to an actual number.

```python
int(“12345”)+int(“54321”)
# 66666
```

### `join` method

- call it on the string that'll be used for joining. 

```python
" ".join(["This", "is ", "a ", "phrase ", "joined ", "by spaces."])
# 'This is  a  phrase  joined  by spaces.'

'…'.join(['This', 'is', 'a', 'phrase', 'joined', 'by triple dots.'])
# 'This...is...a...phrase...joined...by triple dots.’
```

### split method 

- split a string into a list of strings.
- returns a list of all the words in the initial string 
- it automatically splits by any whitespace. 

```python
'This...is...a..phrase disjoined by split method.'.split()
# ['This...is...a..phrase', 'disjoined', 'by', 'split', 'method.']
```


```python
'''
	def initials(phrase):
    		words = phrase.upper()
    		result = ""
    		for word in words:
        		result += ___
    		return ___
'''

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        x=list(word)
        if x[0].isupper():
            result +=x[0]
        elif x[0].islower():
            result +=x[0].upper()
    return result

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words
	result +=word[0].upper()
    return result

'''
print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
'''
```

### `.format()`

```python
def student_grade(name, grade):
    return “{name} received {grade}% on the exam”.format(name=name, grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price = 7.5
	with_tax = price*1.09
	print(price, with_tax)
	7.5 8.175
print(“base price: ${:.2f}. With Tax: ${:.2f}”.format(price, with_tax

```


```python
def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3}F | {:>6.2f} C" .format(x,to_celsius(x)))
'''
  0F | -17.78 C
 10F | -12.22 C
 20F |  -6.67 C
 30F |  -1.11 C
 40F |   4.44 C
 50F |  10.00 C
 60F |  15.56 C
 70F |  21.11 C
 80F |  26.67 C
 90F |  32.22 C
100F |  37.78 C
'''
```

## String Reference Cheat Sheet

### String operations
len(string) Returns the length of the string
for character in string Iterates over each character in the string
if substring in string Checks whether the substring is part of the string
string[i] Accesses the character at index i of the string, starting at zero
string[i:j] Accesses the substring starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(string) by default.

#### String methods
string.lower() / string.upper() Returns a copy of the string with all lower / upper case characters
string.lstrip() / string.rstrip() / string.strip() Returns a copy of the string without left / right / left or right whitespace
string.count(substring) Returns the number of times substring is present in the string
string.isnumeric() Returns True if there are only numeric characters in the string. If not, returns False.
string.isalpha() Returns True if there are only alphabetic characters in the string. If not, returns False.
string.split() / string.split(delimiter) Returns a list of substrings that were separated by whitespace / delimiter
string.replace(old, new) Returns a new string where all occurrences of old have been replaced by new.
delimiter.join(list of strings) Returns a new string with all the strings joined by the delimiter 

[docs.python](https://docs.python.org/3/library/stdtypes.html#string-methods)


## Formatting Strings Cheat Sheet

```python
# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# "{0} {1}".format(first, second)
```

```python
first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""
```

## SEQUENCES - list

- strings and lists are both examples of sequences
- Whenever you need to write a program that'll handle a variable amount of elements, you'll use a list.

```python
x = [“Now”, “we”, “are”, “cooking”]
type(x)
<class list>
```
* `print` function: to show the contents of the whole list. 
`len` function: length of the list is how many elements it has. => how many elements the list has. 
* keyword `in`: to check if a list contains a certain element => result of this check is a Boolean, which we can use as a condition for branching or looping. 
“Today” in x
False
* use indexing to access individual elements depending on their position in the list: use the square brackets and the index we want to access, exactly like we did with strings. 
* if we try to access an element after the end of the list?. We get an index error. We can't go over the end of the list. 
* . As with strings, we can also use indexes to create a slice of the list. 
* x[1:3] Again, the second element isn't included in the slice. So the range goes to the second index minus one. Here, we start at index one and go up to one less than three, which is two. 
* x[:2]We can also leave out one of the range indexes empty. The first value defaults to zero and the second value to the length of the list. 

```python
def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        sentence = sentence.split()
        # Only proceed if n is not more than the number of words
        if n <= len(sentence) and n>0:
            return(sentence [n-1])
    else:
        return(" ")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing
```

### `len(list)` 
* return the number of elements in a list: would return 4. 

### `in` keyword 

* to check if a list contains a certain element. 
* If the element is present, it will return a True boolean. 
* If the element is not found in the list, it will return False. 

lists and strings are both sequences of data => similar properties, like 
* being able to iterate over them using for loops; 
* support indexing; 
* using the len function to find the length of the sequence; 
* using the plus operator + in order to concatenate; and 
* using the in keyword to check if the sequence contains a value. Understanding these concepts allows you to apply them to other sequence types as well.

### Modifying the Contents of a List

* lists are mutable (we can add, remove, or modify elements in a list.) strings are not mutable. 
* Changing the list means we keep the same box and we add, remove, or change the elements inside that box. 

### `append` & `insert` method

```python
fruits = [“Pineapple”, “Banana”, “Apple”, “Melon”]
fruits.append[“Kiwi”]
fruits = [“Pineapple”, “Banana”, “Apple”, “Melon”, “Kiwi”]
fruits.insert(0,“Orange”)
print(fruits)
[“Orange”, “Pineapple”, “Banana”, “Apple”, “Melon”, “Kiwi”]
```

### `remove` method
* removes the first occurrence of the element from the list 

```python
fruits.remove(“Apple”)
print(fruits)
[“Orange”, “Pineapple”, “Banana”, “Melon”, “Kiwi”,“Peach”]
```
### `pop` method 
* Another way we can remove elements 
* method receives an index.
pop method returns the element that was removed at the index that was passed. 


```python
fruits.pop(3)
print(fruits)
[“Orange”, “Pineapple”, “Banana”, “Kiwi”,“Peach”]
```


```python
fruits[2] = “Strawberry”
print(fruits)
[“Orange”, “Pineapple”, “Strawberry”, “Banana”, “Kiwi”,“Peach”]
```

* If the list contains hosts on a network, you could add or remove hosts as they come online or offline. 

```python
# Define a list of hosts on a network
hosts = ["host1", "host2", "host3", "host4", "host5"]

# Assume a host goes offline, so you want to remove it from the list
offline_host = "host3"
if offline_host in hosts:
    hosts.remove(offline_host)

# Assume a new host comes online, so you want to add it to the list
online_host = "host6"
hosts.append(online_host)

# Print the modified list of hosts
print(hosts)
```
* If the list contains users authorized to run a certain process, you could add or remove users when permissions are granted or removed and so on. 

```python
# Define a list of users authorized to run a certain process
authorized_users = ["user1", "user2", "user3", "user4", "user5"]

# Suppose permission is granted to a new user, so you want to add them to the list
new_user = "user6"
authorized_users.append(new_user)

# Suppose permission is revoked from an existing user, so you want to remove them from the list
revoked_user = "user3"
if revoked_user in authorized_users:
    authorized_users.remove(revoked_user)

# Print the modified list of authorized users
print(authorized_users)
```


```python
'''
The `skip_elements` function returns a list 
containing every other element from an input list, 
starting with the first element.

def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for ___
        # Does this element belong in the resulting list?
        if ___
            # Add this element to the resulting list
            ___
        # Increment i
        ___

    return ___
'''
def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0
    # Iterate through the list
    for words in elements:
        # Does this element belong in the resulting list?
        if i <= len(elements):
            # Add this element to the resulting list
            new_list.append(elements[i])
        # Increment i
        i+= 2

    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) 
# Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) 
# Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
```

* Whenever you need to write a program that'll handle a variable amount of elements, you'll use a list.

### sequence of a fixed amount of elements

### `append` method. 

* add elements to the end of a list 
* `list.append("New data")` would add the string "New data" to the end of the list called list.

```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
# ['apple', 'banana', 'cherry', ‘orange']
```

### `extend()` method

*  adds the specified list elements (or any iterable) to the end of the current list.

```python
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
#	['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']
```

### `insert` method
* If you want to add an element to a list in a specific position. 
The method takes two parameters: 
the first specifies the index in the list, and 
the second is the element to be added to the list. 
`list.insert(0, "New data")` would add the string "New data" to the front of the list. This wouldn't overwrite the existing element at the start of the list. It would just shift all the other elements by one. 
If you specify an index that’s larger than the length of the list, the element will simply be added to the end of the list.

### `remove` method
You can remove elements from the list. 
This method takes an element as a parameter, and removes the first occurrence of the element. 
If the element isn’t found in the list, you’ll get a ValueError error explaining that the element was not found in the list.
Syntax: 
```python
list.remove(elmnt)
```

### `pop` method
To remove elements from a list. 
This method differs from the remove method in that it takes an index as a parameter, and returns the element that was removed. 
This can be useful if you don't know what the value is, but you know where it’s located. 
This can also be useful when you need to access the data and also want to remove it from the list.

```python
#	Remove the second element of the fruit list
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
#	['apple', 'cherry']
```

### `indexing`
you can change an element in a list
to overwrite the value stored at the specified index. 
For example, you can enter list[0] = "Old data" to overwrite the first element in a list with the new string "Old data".

built-in methods that you can use on lists/arrays
[ref](https://www.w3schools.com/python/python_ref_list.asp)

## Lists and Tuples

* `Strings` are sequences of characters and are immutable. 
* `Lists` are sequences of elements of any type and are mutable. 
* `Tuples` are sequences of elements of any type that are immutable. We write tuples in parentheses instead of square brackets.
* Since tuples are indexed, they can have items with the same value

* to make sure an element in a certain position or index refers to one specific thing and won't change. In these situations, lists won't help us. 

example, we have a tuple that represents someone's full name.

```python
fullname = (‘Grace’, ‘M’, ‘Hopper’)
```

> when using tuples the position of the elements inside the tuple have meaning. 

example: the return value of functions. 
When a function returns more than one value, it's actually returning a tuple.

```python
def convert _seconds(seconds): 
	hours = seconds // 3600
	minutes = (seconds -  hours * 3600) // 60
	remaining_seconds = seconds - hours*3600 - minutes*60	
	return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# This function returns three values - returns a tuple of three elements.. 
```

```python
def convert _seconds(seconds): 
	hours = seconds // 3600
	minutes = (seconds -  hours * 3600) // 60
	remaining_seconds = seconds - hours*3600 - minutes*60	
	return hours, minutes, remaining_seconds
result = convert_seconds(5000)

type(result)
<class ‘tuples’>
print(result)
#	(1,23,20)

```
### unpack tuples: 

* we can turn a tuple of three elements into three separate variables. 
Because the order won't change, we know what those variables are present, like this.

```python
def convert _seconds(seconds): 
	hours = seconds // 3600
	minutes = (seconds -  hours * 3600) // 60
	remaining_seconds = seconds - hours*3600 - minutes*60	
	return hours, minutes, remaining_seconds
hours, minutes, seconds = result
print(hours, minutes, seconds)
1 23 20

# we've split the tuple into three separate values

def convert _seconds(seconds): 
	hours = seconds // 3600
	minutes = (seconds -  hours * 3600) // 60
	remaining_seconds = seconds - hours*3600 - minutes*60	
	return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)
0 16 40
```

USE case: 

* you could use a tuple to have a filename and it's size, or 
* you could store the name and email address of a person, or a date and time and the general health of the system at any point in time. 

```python
'''
use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.
'''
def file_size(file_info):
  name, type, size= file_info
  return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) 
# Should print 17.46
print(file_size(('Notes', 'txt', 496))) 
# Should print 0.48
print(file_size(('Program', 'py', 1239))) 
# Should print 1.21
```

### Tuples

* `Strings` are sequences of characters, and are immutable. 
* `Lists` are sequences of elements of any data type, and are mutable. 
* `Tuples` are like lists, since they can contain elements of any data type. But unlike lists, tuples are immutable. They’re specified using parentheses instead of square brackets.

Use case: 
* when we need to ensure that an element is in a certain position and will not change.

when a function returns multiple values. In this case, what gets returned is a tuple, with the return values as elements in the tuple. The order of the returned values is important, and a tuple ensures that the order isn’t going to change. Storing the elements of a tuple in separate variables is called unpacking. This allows you to take multiple returned values from a function and store each value in its own variable.

### Iterating over Lists and Tuples

* for loops iterate over a sequence of elements ( list of strings.).

```python
'''
For each of the strings, we get its length and add it to the total amount of characters. At the end we print the total and the average which we get by dividing the total by the length of the list. 
'''
animals = [‘Lion’, ‘Zebra’, ‘Dolphin’, ‘Monkey’]
chars = 0
for animal in animals:
  chars += len(animal)
	print(“Total characters: {}, Average length: {}”.format(chars, chars/len(animals)))
# OUTPUT
# Total characters: 22, Average length: 5.5
```

### `enumerate` function

- returns a tuple for each element in the list. 
- The first value in the tuple is the index of the element in the sequence. 
- The second value in the tuple is the element in the sequence. 

Example:

```python
'''
What if you wanted to know the index of an element while going through the list? 
1. You could use the range function and then use indexing to access the elements at the index that range returned. 
2. You could use a range function and then use indexing to access the elements at the index that range just returned or 
3. you could just use the enumerate function. 
'''

winners = [ ‘Ashley’, ‘Dylan’, ‘Reese’] 
for index, person in enumerate (winners)
	print (“{} - {}”.format(index + 1, person)
1 - Ashley
2 - Dylan
3 - Reese
```

```python
'''
Say you have a list of tuples containing two strings each. 
- first string is an email address and 
- second string is the full name of the person with that email address. 

Write a function that creates a new list containing one string per person including their name and the email address between angled brackets. the format usually used in emails like this.  Terrance Ford <terrance@example.com>

first create the variable [result] that we'll use as a return value which will be a list. 
'''
def full_emails (people): 
	result = []
```


```python
def full_emails (people): 
	result = [] 
	for email, name in people: 
  # iterate over the list of people. 
		result.append(“{} <{}>”.format (name, email))
    # append to the resulting string to the results list 
	return result
print(full_emails([(“alex@example.com", “Alex Diego”), (“shay@example.com", “Shay Brandt”)]))
#OUTPUT
# ['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>’]
```

* use the range function so much with for loops, you might be tempted to use it for iterating over indexes of a list and then to access the elements through indexing. => ugly. Better: iterate through the elements of the list directly or using enumerate when you need the indexes 
* to iterate over the indexes (when we're trying to modify the elements of the list) => it might be better to use a copy of the list instead. 


```python
'''
check if an element is in an even position or an odd position
'''
def skip_elements(elements):
    element = []
    for i,e in enumerate(elements):
      # Iterate through the list
        if i % 2 == 0:
            element.append(e)
    return element
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) 
# Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
```

### Iterating Over Lists Using [Enumerate](https://docs.python.org/3/tutorial/datastructures.html?highlight=enumerate)

* to access the elements in a list, along with the index of the element
* takes a list as a parameter and returns a tuple for each element in the list
* first value of the tuple is the index and the second value is the element itself.

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i, v)
0 tic
1 tac
2 toe

```

### List Comprehensions

* creating lists based on sequences
* List comprehensions let us create new lists based on sequences or ranges.

```python
[expression for variable in sequence] 
# Creates a new list based on the given sequence. Each element is the result of the given expression.
```

```python
[expression for variable in sequence if condition] 
newlist = [expression for item in iterable if condition == True]
# Creates a new list based on the given sequence. Each element is the result of the given expression; elements only get added if the condition is true.  
```

[w3schools](https://www.w3schools.com/python/python_lists_comprehension.asp)

```python
multiples = []
	for x in range(1,11):
	multiples.append(x*7)
print(multiples)
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

multiples = [ x * 7 for x in range(1,11)] 
print(multiples)
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
```


```python
languages = ["Python", "Ruby", "Java", "Perl", "Go"]
lengths = [len(language) for language in languages]
print(lengths)
# [6, 4, 4, 4, 2]

```

### List comprehensions with conditional clause

```python
z = [x for x in range(0,101) if x % 3 == 0] 
print(z)
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

```


```python
'''
def odd_numbers(n):
    return [x for x in ___ if ___]
'''
def odd_numbers(n):
    return [x for x in range(0, n+1) if x % 2 !=0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

```

### [sequence operations]( https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)

len(sequence) Returns the length of the sequence
for element in sequence Iterates over each element in the sequence
if element in sequence Checks whether the element is part of the sequence
sequence[i] Accesses the element at index i of the sequence, starting at zero
sequence[i:j] Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
for index, element in enumerate(sequence) Iterates over both the indexes and the elements in the sequence at the same time

* [mutable-sequence-types](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types)
* [list](https://docs.python.org/3/library/stdtypes.html#lists)


### List-specific operations and methods

list[i] = x Replaces the element at index i with x
list.append(x) Inserts x at the end of the list
list.insert(i, x) Inserts x at index i
list.pop(i) Returns the element a index i, also removing it from the list. If i is omitted, the last element is returned and removed.
list.remove(x) Removes the first occurrence of x in the list
list.sort() Sorts the items in the list
list.reverse() Reverses the order of items of the list
list.clear() Removes all the items of the list
list.copy() Creates a copy of the list
list.extend(other_list) Appends all the elements of other_list at the end of list

Most of these methods come from the fact that lists are mutable sequences. 

### dictionary

* Like lists, dictionaries are used to organize elements into collections.
* while in a list the index must be a number, in a dictionary you can use a bunch of different data types as keys, like strings, integers, floats, tuples, and more
* Dictionaries are mutable (can add remove and replace entries). 

```python
x = {} 
	print(type(x)) 
	<class ‘dict’>

file_counts ={"jpeg":10, "txt":14, "csv":2, "py":23} 
print(file_counts) 
# {'jpeg': 10, 'txt': 14, 'csv': 2, 'py': 23}

file_counts = {"jpeg": 10, "txt": 14, "csv": 2, "py": 23}
file_counts["txt"]
# 14

"jpeg" in file_counts
True
"html" in file_counts 
False 

# to add a file count of eight for a new CFG file extension. 
	file_counts["cfg"] = 8 
	print(file_counts) 

# When you use a key that already exists to set a value, the value that was already paired with that key is replaced 
	file_counts["csv"] = 17 
	print(file_counts)
    # {'jpeg': 10, 'txt': 14, 'csv': 2, 'py': 23, 'cfg': 8}
    # {'jpeg': 10, 'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}
```
-  The keys inside of a dictionary are unique. If we try to store two different values for the same key, we'll just replace one with the other.

### del
```python
file_counts ={'jpeg': 10, 'txt': 14, 'csv': 17, 'py': 23, 'cfg': 8}
	del file_counts["cfg"]
	print(file_counts) 
file_counts ={'jpeg': 10, 'txt': 14, 'csv': 17, 'py': 23}
```

```python
toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary
print("Chapter 5" in toc) # Is there a Chapter 5?
```

### Iterating over the Contents of a Dictionary

- for loop in dictionary, the iteration variable will go through the keys

```python
file_counts = {"jpg":10, "txt":14, "csv":2, “py":23
for extension in file_counts:
    print(extension) 
#Output
jpg
txt
csv
py
```

### `items` method

```python
file_counts = {"jpg":10, "txt":14, "csv":2, “py":23
for ext, amount in file_counts.items(): 
  print("there are {} files with the .{} extension".format(amount, ext)) 

there are 10 files with the .jpgextension
there are 14 files with the .txtextension
there are 2 files with the .csvextension
there are 23 files with the .pyextension
```

```python
print(file_counts.keys())
dict_keys(['jpg', 'txt', 'csv', 'py'])

print(file_counts.values())
dict_values([10, 14, 2, 23])
```
1. use items to get key value pairs, file_counts.items()
2. keys to get the keys, and file_counts.keys()
3. values to get the values. file_counts.values()

```python
'''
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for ___ in cool_beasts.items():
    print("{} have {}".format(___))
'''

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for amount, ext in cool_beasts.items():
    print("{} have {}".format(amount, ext))

for amount, limbs in cool_beasts.items():
    print("{} have {}".format(amount, limbs))

'''
Your output:
octopuses have tentacles
dolphins have fins
rhinos have horns
'''
```

- dictionaries are a great tool for counting elements and analyzing frequency.

```python
# Counting how many times each letter appears in a piece of text.
# a dictionary where keys are each of the letters present in the string and the values are how many times each letter is present
def count_letters(text):
	result = {}
    # initializing an empty dictionary
	for letter in (text):
		if letter not in result: 
            #For each letter, check if it's not already in the dictionary
			result[letter]=0
            # in that case, we initialize an entry in dictionary (value of zero)
		result[letter] += 1
        # increment the count for that letter 
	return result
count_letters("aaaaaaaaaaaaa") 
# {'a': 13}
count_letters("tenant") 
# {'t': 2, 'e': 1, 'n': 2, 'a': 1}

```
>  you're analyzing logs in your server and you want to count how many times each type of error appears in the log file. You could easily do this with a dictionary by using the type of error as the key and then incrementing the associated value each time you come across that error type.

### `items` method 

- This method returns a tuple for each element in the dictionary, where the first element in the tuple is the key and the second is the value.

```python
dictionary.items()
```

### `keys()` method

- to access the keys in a dictionary

```python
dictionary.keys()
```

### `values()` method 
* to access the values

```python
dictionary.values()
```

### Dictionaries vs. Lists

- In `lists`, you can store any data type. 
- In `dictionaries`, we can store any data type for the values but the keys are restricted to specific types. 

* use any immutable data type; numbers, booleans, strings and tuples as dictionary keys. But you can't use lists or dictionaries for that. 
* On the flip side, like we said, the values associated with keys can be any type, including lists or even other dictionaries. You can use them to represent more complex data structures like directory trees in the file system. 

* There's a ton of different key value pairs that we need to work with in system administration. So I use dictionaries all the time. They're especially useful with large data sets. When I need to write a script that gets specific keys out of it to manipulate or modify the associated value.

* One-time, I wanted to be able to look up which Disney villain is associated with each protagonist. So I created a dictionary that stores a key like Snow White, with the value, evil queen. 

use case

- when you plan on searching for a specific element:

store a series of IP addresses to ping, you could put them all into a list and iterate over them. 
```python
ip_addresses = [“192.168.1.1”, “127.0.0.1”, “8.8.8.8”]
```

a list of host names and their corresponding IP addresses, you might want to pair them as key values in a dictionary.
```python
host_addresses = {“router”: “192.168.1.1”, “localhost”: “127.0.0.1”, “google”: “8.8.8.8”}
```


```python
'''
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for __:
    for __:
        print("{} {}".format(__))
'''

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, value in wardrobe.items():
    for i in value:
        print("{} {}”.format(value, key))
Here is your output:
['red', 'blue', 'white'] shirt
['red', 'blue', 'white'] shirt
['red', 'blue', 'white'] shirt
['blue', 'black'] jeans
['blue', 'black'] jeans

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, value in wardrobe.items():
    for i in value:
        print("{} {}”.format(i, key))

# Output:
red shirt
blue shirt
white shirt
blue jeans
black jeans

```

### Dictionary Methods Cheat Sheet
Definition
		x = {key1:value1, key2:value2} 
**Operations**
len(dictionary) - Returns the number of items in the dictionary
for key in dictionary - Iterates over each key in the dictionary
for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
if key in dictionary - Checks whether the key is in the dictionary
dictionary[key] - Accesses the item with key key of the dictionary
dictionary[key] = value - Sets the value associated with key
del dictionary[key] - Removes the item with key key from the dictionary
**Methods**
dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
dict.keys() - Returns a sequence containing the keys in the dictionary
dict.values() - Returns a sequence containing the values in the dictionary
dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
dict.clear() - Removes all the items of the dictionary

Check out the official [documentation](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) for dictionary operations and methods.  
[mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

### Set

* used when you want to store a bunch of elements and be certain that there are only present once.
* Elements of a set must also be immutable. You can think of this as the keys of a dictionary with no associated values or you could see it as a list where what matters isn't the order of the elements but whether an element is in the list or not.  

### Object-oriented programming

* An idea is defined using a class, 
* an instance of this class is called an object. 
* `attributes` are the characteristics associated to a type, (color and flavor)

```python
class Apple:
    color = ''
	flavor = '' 

jonagold = Apple()
jonagold.color = “red”
jonagold.flavor = “sweet”
print (jonagold.color)  
print jonagold.flavor) 

```

* `methods` are the functions associated to a type. (an action, defines what you do with an object)

```python
__add__(self, value, /)
#      Return self+value.
 
__contains__(self, key, /)
#  Return key in self.

__eq__(self, value, /)
#  Return self==value.

__format__(self, format_spec, /)
#  Return a formatted version of the string as described by format_spec.

__ge__(self, value, /)
#   Return self>=value.
__getattribute__(self, name, /)
#    Return getattr(self, name).

__getitem__(self, key, /)
#    Return self[key].

__getnewargs__(...)

__gt__(self, value, /)
#     Return self>value.

__hash__(self, /)
#      Return hash(self).
```
```python

```

### Inheritance

```python
class Fruit:
    def __init__(self, color, flavor):
        self.color = color
		self.flavor = flavor
class Apple(Fruit):
    pass
class Grape(Fruit):
	pass

granny_smith = Apple(“green”, “tart”)
carnelian = Grape(“purple”, “sweet”)

print(granny_smith.flavor)
print(carnelian.color)
```

* If a class has an attribute or a method defined in it, inheriting classes will have the 

```python
class Animal:
	sound = ‘’
	def __init__(self, name):
		self.name = name
	def speak(self):
		print(“{sound} I am {name}! {sound}”.format(name=self.name, sound=self.sound))

class Piglet(Animal):
	sound = “Oink!”

```


```python
class Animal:
	sound = ‘’
	def __init__(self, name):
		self.name = name
	def speak(self):
		print(“{sound} I am {name}! {sound}”.format(name=self.name, sound=self.sound))

class Piglet(Animal):
	sound = “Oink!”
hamlet = Piglet(“Hamlet”)
hamlet.speak()

class Cow(Animal):
	sound = “Moooooo!”
milky = Cow(“Milky White”)
milky.speak()

```

```python

```


```python

```


```python

```

```python

```


```python

```


```python

```


```python

```

```python

```


```python

```


```python

```

```python

```


```python

```


```python

```


```python

```

```python

```


```python

```


```python

```