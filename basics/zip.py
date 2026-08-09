names = ["Naga", "Raju"]
ages = [30, 25]

result = zip(names, ages)

print(list(result))
# output:
# [
#     ("Naga", 30),
#     ("Raju", 25)
# ]
names = ["Naga", "Raju", "Ajay"]
ages = [30, 25]

print(list(zip(names, ages)))
# [
#     ("Naga",30),
#     ("Raju",25)
# ]

names = ["Naga","Raju"]
ages = [30,25]
cities = ["HYD","BLR"]

print(list(zip(names,ages,cities)))

# [
#     ("Naga",30,"HYD"),
#     ("Raju",25,"BLR")
# ]

names = ["Naga","Raju"]
ages = [30,25]

for name, age in zip(names, ages):
    print(name, age)

Naga 30
Raju 25
# Unzipping
data = [
    ("Naga",30),
    ("Raju",25)
]

names, ages = zip(*data)

print(names)
print(ages)

# ('Naga','Raju')

# (30,25)