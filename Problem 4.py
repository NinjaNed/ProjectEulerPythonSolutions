#!/usr/bin/env python 
__author__ = 'Ned Udomkesmalee'

#Find the largest palindrome made from the product of two 3-digit numbers.


def problem4():
    print("Find the largest palindrome made from the product of two 3-digit numbers")
    product = 999 * 999
    while True:
        if str(product) == str(product)[::-1]:  # if product is palindrome
            for i in range(100, 999)[::-1]:  # counting backwards from 1000 for efficiency
                if product % i == 0:
                    factor = product / i # should be an integer
                    if 99 < factor < 1000:
                        print "Answer is %i" % product
                        exit()
        product -= 1

problem4()