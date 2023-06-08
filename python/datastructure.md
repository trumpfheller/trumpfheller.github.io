## Sequences & Data Structure

## Types of Data Structures: 
    - container#1: Lists, 
    - container#2: Tuples, 
    - container#3: Sets, 
    - container#4: Dictionaries

[docs](https://docs.python.org/3/tutorial/datastructures.html)

**Lists**: 
- are **ordered**, an ordered collection of items/objects (an **innate** characteristic of the list).
    - the items have a defined order, 
    - that order will not change.
    - lists with the same elements in a different order are not the same.
- are sequences of elements of any type (like complex objects)
    - Functions
    - Classes
    - Module
- may contain any number of elements/objects (constrained by the computer’s memory, of course), of any type(can store heterogeneous data types). 
- Does not to be unique: same object may occur any number of times.
- are **mutable**, meaning you can add, remove, or modify elements in-place.

**Tuples**
- similar to lists but are immutable, meaning they cannot be modified once created. 
- They are commonly used to represent fixed collections of related data.
- are sequences of elements of any type 
- are immutable.
	
**Dictionaries**
- are key-value pairs and provide a way to store and retrieve data based on a unique key. 
- are also known as associative arrays or hash maps.
- are useful for mapping one value to another and are highly efficient for data retrieval.

**Sets**
- unordered collections of unique elements. 
- useful when you want to eliminate duplicate values or perform set operations such as union, intersection, or difference.

**Strings**
- Although not a traditional data structure, strings are fundamental in programming. 
-  are sequences of characters and provide methods for manipulating and working with textual data.
- are sequences of characters 
- are immutable. 


***

	
- Methods used
    - iterating over them using **for-loops**, 
    - indexing using the **len** function to find the length of the sequence, 
    - using **plus** to concatenate two sequences and 
    - using **in** to verify if the sequence contains an element. 

- Sequences have similar properties, like 
    * being able to iterate over them using **for** loops; 
    * support **indexing**; 
    * using the **len** function to find the length of the sequence; 
    * using the **plus** operator + in order to concatenate; and 
    * using the **in** keyword to check if the sequence contains a value.

- Common sequence operations
    * len(sequence) 
    	* Returns the length of the sequence
    * for element in sequence 
    	* Iterates over each element in the sequence
    * if element in sequence 
    	* Checks whether the element is part of the sequence
    * sequence[i] 
    	* Accesses the element at index i of the sequence, starting at zero
    * sequence[i:j] 
    	* Accesses a slice starting at index i, ending at index j-1. If i is omitted, it's 0 by default. If j is omitted, it's len(sequence) by default.
    * for index, element in enumerate(sequence) 
    	* Iterates over both the indexes and the elements in the sequence at the same time


