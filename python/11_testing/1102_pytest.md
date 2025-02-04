---
title: Testing - pytest
layout: default
---

## pytest
> for verifying how different parts of your application work together (integration testing)

### pytest vs. unittest

* unittest: Python's built-in testing framework; good for basic tests, but can get verbose for more complex scenarios.
* pytest: more feature-rich testing framework; easier to use, offers more powerful features like fixtures and parametrization.
* Start with unittest and as your projects grow or you need more advanced features, consider migrating to pytest.

* features: 
  * Fixtures: Reusable setup and teardown code for tests.
  * Parametrization: Running the same test with different inputs.
  * Mocking and patching: Controlling the behavior of external dependencies during testing.
  * Detailed reports: Easy-to-understand reports that highlight test failures and provide helpful information.

### Install pytest

```bash
pip install pytest
```

### Start with Basic Tests
* Create a test file: Use a filename ending with `_test.py`.
* Write a test function: Use the `test_` prefix for your test functions.
* Assertions: Use Python's built-in `assert` statement to check expected outcomes.



1. Unit Testing
Purpose: To verify that individual units of code (e.g., functions, methods) work as expected.
Example: Testing a function that calculates the factorial of a number.

```python
# test_factorial.py

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
```

2. Integration Testing
Purpose: To test the integration of different units/modules and ensure they work together as intended.
Example: Testing the interaction between a database module and an API.

```python
# test_integration.py

def get_data_from_db():
    # Simulate fetching data from a database
    return {"id": 1, "name": "Alice"}

def get_data_from_api():
    # Simulate fetching data from an API
    return {"id": 1, "name": "Alice"}

def test_integration():
    db_data = get_data_from_db()
    api_data = get_data_from_api()
    assert db_data == api_data
```

3. Functional Testing
Purpose: To test the functionality of the software from the user's perspective.
Example: Testing if a user can successfully log in to an application.

```python
# test_login.py

def login(username, password):
    if username == "user" and password == "pass":
        return True
    return False

def test_login():
    assert login("user", "pass") is True
    assert login("user", "wrong_pass") is False
```

4. Regression Testing
Purpose: To ensure that new changes or bug fixes do not break existing functionality.
Example: Running a suite of tests to verify that previous functionalities still work after adding a new feature.
```python
# test_regression.py

def add(a, b):
    return a + b

def test_addition():
    assert add(1, 1) == 2
    assert add(2, 2) == 4
```

5. Smoke Testing
Purpose: To perform a preliminary check to see if the major functionalities of the application are working.
Example: Running a few critical tests to verify that the application is up and running.

```python
# test_smoke.py

def test_basic_functionality():
    assert 1 + 1 == 2
    assert "Hello".upper() == "HELLO"
```

6. Performance Testing
Purpose: To check the performance and speed of the application.
Example: Measuring the execution time of a function.

```python
# test_performance.py
import time

def slow_function():
    time.sleep(2)
    return True

def test_slow_function(benchmark):
    result = benchmark(slow_function)
    assert result is True
```

7. Test Automation
Purpose: To automate repetitive testing tasks and run tests as part of a Continuous Integration/Continuous Deployment (CI/CD) pipeline.
Example: Using pytest in a CI/CD setup like Jenkins, Travis CI, or GitHub Actions.

```yaml
# .github/workflows/ci.yml

name: CI

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest
    - name: Run tests
      run: |
        pytest
```

### Key Benefits of Using pytest
1. Simple Syntax: Easy-to-read and write test cases using plain functions and assert statements.
2. Powerful Fixtures: Manage test setup and teardown with reusable fixtures.
3. Parameterization: Run tests with multiple sets of inputs using @pytest.mark.parametrize.
4. Rich Plugin Architecture: Extend functionality with a wide range of plugins.
5. Detailed Reports: Provides detailed test reports and error messages.
6. Integration with CI/CD: Seamless integration with CI/CD tools to automate testing.

### When to Use pytest

* Whenever you need to write and run automated tests for your code.
* When you want a powerful and flexible testing framework with minimal boilerplate.
* If you need to manage complex test setups and dependencies.
* For both small projects and large-scale applications with extensive test suites.

## basic test functions using pytest

### Example 1: Simple Test Function

```python
#  checks if two values are equal.
def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 2 - 1 == 1
# in cmd line: pytest test_example.py
```



### Example 2: Test Function with Multiple Assertions

*  test function with multiple assertions

```python
# test_example.py

def test_math_operations():
    assert 1 + 1 == 2
    assert 2 * 2 == 4
    assert 5 - 3 == 2
    assert 9 / 3 == 3
```




### Example 3: Test Function Using a Helper Function

* using a helper function within a test

```python
# helper.py

def add(a, b):
    return a + b

# test_example.py

from helper import add

def test_add():
    result = add(1, 2)
    assert result == 3
```

### Example 4:  Test Function with pytest Fixtures

*  pytest fixtures to set up any required state before the test runs.

```python
import pytest

@pytest.fixture
def numbers():
    return 1, 2, 3

def test_sum(numbers):
    a, b, c = numbers
    assert a + b + c == 6

def test_product(numbers):
    a, b, c = numbers
    assert a * b * c == 6
```

### Example 5: Parameterized Test Functions

* using the `@pytest.mark.parametrize` decorator to run a test with multiple sets of inputs

```python
# test_example.py

import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (2, 3, 5),
    (4, 5, 9),
])
def test_addition(a, b, expected):
    assert a + b == expected
```

