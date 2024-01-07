# Typecasting In Python

Typecasting, or type conversion, is the process of converting a value of one data type to another. Here's some info on typecasting in Python:

### Python supports three types of typecasting:

1. Implicit Typecasting: Python automatically converts data types in certain cases, like when you assign a value of one type to a variable of another type.

2. Explicit Typecasting: You can explicitly convert a value from one type to another using built-in functions like int(), float(), and str().


#### Example of Implicit Typecasting:

```bash
# Implicit Typecasting
a = 4.6
b = 5

c = a + b

# Here Python automatically converts data types of variable 'b' from 'int' to 'float' so that it will do addition of floats

print(c)
```

##### Output: 9.6 (result in float)

#### Example of Explicit Typecasting:

```bash
# Explicit Typecasting
a = "4"
b = 5

c = int(a) + b

# Here we change the datatype of variable 'a' so that we can do addtion of both numbers.

print(c)
```

##### Output: 9
