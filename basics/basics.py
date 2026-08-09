long_dash = "-" * 30
print(long_dash)
# to check length of string
print(len(long_dash))

is_admin = True
print(is_admin)

# Addition and subtraction
total = 10 + 5     # 15
change = 20 - 7    # 13

# Multiplication and division
area = 6 * 4       # 24
half = 10 / 2      # 5.0 (always returns float)

# Powers
squared = 5 ** 2   # 25
cubed = 2 ** 3     # 8

# Regular division (always float)
result = 10 / 3    # 3.333...

# Integer division (rounds down)
result = 10 // 3   # 3

# Even when dividing evenly
result = 10 / 2
print(result)       # 5.0 (not 5)
print(type(result)) # <class 'float'>

# Use // for integer result
result = 10 // 2    # 5

def add(a, b):
    return a + b

result = add(10,20)

print(result)

# Wrong
million = 1,000,000  # Creates a tuple, not a number!


# Right
million = 1000000    # Hard to read
million = 1_000_000  # Python style