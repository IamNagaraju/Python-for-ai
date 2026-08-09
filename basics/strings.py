age = 25
message = "I am " + str(age) + " years old"
print(message)  # I am 25 years old

# message = "I am " + age + " years old"
# TypeError: can only concatenate str (not "int") to str

# Wrong
result = "Age: " + 25  # TypeError!

# Right - convert number first
result = "Age: " + str(25)