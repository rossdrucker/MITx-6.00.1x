# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:26:16 2019

@author: rdrucker
"""

# Problem 1
vowels = ['a', 'e', 'i', 'o', 'u']

n_vowels = 0
for letter in range(len(s)):
    if s[letter] in vowels:
        n_vowels += 1

print('Number of vowels: ' + str(n_vowels))

# Problem 2
bob_count = 0
for l in range(len(s) - 2):
    if s[l:l + 3] == 'bob':
        bob_count += 1

print('Number of times bob occurs is: ' + str(bob_count))

# Problem 3
c = ''
r = ''

for char in s:
    if (c == ''):
        c = char
    elif (c[-1] <= char):
        c += char
    elif (c[-1] > char):
        if (len(r) < len(c)):
            r = c
            c = char
        else:
            c = char
if (len(c) > len(r)):
    r = c
print('Longest substring in alphabetical order is: ' + r)