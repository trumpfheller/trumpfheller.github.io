---
title: UCB Python - lecture -  Namespace 
layout: default
---
||[back](./index.html)

---

## Namespace

* Mapping ("Look up table of names") between names to objects in memory
* Esserntially a dictionary
* Scope and namespace are related concepts in Python, but they are not the same.
* refers to a mapping from names to objects. It's like a dictionary where the keys are the names of variables and the values are the objects those names refer to. Namespaces are used to avoid naming conflicts. Python has various namespaces, such as the global namespace (module-level), local namespace (function-level), class namespace, etc.


|| name | value
|| variable name | value
|| function name | function definition

* when a function is defined it is places in the namespace
* function name and function body are added to the namespace table
* when a function is defined, it is placed in the namespace
* the function name is the name, while the function body is the value.
* if the name alreay exists, it will be overwritten. 
* when a function is calles, its name is searched in the namespace.
* If not found in any namespace, a NameError will occur.


### Function Defintion


### Function call


### Scoping rules

* scopes determine the accessibility of names in namespaces
* Python has multiple namespaces. 
* When accesing a name, Python may search through multiple namespaces
* Each namespace is independent of each other
* the starting namespace depends on where we are in the code.
* the starting namespace depends on the scope.
=> when we are outside, it will sarch the global first and then the built-in namespace. If not found it will give us a nameError.
=> if we are inside a function it will search through the local namespace first followed the global namespace, and then the built-in namespace.

### Built-in namespaces

* created when python starts
* reserved for built-in functions(len(), min(), max(), etc.)
* contents do not change.
* Deleted when Python exits.

### Global namespaces

* Created when a program starts
* Scope: outside a function
* Functions, classes, modules, packages, and variables defined in the global context or outside a function are place in the global namespace.
* Deleted when Python exits.

### Global namespaces Example
https://ucbx.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=bd4b31b3-a6ea-4269-9296-af0900bb8250

```python
screenshot
```


### Local namespaces

* Created when a function is entered
* Scope: within a function
* Function parameteres are automatically added
* Deleted when Python exits.

```python
screenshot
```

### Global Statement

* Access a name in the global namepsace
* use the keyword global followed but a variable name
* allows us to modify a global variable within the function

```python
global variable
```

### Local Statement

```python

```

---

### Namespaces and Scope

* Each function defines its own namepsace. If you define a variable called x in a main program and another variable called x  in a function, they refer to different things. But the walls can be breached.
  * global nameapce => global variable

```python
# you can get the value of a global variable from within a function

animal = 'fruitbat'
def print_global():
    print('inside print_global: ', animal)

print('at the top level: ', animal)
# Output
at the top level: fruitbat
print_global()
# Output
inside print_global: fruitbat
```

* if you try to get the value of the global variable and change it within the function, you get an error

page 162



* locals() returns a dictionary of the contents of the local namespace
* globals() returns a dictionary of the contents of the global namespace

```python

```