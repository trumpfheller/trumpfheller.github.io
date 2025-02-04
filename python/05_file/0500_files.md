---
title: Python - Files 
layout: default
---

## Files

* Define files
* Text Files
* Binary Files
* Directories
* File Paths
* File Referencing

### Define files

* Resource for storing data
* Stored as a one-dimensional array byte format (giant string)
* most data is generated externally
* allows easy exchange of data

Types of files: Text files and Binary files

### Text Files

* human readable
* consists mainly of alphanumeric characters
* Unicode enables non-English characters

### Binary Files

* has specific formats and usually, we can just download specialized modules to deal with them.
* Application readable data (usually not human readable, ther are non-visible characters)
* no limited to cisible characters
* can contain pictures, sound, encrypted data, executable code, etc..

### Directories

* containers of files
* also known as folders
* organized in a hierarchy
* location of program started is the current working directory (this is the directory from which a python program is started.)

### File Paths

* location of a file in a file system 
* String if directories and the filename
* Directories are indicated nby trailing forward slash (/)
* a single forward slash (/) refers to the top-level directory

### File Referencing

* can be specified in three ways: 
  * filename only
  * absolute path format
  * relative path format

  * filename only:
    * Reference just the filename itself
    * assumes file is in the current working directory

  * absolute path format:
    * Complete pathname and the filename
    * Slash character (/) is the directory separator
    * might not work on another system

  * relative path format
    * partial pathname and the filename
    * Current working directory part can be omitted

---

> [back](./index.html)

