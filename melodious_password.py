"Melodious password"

import itertools

alphabet = "bcdfghjklmnpqrstvwxyz"
vowels   = "aeiou"

#alphabet1 = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
#            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']

#vowels1 = ['a','e','i','o','u']

consonants = ['b','c','d','f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
              'r', 's', 't', 'v', 'w', 'x', 'z']
n = 2
if n == 1:
    for code in alphabet:
        print(code)
else:
    code = itertools.product(vowels, alphabet)
    for codes in code:
        print(codes)
