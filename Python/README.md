# Python Learning Roadmap

A structured course guide for learning Python from the first program through object-oriented, GUI, and concurrent programming.

> **Course focus:** Build strong Python fundamentals, practice the language's core abstractions, and finish with real application concepts such as file handling, GUI development, and multi-threading.

## At A Glance

| Level | Coverage |
| --- | --- |
| Foundations | Python, installation, interpreter architecture, syntax, variables, operators, input, and type conversion |
| Core Language | Conditions, loops, strings, lists, tuples, sets, dictionaries, and comprehensions |
| Problem Solving | Functions, decorators, closures, functional tools, modules, packages, and file I/O |
| Application Development | Object-oriented programming, exception handling, Tkinter GUI programming, and multi-threading |

## Course Contents

### 1. Introduction to Python

- Why Python and where it is used
- Python implementations: CPython, Jython, IronPython, and PyPy
- Python versions and installation
- Interpreter architecture
- Python bytecode compiler and Python Virtual Machine (PVM)

### 2. Writing and Executing Python Programs

- Interactive mode and script mode
- Running programs from a text editor and command window
- Using IDLE Editor and IDLE Shell
- Understanding the `print()` function
- Explicitly compiling a Python program

### 3. Python Language Fundamentals

- Character set, keywords, comments, variables, and literals
- Operators
- Reading input from the console
- Parsing strings into `int` and `float`

### 4. Conditional and Looping Statements

- `if`, `if-else`, and `if-elif` statements
- Nested conditional statements
- `while` and `for` loops
- Nested loops
- `pass`, `break`, and `continue`

### 5. Standard Data Types

- Numeric and Boolean types: `int`, `float`, `complex`, and `bool`
- `NoneType`
- Sequence types: `str`, `list`, `tuple`, and `range`
- Mapping and set types: `dict`, `set`, and `frozenset`

### 6. String Handling

- String fundamentals and representations
- Unicode strings
- String functions and methods
- Indexing and slicing
- String formatting

### 7. Python Lists

- Creating and accessing lists
- Indexing and slicing
- List methods
- Nested lists
- List comprehensions

### 8. Python Tuples

- Creating and accessing tuples
- Tuple indexing
- Tuple immutability

### 9. Sets and Frozensets

- Creating sets
- Iterating over sets
- Set methods
- Working with `frozenset`

### 10. Python Dictionaries

- Creating dictionaries
- Accessing and updating values
- Dictionary methods
- Iterating over dictionaries
- Dictionary comprehensions

### 11. Functions

- Defining and calling functions
- Types of functions
- Function arguments:
  - Positional and keyword arguments
  - Default and non-default arguments
  - Arbitrary and keyword-arbitrary arguments
- Return statements
- Nested functions
- Functions as arguments and return values
- Decorators and closures
- Anonymous functions with `lambda`
- `map()`, `filter()`, `reduce()`, and `any()`

### 12. Modules and Packages

- Why modules are useful
- Script versus module
- Importing modules
- Standard-library versus third-party modules
- Why packages are useful
- Using the `pip` package manager

### 13. File I/O

- Introduction to file handling
- File modes
- File-related functions and methods
- Using the `with` statement

### 14. Object-Oriented Programming

- Procedural programming versus object-oriented programming
- OOP principles
- Defining classes and creating objects
- Inheritance
- Encapsulation
- Polymorphism
- Abstraction
- Garbage collection
- Iterators and generators

### 15. Exception Handling

- Syntax errors versus exceptions
- Exception-handling keywords: `try`, `except`, `finally`, `raise`, and `assert`
- Types of `except` blocks
- User-defined exceptions

### 16. GUI Programming with Tkinter

- Introduction to Tkinter
- Tkinter widgets
- Layout managers
- Event handling
- Displaying images

### 17. Multi-Threading Programming

- Multi-processing versus multi-threading
- Why threads are needed
- Creating child threads
- Thread-related functions and methods
- Thread synchronization and locking

## Topic Examples

### Variables, Input, and Conditions

```python
name = input("Enter your name: ")
score = float(input("Enter your score: "))

if score >= 60:
  result = "Pass"
else:
  result = "Try again"

print(f"{name}: {result}")
```

### Loops and List Comprehension

```python
numbers = range(1, 11)
squares = [number ** 2 for number in numbers if number % 2 == 0]

for square in squares:
  print(square)
```

### Dictionaries and Functions

```python
def average_marks(marks: dict[str, int]) -> float:
  return sum(marks.values()) / len(marks)


student = {"name": "Aman", "Python": 88, "SQL": 82}
marks = {subject: score for subject, score in student.items()
     if subject != "name"}

print(student["name"])
print(f"Average: {average_marks(marks):.1f}")
```

### File I/O and Exception Handling

```python
try:
  with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
except FileNotFoundError:
  content = "No notes file found."

print(content)
```

### Object-Oriented Programming

```python
class Student:
  def __init__(self, name: str, score: int):
    self.name = name
    self.score = score

  def summary(self) -> str:
    return f"{self.name}: {self.score}%"


student = Student("Aman", 88)
print(student.summary())
```

### Threading

```python
from threading import Thread


def print_status(task: str) -> None:
  print(f"Finished: {task}")


worker = Thread(target=print_status, args=("Python practice",))
worker.start()
worker.join()
```

## Learning Outcomes

By the end of this course, you should be able to:

- Write and execute Python programs in interactive and script modes.
- Use Python's built-in data types and control-flow statements confidently.
- Process strings and collections with indexing, slicing, methods, and comprehensions.
- Design reusable functions and use higher-order programming techniques.
- Organize code with modules and packages and work with installed libraries.
- Read from and write to files safely.
- Model problems using classes and the principles of object-oriented programming.
- Handle expected and unexpected errors with appropriate exception strategies.
- Build basic desktop interfaces with Tkinter.
- Understand threads, synchronization, and the difference between threading and multiprocessing.

## Suggested Study Flow

1. Complete the foundations and write small programs using input, output, conditions, and loops.
2. Practice each data type with short exercises focused on creation, access, mutation, and iteration.
3. Refactor repeated solutions into functions and then explore decorators, closures, and functional tools.
4. Build a small file-based application using modules, packages, and exception handling.
5. Finish with an object-oriented project, followed by a simple Tkinter interface or threaded utility.

## Folder Resources

- [`SYLLABUS.txt`](SYLLABUS.txt) - Original course outline.
- [`D_Notes.ipynb`](D_Notes.ipynb) - Notebook for examples and interactive practice.
- [`Test.py`](Test.py) - Standalone Python practice program.
- [`Lectures/`](Lectures/) - Recorded lecture resources.

## Running Python Examples

From the repository root, run a Python script with:

```bash
python Python/Test.py
```

Use Python 3 and open the notebook with a Python 3 kernel when working through the interactive exercises.
