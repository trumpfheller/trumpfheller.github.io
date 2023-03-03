---
title: Control Structures
category: Control Flow
layout: post
---
> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
>  [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [OOP](./oop.html) ||

***

### to alter control flow:
- Conditional 
- while loop
- for loop
- Python doesn’t have a switch statement.

### Conditional 

Syntax
```python
if <expression-**boolean**>:
    <statement>
```

#### Boolean
```python
print(10>1)
True
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
#### Module Review
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
```python
print("cat" > "Cat")
# OUTPUT
True
```
=> uppercase letters are alphabetically sorted before lowercase letters.

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

### One-Line if Statements
### Ternary Operator (Short Hand If)


```python
#standard
if <expr>:
    <statement>

# shorter
if <expr>: <statement>
if <expr>: <statement_1>; <statement_2>; ...; <statement_n>
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
### Syntax
```python 
<expr1> if <conditional_expr> else <expr2>
```

### Example
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

### while loop
- execute a set of statements as long as a condition is true
- to continuously execute code based on the value of a condition. 
- code block can be executed multiple times instead of just once.
- performing an action over and over until a condition has changed.
- code block will keep executing as long as the evaluation 
statement is true. Once the statement is no longer true, the loop exits and the next line of code will be executed.

#### Use case
- use them to keep asking for a username if the one provided isn't valid
- try an operation until it succeeds.

```python
1 x=0 #initializing
2 while x<5:
3    print("Not there yet, x=" + str(x))
4    x = x+1
5 print("x=" + str(x))
# OUTPUT
Not there yet, x=0
Not there yet, x=1
Not there yet, x=2
Not there yet, x=3
Not there yet, x=4
x=5
```

***

#### while loop inside of a function. 
```python
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)
```

* Step1: 
    * initializing a variable called x (1).
* Step2: 
    * the function received a value and the while loop checks if the value inside of the x variable is less than the parameter n. 
        * If that comparison evaluates to true, then the code inside the while block is executed. 
* Step3: 
    * think it through: 
        - pass a value of 5 as a parameter to this function. In the first pass through the loop, x is always equal to 1, so the comparison: 1 smaller than or equal to 5 would be true and we then enter the body of the loop. 
In the body, we first print a message indicating that the current attempt number and then we increase the value of x by 1. 


The process continues until the result of the comparison isn't true anymore, which happens when x is bigger than n. In our current example, this would be when the value of x is 6. 
 
#### Example - to call a separate function that evaluates the condition. 

```python
username = get_username()
while not valid_username(username):
    print("invalid username")
    username = get_username()
```

 a lot of code hidden behind functions. 
#### get_username() function 
- asks the user for a username and a valid_username function that validates that username. 
- In this case, the body of the while loop will be executed until the user enters a valid username. 
The important thing to remember is that the condition used by the while loop needs to evaluate to true or false. 

rundown of some of the most common pitfalls that you may come across when writing your own loops. Head on over to the next video to get started.


If you have a loop that's gone rogue and is not behaving as expected, it's a good idea to check if all the variables are correctly initialized. 
In this example, we need to set x back to 1 before starting the second loop. 

```python
1 def count_down(start_number):
2  while (current > 0):
3    print(current)
4   current -= 1
5  print("Zero!")

count_down(3)

# Line 2: Using variable 'current' before assignment
```

The fix: 

```python
def count_down(start_number):
  current = 3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
#OUTPUT
3
2
1
Zero!
```



#### recap 
- whenever you're writing a loop check that you're initializing all the variables you want to use before you use them. 

***

#### Infinite Loops 
- what's called an infinite loop, a loop that keeps executing and never stops. 

```python
while x%2 ==0:
    x = x/2
```
It uses the modulo operator that we saw a while back. This cycle will finish for positive and negative values of x. But what would happen if x was zero? The remainder of 0 divided by 2 is 0, so the condition would be true. The result of dividing 0 by 2 would also be zero, so the value of x wouldn't change. This loop would go on forever, and so we'd get an infinite loop. 

If our code was called with x having the value of zero, the computer would just waste resources doing a division that would never lead to the loop stopping. 

. To avoid this, we need to think about what needs to happen for a loop to be successful.

```python
if x != 0:
    while x%2-=-=0:
        x = x/2
```
 In this example, we said that x needs to be different than zero. So we could nest this while loop inside an if statement just like this. 
With this approach, the while loop is executed only when x is not zero. 

Alternatively, we could add the condition directly to the loop using a logical operator like in this example.

```python
while x != 0 and x % 2 == 0:
    x = x /2
```
This makes sure we only enter the body of the loop for values of x that are both different than zero and even. 

#### sum up
- An infinite loop means the code block in the loop will continue to execute and never stop. 
- This can happen when the condition being evaluated in a while loop doesn't change. 
- take a moment to consider the different values a variable can take - Think about unexpected values, like zero.
- the break keyword to signal that the current loop should stop running. We can use it not only to stop infinite loops but also to stop a loop early if the code has already achieved what's needed. 
First, remember to initialize your variables, and second, check that your loops won't run forever.
- break the loop by pressing Ctrl+C

 ```python 
while True:
    do_something()
    if user_requested_to_stop():
        break
```

***

### for loop?
- to iterate over a sequence of elements.
- to iterate over a sequence of values. 

#### for loop in range() method
- iterate through a sequence of numbers generated using the range function
- variable(x) will take each of the values in the sequence that loop iterates through.
```python
for x in range(5):
    print(x)
#OUTPUT
0
1
2
3
4
```


#### for loop in a function 
- a function to calculate the square of a number, and then use a for loop to sum the squares of the numbers in a range.

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


Iterating over numbers looks very similar to the while 
=> for loop iterates over a sequence of values of any type, not just a range of numbers. 
Here a for loop that iterates over a list of strings. I
- We're iterating a list of strings. And for each of the strings in the list, we're printing a greeting.

```python
friends = [‘Taylor’, ‘Alex’, ‘Eli’]
for friend in friends:
    print(“Hi ” + friend)
```

The sequence that the for loop iterates over could contain any type of element, not just strings. For example, we could iterate over a list of numbers to calculate the total sum and average.

```python 
values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value oil values: 
    sum += value
    length += 1
print(“Total sum: ” + str(sum) + “ - Average: ” +str(sum/length))
```

we’re defining a list of values. 
After that, we're initializing two variables, sum and length, that will update in the body of the for loop. 
In the for loop, we're iterating over each of the values in the list, adding the current value to the sum of values, and then also adding 1 to length, which calculates how many elements there are in the list. 
Once we've gone through the whole list, we print out the sum and the average. We'll keep using for loops in our examples every time we want to iterate over the elements of any sequence and operate with them. 
Some examples of sequences that we can iterate are 
the files in a directory, 
the lines in a file, 
the processes running on a machine. 
And there's a bunch of others. 

So as an IT specialist, you'll use for loops to automate: 
to copy files to machines, process the contents of files, 
automatically install software, 
and a lot more. 

A few weeks ago, I had to update a lot of files with different values depending on their contents. So I used a for loop in a script to iterate over all the files. Then, my script took different actions based on an if condition and updated all of those files for me. It would have taken me forever if I had done this manually file by file. If you're wondering when you should use for loops and when you should use while loops, there's a way to tell. 

Use for loops when there's a sequence of elements that you want to iterate. 
Use while loops when you want to repeat an action until a condition changes. 
And if whatever you're trying to do can be done with either for or while loops, just use whichever one's your favorite. I'm more of a "while" gal myself, but it's totally your call.

***

### For Loops Recap

### while loop 
- for performing an action over and over until a condition has changed. 

### for loop 
- to iterate over a sequence of elements. The power of for loops comes from the fact that it can iterate over a sequence of any kind of data, not just a range of numbers. You can use for loops to iterate over a list of strings, such as usernames or lines in a file.
  


For loops allow you to iterate over a sequence of values:
```python
for x in range(5):
  print(x)
```

Similar to if statements and while loops, for loops begin with the keyword for with a colon at the end of the line. Just like in function definitions, while loops and if statements, the body of the for loop begins on the next line and is indented to the right. But what about the stuff in between the for keyword and the colon? In our example, we’re using the range() function to create a sequence of numbers that our for loop can iterate over. In this case, our variable x points to the current element in the sequence as the for loop iterates over the sequence of numbers. Keep in mind that in Python and many programming languages, a range of numbers will start at 0, and the list of numbers generated will be one less than the provided value. So range(5) will generate a sequence of numbers from 0 to 4, for a total of 5 numbers.
Bringing this all together, the range(5) function will create a sequence of numbers from 0 to 4. Our for loop will iterate over this sequence of numbers, one at a time, making the numbers accessible via the variable x and the code within our loop body will execute for each iteration through the sequence. So for the first loop, x will contain 0, the next loop, 1, and so on until it reaches 4. Once the end of the sequence comes up, the loop will exit and the code will continue.




### calculating the product of all numbers from 1 to 10
#### More for loops examples

```python
product = 1
for n in range (1,10):
    product = product*n
print(product)

>>> def fact(n):
...     """Return the factorial of the given number."""    
...     r = 1
...     while n > 0:
...         r = r * n
...         n = n - 1
...     return r  
#OUTPUT
#362880
```

Additionally, we can specify a third parameter to change the size of each step. This means that instead of going one by one, we could have a larger difference between the elements. 

```python
def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print(x, to_celsius(x))
```

First, we're defining a function that converts a temperature value from Fahrenheit to Celsius, and we're simply using a conversion formula to do that. Then we have a for loop that starts at zero, and goes up to 100 in steps of 10. Notice that we're using 101 for the upper limit instead of 100. We're doing this because the range never includes the last element, and we want to include 100 in our range. The body of the for-loop prints the value in Fahrenheit and the value in Celsius creating a conversion table. 

0 -17.77777777777778
10 -12.222222222222221
20 -6.666666666666667
30 -1.1111111111111112
40 4.444444444444445
50 10.0
60 15.555555555555555
70 21.11111111111111
80 26.666666666666668
90 32.22222222222222
100 37.77777777777778

The range function can receive one, two or three parameters. 
If it receives one parameter, it will create a sequence one by one from zero until one less than the parameter received.
If it receives two parameters, it will create a sequence one by one from the first parameter until one less than the second parameter. 
Finally, if it receives three parameters, it will create a sequence starting from the first number and moving towards the second number. But this time, the jumps between the numbers will be the size of the third number, and again, it will stop before the second number. 


Sound like a lot to remember, but don't panic. As we've said before, you don't have to try to memorize it all, just keep practicing. It'll soon become second nature. To help you practice, we've included all of this in a handy cheat sheet to refer to whenever you need it. You'll find that in the next reading.


#### A Closer Look at the Range() Function

Previously we had used the range() function by passing it a single parameter, and it generated a sequence of numbers from 0 to one less than we specified. 
 the range() function can pass in two parameters: the first specifying our starting point, the second specifying the end point. Don't forget that the sequence generated won't contain the last element; it will stop one before the parameter specified.
The range() function can take a third parameter, too. This third parameter lets you  alter the size of each step. So instead of creating a sequence of numbers incremented by 1, you can generate a sequence of numbers that are incremented by 5.
To quickly recap the range() function when passing one, two, or three parameters:
One parameter will create a sequence, one-by-one, from zero to one less than the parameter.
Two parameters will create a sequence, one-by-one, from the first parameter to one less than the second parameter.
Three parameters will create a sequence starting with the first parameter and stopping before the second parameter, but this time increasing each step by the third parameter.


### Nested for Loops
Dominoes 
each Domino Tiles has two numbers represented by a collection of dots carved on each half of the tile. 
The numbers go from zero to six. 
Tiles can be rotated so that each combination of numbers is represented only once in a set of Domino Tiles (the two three tile is the same as the three two tile, and there's only one per set). 
to write a program that prints each Domino Tile in a set: 
If we take all of the tiles that have zero on the left, we can print tiles with numbers from zero to six on the right. 

But what about tiles that have one on the left? Well, we need to skip the one zero tile, because that one was already printed as zero one. 
So we can print a list of tiles with one on the left and numbers from one to six on the right. 
When we look at two, we would need to skip both zero and one, and so on. 
=>  we'd need to write two for loops, one inside the other. This is what we call nested for loops. Check out how this looks on Python code. 

```python
for left in range(7):
    for right in range(left,7):
        print("["+ str(left) + "|" + str(right) + "]", end=" ")
    print()

# OUTPUT
[0|0] [0|1] [0|2] [0|3] [0|4] [0|5] [0|6] 
[1|1] [1|2] [1|3] [1|4] [1|5] [1|6] 
[2|2] [2|3] [2|4] [2|5] [2|6] 
[3|3] [3|4] [3|5] [3|6] 
[4|4] [4|5] [4|6] 
[5|5] [5|6] 
[6|6] 
```
#### End parameter
Normally, once print has taken the content we passed and written it to the screen, then
it writes a special character that creates a new line called the newline character. If we
want print to write something else instead of the newline character, we use the
end parameter, like we see in this example. 

Notice how the second for loop iterates over a different number of elements each time it's called as the value of left changes. Depending on what you want to achieve with your nested loops, you may want both loops to always go through the same number of elements. Or you might want the second loop to connect to the first one. 

Let's look at a different example. 
Let's say you run a local girl's basketball league in your town. You have four teams that will play against each other in the league, both at home and away. You've stored the names of the teams in a list, like this. 

```python
teams = [‘Dragons’, ‘Wolfes’, ‘Pandas’]
```

We want to write a script that will output all possible team pairings. For this, the order of the names matters because for each game, the first name will be the home team and the second name is the away team. Of course, what we don't want to do is have a team playing against itself. So what statement do we need to use to avoid that? 
To do this, we need to use a conditional that makes sure we only print the pairing when the names are different. Check out what this looks like.

```python
teams = [ 'Dragons', 'Wolves', 'Pandas']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + ‘ vs ’ + away_team)
```
Dragons vs Wolves
Dragons vs Pandas
Wolves vs Dragons
Wolves vs Pandas
Pandas vs Dragons
Pandas vs Wolves

As you can see, nested loops are super useful for solving certain problems, like pairing teams. What it doesn't solve is the question, who would win in a face-off between dragons and unicorns? If only there were some code for that. 

Anyway, we've seen that nested loops are a handy tool, but the longer the list your code needs to iterate through, the longer it takes your computer to complete the task. 

```python
for element in long_list:
    do_something (element)
```
Let's say your manager asks you to do an operation that will run through a list of 10,000 elements. If the operation takes one millisecond per element, the whole loop would take one millisecond times 10,000 to complete, which is 10 seconds. 
Now, imagine we add a nested loop that has to go over the same 10,000 elements. 
```python
for element1 in long_list:
    for element2 in long_list:
        do_something (element)
```

This means that each iteration of the outside loop would do a full iteration of the inside loop, which again, would take ten seconds to go through the whole list. So now, the whole iteration takes 10,000 times 10 seconds, which is a 100,000 seconds, that's over 27 hours. 
This doesn't mean we shouldn't use nested loops. They are a useful tool when solving problems that require them, but we need to be careful of where and how we use them. Throughout this course, and one is coming up, we'll look at a lot of techniques that can help us pick the right tool to use for each type of problem. Up next, we'll look into some common errors that you might come across when writing your for loops and what to do about them.

#### Common errors in for Loops
 But before we're done with for loops, let's check out some common mistakes you may come across while trying this yourself. As we've called out are ready, for loops iterate over sequences. The interpreter will refuse to iterate over a single element. 
for x in 25: 
    print(x)

TypeERROR: int object is not iterable
 
in this example, we're trying to iterate over the number 25. Python prints a type error telling us that integers are not iterable. There are two solutions to this problem, depending on what we're trying to do. 

If we want to go from zero to 25, then we use the range function, so 
for x in range(25): 
print(x) 
but if we're trying to iterate over a list that has 25 as the only element, then it needs to be a list and that means writing it between square brackets, 

```python
for x in [25]: 
print(x) 
OUTPUT
25
```
You might be wondering why you'd ever want to iterate over a list of one element and that's a good question. Well, this kind of issue usually happens when you have a function with a for loop inside it, which is iterating over the elements of a list received by parameter. 



Say for example, you have a function that fixes the permissions of a list of files received by parameter, and you want to call this function to fix the permissions of just one specific file. To do that, you need to pass the file as the single element of a list. 

```python
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
greet_friends ([‘Taylor', 'Alex', 'Pat', ‘Eli'])
Hi Taylor
Hi Alex
Hi Pat
Hi Eli
>>> 
```

We're going to modify it to have the greetings inside a function. We've defined a greet friends function, that receives a list by parameter and iterates over that list, greeting each friend. 

But what if we only want to greet one friend instead of four? 
Well, we still need to define a list, but with only one element. 
But first, let's see what would happen if we don't do that, 
```python
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
greet_friends(“Barry")
>>> %Run greet_friends.py
Hi B
Hi a
Hi r
Hi r
Hi y
>>> 
```

This happens because strings are iterable, the for loop will go over each letter of the string and do the operation we asked it to do, which in this case, print a greeting. 
Depending on what you're trying to do, you may actually want to iterate through the letters of a string. But in this case, we don't. 

So to sum it up, if you get an error that a certain type isn't iterable, you need to make sure the for loop is using a sequence of elements and not just one, and if you find your code iterating through each letter of a string when you want it to do it for the whole string, you probably want to have that string be a part of a list. We've now learned how to write while loops and for loops. You might remember, for loops are best when you want to iterate over a known sequence of elements but when you want to operate while a certain condition is true, while loops are the best choice. Next up, we've got a super useful cheat sheet for you that puts all this into one handy resource. After that, head over to the practice quiz to test your knowledge and check in on how you're doing.



#### Things to watch out for!
Failure to initialize variables. Make sure all the variables used in the loop’s condition  are initialized before the loop.
Unintended infinite loops. Make sure that the body of the loop modifies the variables used in the condition, so that the loop will eventually end for all possible values of the variables.
 Typical use:
While loops are mostly used when there’s an unknown number of operations to be performed, and a condition needs to be checked at each iteration.
For Loops
=> iterates over a sequence of elements, executing the body of the loop for each element in the sequence.
##### Syntax:
```python
for variable in sequence:
    body
```

#### The range() function:
range() generates a sequence of integer numbers. It can take one, two, or three parameters:
```python
range(n): 0, 1, 2, ... n-1
range(x,y): x, x+1, x+2, ... y-1
range(p,q,r): p, p+r, p+2r, p+3r, ... q-1 (if it's a valid increment)
```

#### Common pitfalls:
Forgetting that the upper limit of a range() isn’t included.
Iterating over non-sequences. Integer numbers aren’t iterable. Strings are iterable letter by letter, but that might not be what you want.
Typical use:
For loops are mostly used when there's a pre-defined sequence or range of numbers to iterate.

Break & Continue
You can interrupt both while and for loops using the break keyword. We normally do this to interrupt a cycle due to a separate condition.
You can use the continue keyword to skip the current iteration and continue with the next one. This is typically used to jump ahead when some of the elements of the sequence aren’t relevant. [https://wiki.python.org/moin/ForLoop]




`
#### use while loops 
* when we want to do an operation while a certain condition is true or alternatively until it becomes false. 
We use for loops 
* when we want to iterate over the elements of the sequence or a range of numbers. 
we use recursion 
* when the problem is best solved in smaller steps and then combining those steps towards a larger solution. 
`

If you're still not sure which is the best tool to choose for a specific problem don't worry, that's normal. As you keep practicing your automation skills, choosing between one option and another will become natural. So next time you find yourself doing the same or similar things over and over again, that's your call to see if you can use a loop to get your computer to do the work for you.

