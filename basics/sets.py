# To create an empty set:
colors = set()
# Adding values
colors = {"Red","Blue"}

colors.add("Green")

print(colors)

# Output:

{'Red','Blue','Green'}
# Removing
colors.remove("Blue")
colors.discard(100)  # discard() doesn't raise an error if the element is not found
print(colors)
# Update
a = {1, 2}

a.update({3, 4})

print(a) # Output: {1, 2, 3, 4}
# Union
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b) # Output: {1, 2, 3, 4, 5}
# Intersection
a = {1, 2, 3}
b = {3, 4, 5}  
print(a & b) # Output: {3}
# Difference
a = {1, 2, 3}
b = {3, 4, 5}
print(a - b) # Output: {1, 2} 
if 3 in a:
    print("Found") # This is one reason sets are used frequently for lookups.
# print(a[0]) # This will raise a TypeError because sets are unordered and don't support indexing.
# Remember the properties of a set:

# ❌ No indexing
# ❌ No slicing
# ❌ No order guarantee
# Important

# Sets don't maintain insertion order (you shouldn't rely on the order of elements).

# Suppose users enter skills:

skills = [
    "React",
    "Node",
    "React",
    "Python",
    "Node"
]

# Remove duplicates:

unique_skills = set(skills)

print(unique_skills)

# Output:

# {'React','Node','Python'}