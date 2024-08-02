Python - Variable Annotations

Overview
Variable annotations in Python provide a way to explicitly declare the expected data types of variables. Introduced in Python 3.6 via PEP 526, variable annotations enhance code readability, support static type checking, and improve development tools' ability to understand the code.

Purpose
The primary purposes of variable annotations are:

Documentation: Clearly document the intended use of variables.
Static Type Checking: Enable tools like mypy to perform static type checks and catch potential type errors.
IDE Support: Enhance features like autocompletion, refactoring, and code analysis in integrated development environments (IDEs).

Basic Syntax
The basic syntax for variable annotations is:

variable_name: type = value

variable_name: The name of the variable.
type: The expected type of the variable.
value: The initial value of the variable (optional).

Examples
Simple Annotations
x: int = 10
name: str = "Alice"
is_active: bool = True

Without Initial Value
x: int
name: str
is_active: bool

Annotations can be used without assigning an initial value. In such cases, the variables are initialized with a value later.

Complex Annotations
from typing import List, Dict

numbers: List[int] = [1, 2, 3]
user_info: Dict[str, str] = {"name": "Alice", "email": "alice@example.com"}

Annotations for more complex data structures can be specified using types from the typing module.

Advanced Usage
Function Annotations
Variable annotations are often used alongside function annotations to specify parameter and return types.

from typing import List

def greet(name: str) -> str:
    return f"Hello, {name}!"

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

Class Annotations
Variable annotations can also be used within classes to specify the types of instance variables.

class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

Using mypy for Type Checking
mypy is a static type checker for Python that can validate your code based on the type annotations.

Installation
Install mypy using pip:

pip install mypy

Running mypy
To check your code, run mypy with the filename:

mypy your_script.py

Example
Consider the following script:

def add(a: int, b: int) -> int:
    return a + b

x: int = 10
name: str = "Alice"

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(add(x, 5))
print(greet(name))

If there is a type error, such as passing a string where an integer is expected:

print(add(x, "5"))  # Error: Argument 2 to "add" has incompatible type "str"; expected "int"

Running mypy on this script:

mypy your_script.py
Will produce an output indicating the type error:

your_script.py:11: error: Argument 2 to "add" has incompatible type "str"; expected "int"

Conclusion
Variable annotations in Python provide a powerful way to document and enforce type expectations in your code. By using type annotations and tools like mypy, you can enhance code readability, catch errors early, and improve overall code quality.