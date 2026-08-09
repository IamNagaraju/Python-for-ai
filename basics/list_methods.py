# print first element and last element
languages = ["Python","JavaScript", "Java", "Go"]
print(languages[0])
print(languages[-1])

#Replace "Java" with "TypeScript"
for index, lang in enumerate(languages):
    if lang == "Java":
        languages[index] = "TypeScript"

print(languages)

#append()
languages = ["Python", "JavaScript", "Go"]
languages.append("Rust") # ["Python", "JavaScript", "Go", "Rust"]

#extend()
languages = ["Python", "Java"]

languages.extend(["Go", "Rust"])

print(languages) 

numbers = [1, 2]

numbers.extend("345") #[1, 2, "3", "4", "5"]

print(numbers)

# What is "345"? It's not a list. It's a string.But a string is an iterable. That means Python can loop through it and append it for ch in "345"
arr = []

arr.append("Python")

# print(arr)
# arr.extend([1, 2, 3])      # List ✅

# arr.extend((1, 2, 3))      # Tuple ✅

# arr.extend("ABC")          # String ✅

# arr.extend({1, 2, 3})       # Set ✅ (order not guaranteed)

# arr.extend(range(5))        # Range ✅
print(arr)

arr = [10]

arr.append("ABC")

arr.extend("XYZ")

print(arr)

# insert It inserts before the given index
numbers = [10, 20, 30]
numbers.insert(-1, 15) # [10, 20, 15, 30]

# remove()
languages = ["Python", "Java", "Go"]

languages.remove("Java")

print(languages) #["Python", "Go"]
numbers = [10, 20, 30]

numbers.remove(100)

numbers = [10, 20, 30]

result = numbers.remove(20)

print(result) #None

arr.clear() // empties the array
copy() // shallow copy

arr1 = [10, 20, 30]

arr2 = arr1

arr1 = [100]

print(arr1) #[100][10,20,30]
print(arr2) 
# does NOT modify the old list. It creates a brand new list.

numbers = [8, 3, 6, 1, 5]

numbers.sort(reverse=True)

print(numbers) # sort in reverse order
numbers.sort() # ascending order

numbers = [5, 2, 9]

new_list = sorted(numbers)

print(numbers)
print(new_list) # sorted will not mutate original array

| Feature               | `sort()`  | `sorted()`      |
| --------------------- | --------- | --------------- |
| Changes original list | ✅ Yes     | ❌ No            |
| Returns               | `None`    | New sorted list |
| Memory                | Same list | New list        |
| Works only on lists   | ✅ Yes     | ❌ No            |


# index
numbers = [10, 20, 30]

print(numbers.index(100)) // python throws errors
numbers = [10, 20, 30, 20, 40]

print(numbers.index(20, 2)) # 3
# for avodign erros
if 100 in numbers:
    print(numbers.index(100))

numbers = [1, 2, 3, 2, 2, 4, 5]

print(numbers.count(2)) # 3

numbers = [1, True, 2, True, 1]

print(numbers.count(True)) # 4

| Element | `element == True` |
| ------- | ----------------- |
| `1`     | ✅ True            |
| `True`  | ✅ True            |
| `2`     | ❌ False           |
| `True`  | ✅ True            |
| `1`     | ✅ True            |
print(1 == True)      # True
print(0 == False)     # True
print(2 == True)      # False

# Falsy Values
# False
# None
# 0
# 0.0
# 0j          # complex zero
# ""          # Empty string
# []          # Empty list
# ()          # Empty tuple
# {}          # Empty dictionary
# set()       # Empty set
# range(0)    # Empty range

List Methods and Their Return Types
| Method                   | Modifies Original List | Returns             | Example                       |
| ------------------------ | ---------------------- | ------------------- | ----------------------------- |
| `append(x)`              | ✅ Yes                  | `None`              | Add one element at the end    |
| `extend(iterable)`       | ✅ Yes                  | `None`              | Add multiple elements         |
| `insert(index, x)`       | ✅ Yes                  | `None`              | Insert at specific index      |
| `remove(value)`          | ✅ Yes                  | `None`              | Remove first matching value   |
| `clear()`                | ✅ Yes                  | `None`              | Remove all elements           |
| `sort()`                 | ✅ Yes                  | `None`              | Sort the list                 |
| `reverse()`              | ✅ Yes                  | `None`              | Reverse the list              |
| `pop()`                  | ✅ Yes                  | **Removed element** | Remove by index and return it |
| `copy()`                 | ❌ No                   | **New list**        | Shallow copy                  |
| `count(x)`               | ❌ No                   | **Integer**         | Count occurrences             |
| `index(x)`               | ❌ No                   | **Integer**         | Find first index              |
| `len(list)` *(function)* | ❌ No                   | **Integer**         | Number of elements            |




