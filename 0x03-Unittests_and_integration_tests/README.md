1. unittest — Unit Testing Framework
What is it?
unittest is a built-in Python module used for testing your code. It helps you create tests to check whether different parts (or "units") of your code are working as expected.

How does it work?
You write test cases by defining methods inside a class that inherits from unittest.TestCase. These methods usually start with test_. When you run the tests, unittest will automatically execute these methods and report which tests passed and which failed.

Example:

import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()

2. unittest.mock — Mock Object Library
What is it?
unittest.mock is a part of the unittest module that allows you to create mock objects. Mock objects are fake versions of real objects that you can use in tests to simulate the behavior of complex, slow, or difficult-to-set-up parts of your code.

How does it work?
You can replace parts of your system under test (like functions, methods, or objects) with mock versions that mimic their behavior. This allows you to focus on testing the specific piece of code you're interested in, without worrying about external dependencies.

Example:

from unittest import mock

def get_data():
    return "real data"

def process_data():
    data = get_data()
    return f"Processed {data}"

def test_process_data():
    with mock.patch('__main__.get_data', return_value="mock data"):
        result = process_data()
        assert result == "Processed mock data"

3. How to Mock a Readonly Property with Mock
What is it?
A readonly property is a property in a class that can only be read, not written to. If you need to mock such a property in tests, you can use mock.PropertyMock.

How does it work?
You use mock.PropertyMock to specify the value that should be returned when the readonly property is accessed.

Example:

from unittest import mock

class MyClass:
    @property
    def readonly_property(self):
        return "real value"

def test_readonly_property():
    with mock.patch.object(MyClass, 'readonly_property', new_callable=mock.PropertyMock) as mock_prop:
        mock_prop.return_value = "mocked value"
        obj = MyClass()
        assert obj.readonly_property == "mocked value"

4. parameterized
What is it?
parameterized is a library or feature in testing frameworks that allows you to run the same test with different sets of inputs. This way, you can test multiple scenarios with the same code.

How does it work?
You define the test once and specify the different input values you want to test it with. The framework will then run the test multiple times, once for each set of inputs.

Example:

from parameterized import parameterized
import unittest

class TestMathOperations(unittest.TestCase):
    @parameterized.expand([
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0)
    ])
    def test_add(self, a, b, expected):
        result = a + b
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

5. Memoization
What is it?
Memoization is a technique used to speed up your code by storing the results of expensive function calls and reusing those results when the same inputs occur again.

How does it work?
When a function is called, its result is saved in a cache (usually a dictionary). If the function is called again with the same arguments, the cached result is returned instead of recalculating it.

Example:

def fib(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 2:
        return 1
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

6. Difference Between Unit and Integration Tests
Unit Tests:

Purpose: Test individual pieces (units) of your code, like functions or methods, in isolation.
Example: Testing if a single function returns the correct result for given inputs.
Focus: Small scope, testing one thing at a time.
Dependencies: Typically, you mock or replace external dependencies.
Integration Tests:

Purpose: Test how different units of your application work together.
Example: Testing how a function interacts with a database.
Focus: Larger scope, ensuring components work together.
Dependencies: Involves real components and systems, like databases, APIs, etc.

7. Common Testing Patterns
Mocking:

What is it?
Creating fake objects or functions to simulate the behavior of real ones. Useful in unit tests to isolate the code being tested.
Example: Mocking a database connection to test a function that retrieves data from the database.

Parametrizations:
What is it?
Running the same test with different inputs or configurations. Helps test various scenarios efficiently.
Example: Testing a sorting algorithm with different types of lists (e.g., empty, already sorted, reverse order).

Fixtures:
What is it?
Predefined setups that prepare your environment or data before running tests. Useful for setting up common test data or configurations.
Example: Creating a temporary database with sample data that will be used across multiple tests.

These concepts are fundamental to understanding how to write and organize tests in Python, ensuring your code is reliable, efficient, and easy to maintain.