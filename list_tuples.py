# Tuple (Immutable)
fruits = ("Apple", "Banana", "Orange")

print(fruits)

# Output:

# ('Apple', 'Banana', 'Orange')

# Now try:

fruits[0] = "Mango"

# Output:

# TypeError: 'tuple' object does not support item assignment

# Python doesn't allow changes to tuples.

# List (Mutable)
fruits = ["Apple", "Banana", "Orange"]

print(fruits)

# Output:

# ['Apple', 'Banana', 'Orange']

# Now try:

fruits[0] = "Mango"

# Output:

# ['Mango', 'Banana', 'Orange']

# Python allows changes to lists.