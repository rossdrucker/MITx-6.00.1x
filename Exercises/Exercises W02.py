# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:45:13 2019

@author: rdrucker
"""

print('Please think of a number between 0 and 100!')
low = 0
high = 100
guess = (low + high) // 2
secret_number_found = False
while secret_number_found == False:
    print('Is your secret number ' + str(guess) + '?')
    user_response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_response == 'l':
        low = guess
        high = high
        guess = (high + low) // 2
    elif user_response == 'h':
        low = low
        high = guess
        guess = (high + low) // 2
    elif user_response == 'c':
        print('Game over. Your secret number is ' + str(guess))
        secret_number_found = True
    else:
        print('Sorry, I did not understand your input.')

def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    return x ** 2

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic
    '''
    # Your code here
    return (a * (x ** 2)) + (b * x) + c

def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(square(x))

def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return not x % 2 == 0

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    output = 1
    while exp > 0:
        output *= base
        exp -= 1

    return output

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
        n = a
    else:
        n = b
    while n >= 1:
        if (a % n == 0) and (b % n == 0):
            return n
        else:
            n -= 1

def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) < 1:
        return False
    elif len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False
    else:
        low = 0
        high = len(aStr)
        mid = (low + high) // 2
        mid_char = aStr[mid]
        if char == mid_char:
            return True
        elif char < mid_char:
            return isIn(char, aStr[:mid])
        elif char > mid_char:
            return isIn(char, aStr[mid:])