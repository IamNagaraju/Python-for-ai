
# [expression for item in iterable if condition]
# [true_value if condition else false_value for item in iterable]
numbers = []

for i in range(1,11):
    numbers.append(i)

fomrated_array = [i for i in range(1,6)]
print(fomrated_array)

fomrated_array = [i*i for i in range(1,6)]

# [expression for item in iterable if condition]
fomrated_array = [i for i in range(1,6) if i%2 == 0 ]
# [What you want for each item in collection if condition]

names = ["naga", "raju", "python"]
capitalized_names = [name.upper() for name in names]
print(capitalized_names,'===')

numbers = [1, 2, 3, 4, 5, 6]

res = [num for num in numbers if num % 2 != 0]

words = ["apple", "banana", "kiwi", "mango"]

words_length = [len(word) for word in words]
print(words_length)

# even or odd
result = ["Big" if num > 3 else "small" for num in numbers]
print(result, '****')

# captialize
names = ["naga", "raju", "python", "ai"]
result = [name.upper() if len(name) > 4 else name.lower() for name in names]
print(result)

names = ["naga", "", "python", "", "ai"]
res = [name for name in names if name]
print(res)

numbers = [1, 2, 3, 4, 5]
res = ["Even" if number % 2 == 0 else "Odd" for number in numbers]
print(res)
