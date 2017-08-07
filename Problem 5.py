#!/usr/bin/env python 
__author__ = 'Ned Udomkesmalee'

# Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import operator
import math


def primes_up_to(n):
    #Sieve of Eratosthenes Implementation to create Prime Numbers up to n
    if n <= 2:
        return []
    sieve = [True] * (n+1)
    for x in range(3, int(n ** 0.5) + 1, 2):
        for y in range(3, (n // x) + 1, 2):
            sieve[(x * y)] = False

    return [2]+[i for i in range(3, n, 2) if sieve[i]]


def problem5():
    print("Find the smallest number that is evenly divisible by all the numbers from 1 to n")

    while True:
        n = raw_input("What is n? ")
        try:
            n = int(n)
            if n > 0:
                # you only need to deal with the lcm of the top half of the divisibility set
                # i.e if n = 16, no need to check divisibility with 4 or 8 since divisibility with 16 will satisfy both.
                list_divisors = range(n // 2 + 1, n+1)
                product = list_divisors[-1] * reduce(operator.mul, primes_up_to(n), 1)
                while product < math.factorial(n):
                    flag = True
                    # no need to check divisible by largest divisor cause we increment by that amount
                    for i in list_divisors[:-1][::-1]:
                        if product % i != 0:
                            flag = False
                            break
                    if flag:
                        print "Answer is %i" % product
                        exit()
                    else:
                        product += list_divisors[-1]
            else:
                print "*** Upper bound must be positive non-zero number. ***"
        except ValueError:
            print "*** %s is not a valid integer. ***" % n


problem5()