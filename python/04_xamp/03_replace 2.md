---
title: Python - Examples of Application - Replacing 
layout: default
---

## Examples - Replacing 

### 1. Replacing Items in a List 

* List (mutable: you can change their elements directly by accessing them via their indices)

```python
my_list = [1, 2, 3, 4, 5]

# Replace an item at a specific index
my_list[2] = 10
print("List after replacing an item:")
print(my_list)  # Output: [1, 2, 10, 4, 5]

# Replace multiple items using slicing
my_list[1:4] = [20, 30, 40]
print("\nList after replacing multiple items:")
print(my_list)  # Output: [1, 20, 30, 40, 5]
```

* Use indexing `(my_list[index] = new_value)` to directly replace an item or slicing `(my_list[start:end] = new_list)` to replace multiple items.

### 2. Replacing Items in a Set

```python
# Original set
my_set = {1, 2, 3, 4, 5}

# Remove an item and add a new item
my_set.remove(3)
my_set.add(10)
print("Set after replacing an item:")
print(my_set)  # Output: {1, 2, 4, 5, 10}
```

* Since sets are unordered and do not support indexing, you typically remove the old item with `remove()` and add the new item with `add()`.

### 3. Replacing Items in a Dictionary

```python
# Original dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Replace value for a specific key
my_dict['b'] = 20
print("Dictionary after replacing an item:")
print(my_dict)  # Output: {'a': 1, 'b': 20, 'c': 3}

# Add a new key-value pair
my_dict['d'] = 4
print("\nDictionary after adding a new item:")
print(my_dict)  # Output: {'a': 1, 'b': 20, 'c': 3, 'd': 4}

# Remove an item by key
del my_dict['a']
print("\nDictionary after deleting an item:")
print(my_dict)  # Output: {'b': 20, 'c': 3, 'd': 4}

```

* Replace items by assigning a new value to an existing key `(my_dict[key] = new_value)`. You can also add new key-value pairs or delete existing ones using del statement.

### 4. Replacing Items in a tuple

```python
# List of dictionaries representing students' information
students = [
    {'id': 1, 'name': 'Alice', 'grade': 'A'},
    {'id': 2, 'name': 'Bob', 'grade': 'B'},
    {'id': 3, 'name': 'Charlie', 'grade': 'C'}
]

# Function to replace/update student information based on ID
def update_student_info(student_list, student_id, new_name, new_grade):
    for student in student_list:
        if student['id'] == student_id:
            student['name'] = new_name
            student['grade'] = new_grade
            break  # Assuming IDs are unique, we can stop iterating once we find the student

# Update student with ID 2 to change their name and grade
update_student_info(students, 2, 'Barbara', 'A')

# Print updated list of students
print("Updated list of students:")
for student in students:
    print(student)
```

### 5. Replacing Items in a tuple

* while you cannot directly replace items in a tuple due to its immutability, you can achieve similar results by creating new tuples that include the desired modifications alongside the original elements. 

```python
# Original tuple
my_tuple = (1, 2, 3, 4, 5)

# Creating a new tuple with a different item at a specific index
new_tuple = my_tuple[:2] + (10,) + my_tuple[3:]
print("New tuple after 'replacing' an item:")
print(new_tuple)  # Output: (1, 2, 10, 4, 5)

# Another example: replacing multiple items
new_tuple = my_tuple[:1] + (20, 30) + my_tuple[3:]
print("\nNew tuple after 'replacing' multiple items:")
print(new_tuple)  # Output: (1, 20, 30, 4, 5)
```

* Tuple Immutability: As tuples are immutable, you cannot modify them directly. Instead, you create a new tuple with the desired changes.

* Creating a New Tuple: To "replace" an item in a tuple, you slice the original tuple into parts before and after the item you want to replace, then concatenate these parts with the new item or items enclosed in parentheses ( ).

* Tuple Concatenation: Use tuple slicing `(my_tuple[start:end])` and tuple concatenation `(+)` to create a new tuple that appears as if items have been replaced.







```python

```




```python

```
