
# Variables & Datatypes

## Variables In Python
Variables: A variable is a named storage location that can hold a value. In Python, you can create a variable by assigning a value to it, like this:

x = 5

In this example, "x" is a variable that holds the value 5.

### Rules for defining a variable name
1. A variable name can contain alphabets, digits and underscore
2. A variable name only starts with an alphabets and underscore
3. A variable name can't start with a digits
4. No while space is allowed to be used inside a variable name

### Reserved Keywords
Keywords: Keywords are special reserved words that have a specific meaning in Python. They are used to define the structure of your program and cannot be used as variable names. Some examples of keywords in Python are "if", "for", "while", and "import".

### Identifiers
Identifiers: Identifiers are names used to identify variables, functions, classes, and other objects in Python. They can be any combination of letters, numbers, and underscores, but they cannot start with a number or contain spaces. For example, "my_variable" is a valid identifier in Python.

It's important to understand these concepts when writing Python code, as they form the foundation of the language and help you organize and structure your programs.


## Datatypes In Python

'type()' is a function used to identify the datatype of variable.

```bash
a = 55
print(type(a))
```

Python has a wide range of built-in data types that can be used to store and manipulate data.

1. Int: Stores integers (whole numbers).
```bash
my_number = 5 # my_number is an integer with the value 5
```

2. Float: Stores floating-point numbers (numbers with decimals).
```bash
my_float = 3.14 # my_float is a floating-point number with the value 3.14
```

3. String: Stores text as a series of characters.
```bash
my_string = "Hello, world!" # my_string is a string containing the text "Hello, world!"
```

4. List: Stores an ordered collection of items.
```bash
my_list = [1, 2, 3, 4, 5] # my_list is a list containing the integers 1 through 5
```

5. Tuple: Stores an unchangeable collection of items.
```bash
my_tuple = ("apple", "banana", "orange") # my_tuple is a tuple containing three strings
```

6. Set: Stores an unordered collection of unique items.
```bash
my_set = {1, 2, 3} # my_set is a set containing the integers 1, 2, and 3
```

7. Dictionary: Stores key-value pairs, where each key is associated with a value.
```bash
my_dict = {
    "Name": "Rohan",
    "Age": 34,
    "Salary": 20000.34
}
```

8. Boolean: Stores true or false values.
```bash
is_even = True # is_even is a boolean with the value True
```
