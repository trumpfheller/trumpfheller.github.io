---
layout: default
---

> [Strings](./strings.html) || [Variables](./variables.html) || [Lists](./lists.html) || [Tuples](./tuples.html) || [Dictionary](./dictionary.html) ||
> [Control](./control.html) || [Function](./function.html)|| [Files](./files.html) || [Exceptions](./exceptions.html) ||
> [OOP](./oop.html) || [back](./)

***
### Flags

| flag        | what it means          | what it does |
|:-------------|:-----------------:|:------|
| "r" | Read | Default value. Opens a file for reading, error if the file does not exist  |
| "a" | Append  | Opens a file for appending, creates the file if it does not exist  |
| "w" | Write | Opens a file for writing, creates the file if it does not exist  |
| "x" | Create | Creates the specified file, returns an error if the file exists   |
| "t" | Text | Default value. Text mode  |
| "b" | Binary | Binary mode (e.g. images)  |

* To open a file for reading
```python
f = open("demofile.txt")
f = open("demofile.txt", "rt")
```

```python 
f = open("demofile.txt", "r")
print(f.read())
```

```python 
f = open("<path>\welcome.txt", "r")
print(f.read())
```

* append content to the file

```python 
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
```

* overwrite the content

```python 
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
```

```python 
# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

#Create a new file if it does not exist:
f = open("myfile.txt", "w")
```
```python 
# remove a file
import os
os.remove("demofile.txt")
```

```python 
# Check if file exists, then delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
  ```

```python 
# To delete an entire folder
import os
os.rmdir("myfolder")
```

***

## not to self: maybe a link to Exceptions?
