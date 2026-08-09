text = "Python Programming"

print(text.lower())      # "python programming"
print(text.upper())      # "PYTHON PROGRAMMING"
# The .title() method converts the first letter of every word to uppercase and the remaining letters to lowercase.
print(text.title())      # "Python Programming"'
print(text.capitalize()) #Only the first letter of the entire string uppercase

#Strings are Immutable
text = "Python"

text[0] = "J"
# TypeError: 'str' object does not support item assignment

# Cleaning strings
messy = "  hello world  "
print(messy.strip())     # "hello world" (removes whitespace)

price = "$19.99"
print(price.strip("$"))  # "19.99"

# lstrip()
text = "   Python"

print(text.lstrip())
# Remove spaces from left.
# rstrip()
text = "Python     "

print(text.rstrip())

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"

# split()
text = "React Python Node"

print(text.split()) #['React', 'Python', 'Node']

# "separator".join()
skills = ["React","Node","Python"]

print(", ".join(skills)) #"React, Node, Python"

# find()
text = "Python Programming"

print(text.find("Pro")) #  7 (index of first occurrence)

print(text.find("Java")) # -1 (not found)

# index simlar to find but raises error if not found
text = "Python"

print(text.index("t")) # 2 (index of first occurrence)
# print(text.index("z")) # ValueError: substring not found

# isalpha()    
print("Python".isalpha()) # True (only letters)
print("Python3".isalpha()) # False (contains a number) 

# isdigit()
print("123".isdigit()) # True (only digits)
print("123abc".isdigit()) # False (contains letters)

# isalnum()
print("Python3".isalnum()) # True (letters and numbers)
print("Python!".isalnum()) # False (contains special character)

# Slicing (Very Important)
text = "Python"

print(text[0]) # P
print(text[1]) # y
print(text[-1]) # n
print(text[0:3]) # Pyt
print(text[:4]) # Pyth
print(text[2:5]) # tho 
print(text[::-1]) # nohtyP (reverses the string) [start:end:step]
print(text[::3]) # Pto (steps through the string)
# ✅ start → Included
# ❌ end → Excluded
# 🔄 step → Jump size
text = "ABCDEFGHIJKL"
       #0 1 2 3 4 5 6 7 8 9 10 11

print(text[-2:1:-3], '-------') # 
# How Python Slicing WorksString length: ABCDEFGHIJKL has 12 characters (indices 0 to 11, or -12 to -1).Start index (-2): Points to 'K' (index 10).End index (1): Points to 'B' (index 1).Step (-3): Moves backward.Step-by-Step BreakdownFirst character included: index -2 which is 'K'.Next index would be 10 - 3 = 7 (character 'H').Next index would be 7 - 3 = 4 (character 'E').Next index would be 4 - 3 = 1 (stop index 1 is exclusive in Python slices).
# If the step is positive:
text[0:len(text):2]
# Start at the beginning.
# If the step is negative:
# Python interprets it as: text[len(text)-1 : : -2]
# Start at the last character.

# | Step           | Default Start | Default End      |
# | -------------- | ------------- | ---------------- |
# | Positive (`+`) | `0`           | `len(text)`      |
# | Negative (`-`) | `len(text)-1` | Before index `0` |

