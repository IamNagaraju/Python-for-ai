There are mainly 2 loops in Python:

for loop ⭐⭐⭐⭐⭐ (Most used)
while loop ⭐⭐⭐⭐

Along with:

break
continue
pass
range()
enumerate() ⭐⭐⭐⭐⭐

These are what you'll use 99% of the time.

1. for Loop
JavaScript
const fruits = ["Apple", "Banana", "Orange"];

for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}
Python
fruits = ["Apple", "Banana", "Orange"]

for fruit in fruits:
    print(fruit)

Output

Apple
Banana
Orange

Notice:

No i++
No length
No semicolons
Much cleaner
2. Using range()

JavaScript:

for(let i=0;i<5;i++){
    console.log(i);
}

Python:

for i in range(5):
    print(i)

Output

0
1
2
3
4

range(5) means:

0
1
2
3
4
range(start, end)
for i in range(2, 6):
    print(i)

Output

2
3
4
5
range(start, end, step)

Exactly like slicing.

for i in range(0, 10, 2):
    print(i)

Output

0
2
4
6
8

Reverse

for i in range(10, 0, -2):
    print(i)

Output

10
8
6
4
2

Same idea as:

text[::-2]

The third argument is the step.

3. while Loop

Exactly like JavaScript.

JavaScript
let i = 0;

while(i < 5){
    console.log(i);
    i++;
}
Python
i = 0

while i < 5:
    print(i)
    i += 1

Output

0
1
2
3
4
4. break

Stops the loop.

for i in range(10):

    if i == 5:
        break

    print(i)

Output

0
1
2
3
4

Exactly like JavaScript's break.

5. continue

Skip current iteration.

for i in range(6):

    if i == 3:
        continue

    print(i)

Output

0
1
2
4
5

Exactly the same as JavaScript.

6. pass

This is something JavaScript doesn't really have.

Suppose you're writing code later.

for i in range(5):
    pass

It does nothing.

Useful while developing.

Example

def login():
    pass

No error occurs.

Without pass

def login():

You'll get

IndentationError
7. enumerate() ⭐⭐⭐⭐⭐

This is one of Python's best features.

Suppose:

fruits = ["Apple","Banana","Orange"]

JavaScript

fruits.forEach((item,index)=>{
    console.log(index,item);
});

Python

for index, fruit in enumerate(fruits):
    print(index, fruit)

Output

0 Apple
1 Banana
2 Orange

Much cleaner than maintaining your own counter.

8. Loop through string
text = "Python"

for ch in text:
    print(ch)

Output

P
y
t
h
o
n

JavaScript

for(let ch of text){
    console.log(ch);
}

Very similar.

9. Loop through dictionary

Suppose

person = {
    "name":"Naga",
    "age":30
}

Keys

for key in person:
    print(key)

Output

name
age

Both

for key, value in person.items():
    print(key, value)

Output

name Naga
age 30

Very important in Python.

10. Nested Loop
for i in range(3):
    for j in range(2):
        print(i, j)

Output

0 0
0 1
1 0
1 1
2 0
2 1

Exactly like JavaScript.