---
title: Python strings - bigger picture
layout: default
---

## Put it all together

1. creating a list
2. iterating over it to search for a character provided by the user, 
3. including error handling for invalid input or if the character is not found in the list

```python
def char_search():
    # Create a list of 5 characters
    char_list = ['a', 'b', 'c', 'd', 'e']
    
    # Prompt the user to enter a character to search for
    while True:
        try:
            target_char = input("Enter a character to search for: ")
            
            # Check if input is a single character
            if len(target_char) != 1:
                raise ValueError("Please enter exactly one character.")
            
            # Convert to lowercase (assuming case insensitivity)
            target_char = target_char.lower()
            
            # Iterate over the list to search for the target character
            found = False
            for index, char in enumerate(char_list):
                if char == target_char:
                    print(f"Character '{target_char}' found at index {index}")
                    found = True
                    break
            
            # If character is not found, inform the user
            if not found:
                print(f"Character '{target_char}' not found in the list.")
            
            break  # Exit the loop after successful search
        
        except ValueError as ve:
            print(f"Error: {ve}")
            # Continue the loop to prompt the user again

# start the music, DJ!
char_search()
```
