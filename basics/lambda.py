def add(a, b):
    return a + b

add = lambda a, b: a + b

print(add(10, 20)) # lambda parameters: expression
# lambda parameters: expression

words = ['apple', 'banana', 'kiwi']
words.sort(key=lambda word: len(word))

print(words)