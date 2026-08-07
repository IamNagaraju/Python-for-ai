# Adding values
colors = {"Red","Blue"}

colors.add("Green")

print(colors)

# Output:

{'Red','Blue','Green'}
# Removing
colors.remove("Blue")

print(colors)
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