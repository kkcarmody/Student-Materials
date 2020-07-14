# python_intro.py
"""Python Essentials: Introduction to Python.
Kody Carmody
Python Essentials
7/11/2020
"""

import math

def sphere_volume(r = 0):
    ''' Returns the volume of a sphere with radius r
    '''
    return 4/3 * math.pi * r**3
    
def isolate(a, b, c, d, e):
    ''' Returns the first two terms isolated from the last three.
    '''
    print(a, '     ', b, '     ', c, d, e)

def first_half(string):
    ''' returns the first half of a string
    '''
    half = int((len(string) - (len(string) % 2))/2)
    return string[:half]

def backward(string):
    ''' reverses a string
    '''
    return string[::-1]

def list_ops(list):
    list.append('eagle')
    list[1] = 'fox'
    list.remove(list[1])
    list.sort(reverse = False)
    list[list.index('eagle')] = 'hawk'
    list[-1] = list[-1] + ' hunter'
    return list

def pig_latin(word : str) -> str:
    ''' Translates a word into pig latin
    '''
    if word[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        return word + 'hay'
    
    else:
        return word[1:] + word[0] + 'ay'

def check_palindrome(x : int) -> bool:
    # identical = sum([x == y for x, y in zip(str(x), str(x)[::-1])])
    # return identical == len(str(x))
    return str(x) == str(x)[::-1]

def palindrome() -> int:
    ''' Finds and returns the largest palindromic number made from the product of two 3-digit numbers.
    '''
    palindromes = {}
    for i in range(100, 1000):
        for j in range(100, 1000):
            if check_palindrome(i * j):
                palindromes[(i, j)] = i * j

    return max(palindromes, key = palindromes.get)

def alt_harmonic(n):
    ''' Returns the sum of the first n terms of the alternating harmonic series
    '''
    return sum([(-1)**(n + 1)/n for n in range(1, n + 1)])

if __name__ == "__main__":
    print("Hello, world!")
    print(sphere_volume())
    isolate(1, 2, 3, 4, 5)
    print(first_half('cut this string in half'))
    print(backward('flip this string'))
    print(list_ops(['bear', 'ant', 'cat', 'dog']))
    print(pig_latin('bugs'))
    print(pig_latin('oof'))
    print(palindrome())