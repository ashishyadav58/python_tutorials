
# Modules, Pip & Comments

## Modules
In Python, a module is a file containing Python code that can be imported and used by other Python programs. Modules are a way to organize and reuse code in Python, and they help keep your code clean and organized.

Types of modules in Python:

1. built-in modules: Built-in modules are modules that come pre-installed     with Python, such as the math or os modules.

2. user-defined modules: User-defined modules are modules that you create yourself, either by writing your own Python code in a file or by importing code from other sources.

```bash
import math # built in module

square = math.sqrt(9)
print(square)

```

```bash
import requests # external module

url = "https://www.example.com"
get = requests.get(url)
print(get)

```

## Pip

Pip stands for "Preferred Installer Program", and it's a package manager for Python. It's used to install and manage additional Python packages and libraries that you might need for your projects.

## Comments

Comments are a way to add notes and annotations to your Python code. They are ignored by the Python interpreter, but they can be really useful for you or other developers who might be working on your code.

Types of Comments in Python:

1. Single-line comments start with a hash symbol (#) and continue until the end of the line

For example:
```bash
# This is single line comments
```

2. Multi-line comments are created by using triple quotes (""") at the beginning and end of the comment.

For example:
```bash
"""
This is
multi-line
comments
"""
```