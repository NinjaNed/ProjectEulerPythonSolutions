#!/usr/bin/env python 
__author__ = 'Ned Udomkesmalee'

#Find the sum of all the primes below two million.


def primes_up_to(n):
    #Sieve of Eratosthenes Implementation to create Prime Numbers up to n
    if n <= 2:
        return []
    sieve = [True] * (n+1)
    for x in range(3, int(n ** 0.5) + 1, 2):
        for y in range(3, (n // x) + 1, 2):
            sieve[(x * y)] = False

    return [2]+[i for i in range(3, n, 2) if sieve[i]]


def problem10():
    print("Find the largest prime factor up to n")

    while True:
        n = raw_input("What is n? ")
        try:
            n = int(n)
            if n > 0:
                primes = primes_up_to(n)
                print "Answer = %i" % sum(primes)
                break
            else:
                print "*** n must be positive. ***"
        except ValueError:
            print "*** %s is not a valid integer. ***" % n

problem10()
