#!/usr/bin/env python 
__author__ = 'Ned Udomkesmalee'

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def problem9():
    print("Find the product of the only pythagorean triplet in which a + b + c = 1000")

    # since a < b < c then (a + b + c = s) => (a < s/3) & (a < b < s/2)
    for a in range(1000/3):
        for b in range(a, 500):
            c = 1000 - a - b
            if a * a + b * b == c * c:
                if a + b + c == 1000:
                    print " a = %i \n b = %i \n c = %i \n Answer = %i" % (a, b, c, a * b * c)
                    break

problem9()