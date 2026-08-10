#range(start, stop, step)
# for i in range(10,0,-1):
    # print(i)

# even numbers
# for i in range(1,21):
#     if i%2 == 0:
        # print("Even numbers are", i)

numbers = [10, 25, 8, 13, 40, 7, 18]
#Print only the numbers greater than 15.
for num in numbers:
    if num > 15:
        print(num)

numbers = [10, 20, 30, 40, 50]
print(sum(numbers))
# Calculate the sum of all numbers
sum = 0
for num in numbers:
    sum += num

print(sum)

# Find the largest number
max = numbers[0]
for num in numbers:
    if(max < num):
        max = num

print(max)

# numbers = [2, 4, 6, 8, 9, 10, 12]
# # As soon as you encounter 9, stop the loop immediately
# for num in numbers:
#     print(num)

#     if num == 9:
#         break

numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num == 4:
        continue
    print(num)
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    res = ""
    for j in range(1, i+1):
        res += "*" 
    
    print(res, '======')

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     res = ""
#     for j in range(1, i + 1):
#         res += str(j)
    
#     print(res)

# res = ""
# for i in range(1,6):
#     res += str(i)
#     print(res)

# 12345
# 1234
# 123
# 12
# 1

for i in range(6, 1, -1):
    res = ""
    for j in range(1, i, +1):
        res += str(j)

    print(res)

# multiplication tables

for i in range(1, 6):
    res = ""
    total = 0
    for j in range(1, 11):
        total = i * j
        res = f"{i} * {j} = {total}"
        print(res)

    print("-----")
