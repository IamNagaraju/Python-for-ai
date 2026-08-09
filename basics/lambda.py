def add(a, b):
    return a + b

add = lambda a, b: a + b

print(add(10, 20)) # lambda parameters: expression
# lambda parameters: expression

words = ['apple', 'banana', 'kiwi']
words.sort(key=lambda word: len(word))

print(words)

numbers = [1, 5, 3]

result = map(lambda num: num * 2, numbers)
print(result)# <filter object at 0x...>
# Now convert it to a list: print(list(result)) output: []
# Without Lambda
def double(x):
    return x * 2

numbers = [1, 2, 3]

result = map(double, numbers)

print(list(result)) # output: [2, 4, 6]
print(list(result)) # output: [] An iterator can be consumed only once.
numbers = [1, 2, 3]
print('------')
result = map(lambda x: x * 2, numbers)

print(next(result))
print(next(result))
print(list(result))
# Why does Python use iterators instead of lists?
# Memory efficient: It generates values one at a time instead of storing everything.
# Useful for huge datasets: You can process millions of records without loading them all into memory.
numbers = [10, 20]

result = map(lambda x: x + 1, numbers)

print(list(result))
print(next(result))
