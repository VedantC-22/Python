a = 1 #variable a - Integer
b = 2.12 #variable b - Floating point number

print(a + b)

name = "Vedant" #name string
print(name)
print(type(name)) #<class 'str'>

bool = False #boolean variable
print(bool)
print(type(bool)) #<class 'bool'>


# In Python, None is a special constant that represents the absence of a value or a null value. 
# It is similar to null in other languages like JavaScript or NoneType in some programming concepts
n = None
print(n)
print(type(None)) #<class 'NoneType'>

# None in Default Arguments
# You can use None as a default argument in functions:
def greet(name=None):
    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!


# Logical operators
print("--------Truth Table--------")
c = True or False
print(c)

d = True and False
print(d)

print(not(False))


print("-------TypeCasting--------")
# Typecasting (or type conversion) in Python is the process of converting one data type into another. 
# Python supports both implicit and explicit type conversion.

f = 53.65
g = int(f)
print(g)
print(type(g))

h = str(f)
print(h)
print(type(h))

i = "22.22"
print(i)
print(type(i))

j = float(i)
print(j)
print(type(j))

# print(bool(None))       # Output: False
# print(bool("Hello")) # Output: True
# print(bool([]))      # Output: False


#  Implicit Typecasting (Automatic Conversion)
# Python automatically converts one data type to another when no data loss occurs.

# a = 5       # int
# b = 2.5     # float
# c = a + b   # int + float → float  float has a higher precision.

# print(c)       # Output: 7.5
# print(type(c)) # Output: <class 'float'> 

z = 5 % 2
print(z)

# Notes

# ### **Operators in Python**
# Operators in Python are symbols that perform operations on variables and values. Python supports several types of operators:

# ---

# ## **1. Arithmetic Operators**
# Used for mathematical calculations.

# | Operator | Description | Example (`a = 10, b = 3`) | Output |
# |----------|------------|-----------------|--------|
# | `+`  | Addition | `a + b`  | `13` |
# | `-`  | Subtraction | `a - b`  | `7` |
# | `*`  | Multiplication | `a * b`  | `30` |
# | `/`  | Division | `a / b`  | `3.3333` |
# | `//` | Floor Division (integer result) | `a // b` | `3` |
# | `%`  | Modulus (remainder) | `a % b`  | `1` |
# | `**` | Exponentiation (power) | `a ** b` | `1000` |

# ---

# ## **2. Comparison Operators**
# Used to compare values, returns `True` or `False`.

# | Operator | Description              | Example (`a = 10, b = 3`) | Output |
# |----------|--------------------------|---------------------------|--------|
# | `==`     | Equal to                 | `a == b`                  | `False`|
# | `!=`     | Not equal to             | `a != b`                  | `True` |
# | `>`      | Greater than             | `a > b`                   | `True` |
# | `<`      | Less than                | `a < b`                   | `False`|
# | `>=`     | Greater than or equal to | `a >= b`                  | `True` |
# | `<=`     | Less than or equal to    | `a <= b`                  | `False`|

# ---

# ## **3. Logical Operators**
# Used to combine conditional statements.

# | Operator | Description                             | Example (`x = True, y = False`) | Output |
# |----------|-----------------------------------------|---------------------------------|--------|
# | `and`    | Returns `True` if both are `True`       | `x and y`                       | `False`|
# | `or`     | Returns `True` if at least one is `True`| `x or y`                        | `True` |
# | `not`    | Reverses the Boolean value              | `not x`                         | `False`|

# ---

# ## **4. Bitwise Operators**
# Used to perform bitwise operations on binary numbers.

# | Operator | Description | Example (`a = 5 (0101)`, `b = 3 (0011)`) | Output |
# |----------|------------|-----------------|--------|
# | `&`  | AND | `a & b` | `1` (0001) |
# | `|`  | OR  | `a | b` | `7` (0111) |
# | `^`  | XOR | `a ^ b` | `6` (0110) |
# | `~`  | NOT | `~a` | `-6` (inverts bits) |
# | `<<` | Left Shift | `a << 1` | `10` (1010) |
# | `>>` | Right Shift | `a >> 1` | `2` (0010) |

# ---

# ## **5. Assignment Operators**
# Used to assign values to variables.

# | Operator | Example        | Equivalent To |
# |----------|----------------|--------------|
# | `=`      | `a = 10`       | `a = 10` |
# | `+=`     | `a += 5`       | `a = a + 5` |
# | `-=`     | `a -= 2`       | `a = a - 2` |
# | `*=`     | `a *= 3`       | `a = a * 3` |
# | `/=`     | `a /= 2`       | `a = a / 2` |
# | `//=`    | `a //= 2`      | `a = a // 2` |
# | `%=`     | `a %= 3`       | `a = a % 3` |
# | `**=`    | `a **= 2`      | `a = a ** 2` |
# | `&=`     | `a &= b`       | `a = a & b` |
# | `|=`     | `a |= b`       | `a = a | b` |
# | `^=`     | `a ^= b`       | `a = a ^ b` |
# | `<<=`    | `a <<= 1`      | `a = a << 1` |
# | `>>=`    | `a >>= 1`      | `a = a >> 1` |

# ---

# ## **6. Identity Operators**
# Used to check if two objects refer to the same memory location.

# | Operator | Description | Example (`a = [1, 2, 3]`, `b = a`, `c = [1, 2, 3]`) | Output |
# |----------|------------|-----------------|--------|
# | `is`   | Returns `True` if both refer to the same object | `a is b` | `True` |
# | `is not` | Returns `True` if they refer to different objects | `a is not c` | `True` |

# ---

# ## **7. Membership Operators**
# Used to check if a value exists in a sequence.

# | Operator | Description                                    | Example (`x = [1, 2, 3]`) | Output |
# |----------|------------------------------------------------|---------------------------|--------|
# | `in`     | Returns `True` if value is in the sequence     | `2 in x`                  | `True` |
# | `not in` | Returns `True` if value is NOT in the sequence | `5 not in x`              | `True` |
