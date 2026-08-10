try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:
    print("Cannot divide by zero")

print("Program Finished")
# Catching Specific Exceptions
try:
    number = int("abc")

except ValueError:
    print("Invalid Number")

# try:
#     value = int(input())

#     print(10 / value)

# except ValueError:
#     print("Please enter a number")

# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:
#     print("Done")

# Real AI Example
# try:
#     response = client.responses.create(...)

# except Exception as e:
#     print("OpenAI API Error:", e)

# Never do this
# try:
#     ...
# except:
#     pass # Because it hides all errors.

# do this instead: except Exception as e:
#     print(e)
# try
#    ↓
# Exception?
#    │
#  ┌─┴─────────┐
#  │           │
# No          Yes
#  │           │
# else      except
#  └────┬──────┘
#       ↓
#    finally
print('------')
def test():
    try:
        return 10

    finally:
        return 20

print(test(),'====')
def test():
    try:
        print("A")
        return 10

    finally:
        print("B")

print(test())
try:
    age = -5

    if age < 0:
        raise ValueError("Age cannot be negative")

    print(age)

except ValueError as e:
    print("Error:", e)
# Return value = 10

# ↓

# Wait...

# ↓

# Is there a finally block?

# ↓

# Yes

# ↓

# Execute finally first