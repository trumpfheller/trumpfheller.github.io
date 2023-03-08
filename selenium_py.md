---
layout: default
---

## Open Firefox browser

```python
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://www.google.com")

# next in terminal call it
python3 get_firefox.py

```

## Open Chrome browser

```python
from selenium import webdriver
driver = webdriver.Chrome()
# URL of website
browser.get("https://trumpfheller.github.io/")
# Opening the website
driver.get(url)

# next in terminal call it
python3 get_firefox.py

```


## Finding Elements on the page

### find_element.* methods
- returns a single web object, representing the first element on th epage that matches your query

```python
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("https://trumpfheller.github.io/")
try:
    elem = browser.find.element_by_class_name('Playbook')
    print('Found <%s> element with that class name!' % (elem,tag_name))
except:
    print('Was not able to find an elment with that name.')
```

If no element (Playbook) eistson the page that match the method is looking for, Selenium module raises a NoSuchElement exception. If you do not want this exception to crash your program, add try and except statements to the code.


### find_elements.* methods
- returns a list of WebElement_* objects for every matching element on the page.


| Method name        | web element object/list returned |
|:-------------|:------------------|
| browser.find_element_by_name(name) | Elements that use the CSS class name  |
| browser.find_elements_by_name(name) |   |
| browser.find_element_by_css_selector(selector) | Elements that match the CSS selector  |
| browser.find_elements_by_ |   |
| browser.find_element_by_id(id) | Elements with matching id attribute  |
| browser.find_elements_by_ |   |
| browser.find_element_by_link_text(text) | <a> elements that completely match the text provided  |
| browser.find_elements_by_link_text(text) |  <a> elements that contain the text provided |
| browser.find_element_by_partial_link_text(text) |   |
| browser.find_elements_by_partial_link_text(text)  |   |
| browser.find_element_by_name(name) | Elements with matching name attribute   |
| browser.find_elements_by_name(name) |   |
| browser.find_element_by_tag_name(name) | Elements with matching tag name (case sensitive)   |
| browser.find_elements_by_ |   |


## Filling out and submitting forms
- Selenium has a module for keyboard keys.

```python
from selenium import webdriver
browser = webdriver.Firefox()
browser.get("http://gmail.com/")
emailElem = browser.find_element_bu_id('Email')
emailElem.send_keys('mikeTester@gmail.com')
passwordElem = browser.find_element_by_id('google1234')
passwordElem.send_keys('1234')
passwordElem.submit()

# next in terminal call it
python3 get_firefox.py

```
## Sending special keys

```python


# next in terminal call it
python3 get_firefox.py

```
## Clicking Browser Buttons
```python


# next in terminal call it
python3 get_firefox.py

```

## Take screenshots on Firefox
```python
from selenium import webdriver
from PIL import Image
browser = webdriver.Firefox()
browser.get("http://www.google.com")
try:
    driver.save_screenshot('ss.png')
    screenshot = Image.open('ss.png')
    screenshot.show()
except:
    print('Was not able to take the screenshot.')

# next in terminal call it
python3 get_firefox.py

```
## taking a screenshot on Chrome
```
Open Terminal (Applications/Terminal) and run:
xcode-select -install (prompted to install Xcode Command Line Tools)
sudo easy_install pip
[ORRrrrr just use one of the next]
sudo pip install pillow
pip install pillow
pip install Pillow
```
```python
from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome()
# URL of website
browser.get("https://trumpfheller.github.io/")
# Opening the website
driver.get(url)
try:
    linkElem = browser.find.element_by_link_text('Flow of Initiation')
    linkElem.click()
    print('Was able to land on Flow.')
    driver.save_screenshot("ss.png")
    # Loading the image
    screenshot = Image.open("ss.png")
    # Showing the image
    screenshot.show()
except:
    print('Was not able to take the screenshot.')
```
