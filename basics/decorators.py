without decorators, you can achieve similar functionality by defining a function and passing it as an argument to another function. However, decorators provide a more elegant and reusable way to modify or enhance the behavior of functions or methods.

def greet():
    print("Hello")

greet = wrapper(greet)

greet()

# with @
@wrapper # Python automatically does: greet = wrapper(greet) behind the scenes.
def greet():
    print("Hello")

greet()

@wrapper (equivalent to greet = wrapper(greet))