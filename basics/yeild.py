def test():
    print("A")
    yield 10

    print("B")
    yield 20

    print("C")

g = test()

print(next(g))
print(next(g))
# print(next(g))
print('------')
def test():
    for i in range(3):
        yield i

g = test()

print(list(g))
print(list(g))