# Suppose you open a file.
file = open("data.txt", "r")

content = file.read()

file.close()
# But what if an error occurs?
file = open("data.txt", "r")
# Instead of writing:
try:
    content = file.read()
finally:
    file.close()

# Python lets us write:
with open("data.txt", "r") as file:
    data = file.read() 
# The file is automatically closed when the block ends, even if an error occurs.
with open("data.txt", "w") as file:
    print(file.closed)   # False we are in the context manager block means inside the with statement

print(file.closed)    # True we are outside the context manager block means outside the with statement