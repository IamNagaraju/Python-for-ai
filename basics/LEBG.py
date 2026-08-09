# This is the first rule of LEGB
# Python follows this order when looking for a variable:
# L → Local
# E → Enclosing
# G → Global
# B → Built-in

# Reading a global variable is allowed. Assigning to it inside a function creates a local variable unless you use global.
x = 10

def test():
    x = x + 1
    print(x)

test()
# UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
# Python sees: x = x + 1 and immediately decides: "x is a local variable because you're assigning to it."
# internally, Python treats it like:
def test():
    # x is considered local

    x = x + 1
# The moment you assign to x anywhere in the function, x becomes local for the entire function.
# How do we modify the global variable?
x = 10

def test():
    global x
    x = x + 1
    print(x)

test()
print(x)

def outer():
    x = 10

    def inner():
        nonlocal x
        x = x + 1
        print(x)

    inner()
    print(x)

outer()
| Keyword    | Modifies                    |
| ---------- | --------------------------- |
| Nothing    | Creates a local variable    |
| `global`   | Global variable             |
| `nonlocal` | Enclosing function variable |
