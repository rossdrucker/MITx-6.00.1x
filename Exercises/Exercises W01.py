# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 09:23:40 2019

@author: rdrucker
"""

# What is the difference between an algorithm and a program?
"""
An algorithm is a conceptual idea, a program is a concrete instantiation of an
algorithm
"""

# True or False? A computational mode of thinking means that everything can be
# viewed as a math problem involving numbers and formulas.
"""
True
"""

# The two things every computer can do are:
"""
Perform calculations
Remember the results
"""

# Declarative knowledge refers to statements of fact
"""
True
"""

# Imperative knowledge refers to 'how to' methods
"""
True
"""

# A recipe for deducing the square root involves guessing a starting value for
# y. Without another recipe to be told how to pick a starting number, the
# computer cannot generate one on its own.
"""
True
"""

# A stored program computer is designed to compute precisely one computation,
# such as a square root, or the trajectory of a missile.
"""
False
"""

# A fixed program computer is designed to run any computation, by interpreting
# a sequence of program instructions that are read into it.
"""
False
"""

# A program counter
"""
points the computer to the next instruction to execute in the program.
"""

# What does it mean when we say that "the computer walks through the sequence
# executing some computation"?
"""
The computer executes the instructions mostly in a linear sequence, except
sometimes it jumps to a different place in the sequence
"""

# In order to compute everything that is computable, every computer must be
# able to handle the sixteen most primitive operations.
"""
False
"""

# Definitions...
# Determines whether a string is legal:
"""
Syntax
"""

# Determines whether a string has meaning:
"""
Static semantics
"""

# Assigns a meaning to a legal sentence
"""
Semantics
"""

# 3.14
type(3.14)

type(-34)

type(True)

type(None)

type(3.0)

6 + 12 -3

2 * 3.0

- - 4

10/3

10.0/3.0

(2 + 3) * 4

2 + 3 * 4

2**3 + 1

2.1 ** 2.0

2.2 * 3.0


a = 3
a + 2.0
type(a + 2.0)

a = a + 1.0
a
type(a)

a = 3
try:
    b
except:
    print('This is NoneType since b is never defined')

3 > 4

4.0 > 3.999

4 > 4

4 > + 4

2 + 2 == 4

True or False

False or False

not False

3.0 - 1.0 != 5.0 - 3.0

3 > 4 or (2 < 3 and 9 > 10)

4 > 5 or 3 < 4 and 9 > 8

not(4 > 3 and 100 > 6)

a = 3
a == 5.0
a
type(a)

b = 10
c = b > 9
c
type(c)

3 + 5.0
type(3 + 5.0)

5/2
type(5/2)

5/2 == 5/2.0
type(5/2 == 5/2.0)

5/2.0
type(5/2.0)

round(2.6)
type(round(2.6))

2.0 + 5.0
type(2.0 + 5.0)

5 * 2 == 5.0 * 2.0
type(5 * 2 == 5.0 * 2.0)


"a" + "bc"

3 * "bc"

try:
    "3" * "bc"
except:
    print('"3" * "bc" produces an error')

"abcd"[2]

"abcd"[0:2]


"abcd"[:2]

"abcd"[2:]

str1 = 'hello'
str2 = ','
str3 = 'world'

str1
type(str1)

str1[0]
type(str1[0])

str1[1]
type(str1[1])

str1[-1]
type(str[-1])

len(str1)
type(len(str1))

if 6 > 7:
   print("Yep") # will not print; answer is blank

if 6 > 7:
   print("Yep")
else:
   print("Nope")

var = 'Panda'
if var == "panda":
   print("Cute!")
elif var == "Panda":
   print("Regal!")
else:
   print("Ugly...")

temp = 120
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable")
else:
   print("Cold")

temp = 50
if temp > 85:
   print("Hot")
elif temp > 100:
   print("REALLY HOT!")
elif temp > 60:
   print("Comfortable")
else:
   print("Cold")

print('hello world')

if happy > 2:
    print('hello world')

if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
elif varA < varB:
    print('smaller')

num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num)

# This will create an infinite loop since number of loops never grows to 10
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

num = 10
while num > 3:
    num -= 1
    print(num)

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

# This will create an infinite loop since num is never decreased
num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num))

"""
Convert the following into code that uses a while loop.

print 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""
n = 1
while n <= 10:
    if n % 2 == 0:
        print(str(n))
    n += 1
print('Goodbye!')


"""
Convert the following into code that uses a while loop.

prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
"""
print('Hello!')
n = 10

while n >= 2:
    if n % 2 == 0:
        print(str(n))
    n -= 1

"""
Write a while loop that sums the values 1 through end, inclusive.
end is a variable that we define for you. So, for example, if we define end to
be 6, your code should print out the result:

21

which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include input statements or define variables
we will provide for you. Our automating testing will provide values so write
your code in the following box assuming these variables are already defined.
"""
s = 0
n = 1
while n <= end:
    s += n
    n += 1

print(str(s))

"""
Convert the following code into code that uses a for loop.

prints 2
prints 4
prints 6
prints 8
prints 10
prints Goodbye!
"""
for i in range(1, 11):
    if i % 2 == 0:
        print(str(i))

print('Goodbye!')

"""
Convert the following code into code that uses a for loop.

prints Hello!
prints 10
prints 8
prints 6
prints 4
prints 2
"""
print('Hello!')
for i in reversed(range(1, 11)):
    if i % 2 == 0:
        print(str(i))


"""
Write a for loop that sums the values 1 through end, inclusive.
end is a variable that we define for you. So, for example, if we define end to
be 6, your code should print out the result:

21

which is 1 + 2 + 3 + 4 + 5 + 6.

For problems such as these, do not include input statements or define variables
we will provide for you. Our automating testing will provide values so write
your code in the following box assuming these variables are already defined.
"""
s = 0
for i in range(1, end + 1):
    s += i

print(str(s))

num = 10
for num in range(5):
    print(num)
print(num)

divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!')

for letter in 'hola':
    print(letter)

count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)


myStr = '6.00x'
for char in myStr:
    print(char)

print('done')


greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))

# Sample
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

# This creates an infinite loop since the while loop never breaks
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))

# This never changes the value of count
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break

# Same as sample
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))

# Same as sample
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))

# Same as sample
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))
