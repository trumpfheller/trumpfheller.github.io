---
title: lec_05 String Formatting
layout: default
---

||[back](../index.html)

## String Methods

### Building Strings

* Concatenate operator to combine strings

```python
str(object)
# return a string from a given object
```

* operands must be strings
* Use the strin fuction to convert other types to strings

```python
mean = (1+2+3+4) / 4
print('the aver is: ' + mean + '.')
# Output 
Typeerror: can only concatenate str (not float) to str

print('the aver is: ' + str(mean) + '.')
# Output 
the aver is: 2.5.
```

### Formatted String Literals

* also called formated string literals of f-strings
* use replacemnt fields
  * Placeholders where a vlaue will appear
  * Indicated by {} and a value

```python
mean = (1+2+3+4) / 4
print(f'the aver is: {mean}.')
```

### Format specifiers

* codes to change the appearance of replacement fiuelds
* placed after the value and a colon in the replacement field
  * {value: format_specifier}
* Examples
  * currency
  * floating point
  * width and alignment

```python
,.2f

# , thousands seperator
# .2f two digits after the decimal point
```

```python
price = 12345.6
print(f'the price is: {price}.')
print(f'the price is: {price:,.2f}.')
```

### Floating point

* .[digits]f

```python
pi = 3.14159
print(f'pi with 3 digits: {pi:,.3f}.')x 
```

### Alignment and Width

* <,^,>

```python
city = 'Berkeley'
print(f'|{city:<20}|')
print(f'|{city:^20}|')
print(f'|{city:>20}|')

# Output
|Berkeley           |
|       Berkeley    |
|           Berkeley|
```