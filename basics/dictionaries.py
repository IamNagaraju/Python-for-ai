user = {
    "name": "Naga", # for keys also "" required
    "age": 30,
    "city": "Hyderabad"
} 
# print(user["place"]) # error if access key is not present

#Delete a key
del user["city"]

employee = {
    "name": "Naga"
}
# print(employee["age"]) # error
print(employee.get("age")) # None

print(employee.get("age", 0)) # default we can provide if key is not exists
print(employee.get("age", "Not Available"))

# Which is better?
# when you're 100% sure the key exists. use employee["age"] else use employee.get("age")

#keys()
employee = {
    "name": "Naga",
    "age": 30,
    "city": "Hyderabad"
}

print(employee.keys())

#values()
print(employee.values()) # dict_values(['Naga', 30, 'Hyderabad'])

#items() 

print(employee.items(), '======') # dict_items([ ('name', 'Naga'), ('age', 30), ('city', 'Hyderabad') ])

for key, value in employee.items():
    print(key, value)   

# name Naga
# age 30
# city Hyderabad

# JavaScript Equivalent
# Object.entries(employee).forEach(([key, value]) => {
#     console.log(key, value);
# });

#pop()
employee = {
    "name": "Naga",
    "age": 30
}

age = employee.pop("age")

print(age) # 30 it return the removed value (if you want value by removing we can use it)
print(employee) # {'name': 'Naga'}
print(employee.pop("age", "Not Found")) # we can pass default value

numbers = [1,2,3,4,5]

result = {}

for num in numbers:
    result[num] = num * 10

res = {num: num * 10 for num in numbers}

words = ["apple","banana","kiwi"]

output = {word: len(word) for word in words}

numbers = [1,2,3,4,5]
output = {num: num * num  for num in numbers if num %2 == 0}

#clear

# shallow copy
import copy

employee1 = {
    "name": "Naga",
    "skills": ["Python", "React"]
}

employee2 = copy.deepcopy(employee1)

employee2["skills"].append("AI")

print(employee1)
print(employee2)

employee1 = {
    "name": "Naga",
    "skills": ["Python", "React"]
}

employee2 = employee1.copy()

employee2["skills"].append("AI")

print(employee1)
print(employee2)