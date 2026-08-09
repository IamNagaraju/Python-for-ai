def greet():
    print("Hello")

greet()

# Keyword Arguments
def introduce(name, age):
    print(name, age)

introduce(age=30, name="Naga") # Naga 30

# Default Arguments
def introduce(name, age=18):
    print(name, age)

introduce("Naga")


def add(a, b):
    return a + b

print(add(b=20, a=10))

def sum(*numbers):
    print(numbers)

print(sum(5,10))

def sum(name, *numbers):
    print(name)
    print(numbers)

sum("Naga", 10, 20) # Naga (10, 20)
# But if you call: sum()  TypeError: missing 1 required positional argument: 'name'

# Tuple of immutable values
def test(*numbers):
    print(numbers)

    numbers[0] = 100 # TypeError: 'tuple' object does not support item assignment

# Create a new tuple
# You don't know how many positional arguments the caller will pass.
def test(*numbers):
    numbers = numbers + (100,)
    print(numbers)

test(1, 2, 3) # (1, 2, 3, 100)
# The objects inside the tuple may still be mutable.

def test(*args):
    args[0]["age"] = 31
    print(args)

employee = {
    "name": "Naga",
    "age": 30
}

test(employee)

print(employee)

def user(**details):
    print(details)

user(name="Naga", age=30, city="Hyderabad")
print('-------------')

def demo(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

demo(
    10,
    20,
    30,
    name="Naga",
    age=30
)

employee = {
    "name": "Naga",
    "age": 30
}

introduce(**employee) # Python automatically does:  introduce(name="Naga", age=30)