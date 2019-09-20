# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 11:13:19 2019

@author: rdrucker
"""

def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    return aTup[::2]

def findAbs(a):
    if a < 0:
        return a * -1
    else:
        return a


def plusOne(a):
    return a + 1

def square(a):
    return a ** 2

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    s = 0
    for k in aDict:
        s += len(aDict[k])

    return s

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    mkey = ''
    m = 0
    for k in aDict:
        if len(aDict[k]) > m:
            m = len(aDict[k])
            mkey = k

    return mkey