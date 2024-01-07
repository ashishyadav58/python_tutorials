a = "40"
b = 3

c = a + b
print(c)

# Implicit Typecasting
a = 4.6
b = 5

c = a + b

# Here Python automatically converts data types of variable 'b' from 'int' to 'float' so that it will do addition of floats

print(c)

# Explicit Typecasting
a = "4"
b = 5

c = int(a) + b

# Here we change the datatype of variable 'a' so that we can do addtion of both numbers.

print(c)

# In this case we can't convert the datatype of variable d because it is a text not numeric
d = "Rohan"

print(int(d))