---
title: Python - Strings
layout: default
---

## Strings

* Containers of characters
* Used for communicating to the user
* used for processing data (files, network)

### Characters

* Basic unit of a string
* every letter, digit, symbol and emoji
* have a claue that comes from the Unicode standard

### String literals

* String are immutable

### String Quoates

* single, double
* quotes are also called delimiters
* Now shown when using the print() function

### String literals Examples

* ''hello'
* '42'
* "emoji"

### Special characters

* do not have a single printable representation
* require escape sequence to be invoked

### Escape Sequence

* Started by the backslash character \
* Interpreted when using the print function

### Special characters List

* \\ backslash
* \' single quote
* \" double quote

### Special characters Example

```python
print('Use backslash: \\ to escape a single quote: \'')
```

### Whitespaces

* charcters that are not visible but take up space
* seperators of data, words or lines

### Whitespace characters

* '' space
* \t tab
* \n newline
* \b backspace
* \r line feed

### Whitespace example

```python
print('First:\tGold\nSecond:\tSilver\nThird:\tBronze')
OUTPUT
First: Gold
Second: Silver
Third: Bronze
```

### Data Type properties

|| Data Type   | Container | Mutuable
| numeric | no | no
| string | yes | no
