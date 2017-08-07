#!/usr/bin/env python 
__author__ = 'Ned Udomkesmalee'

#What is the largest prime factor of the number 600851475143?


def primes_up_to(n):
    #Sieve of Eratosthenes Implementation to create Prime Numbers up to n
    if n <= 2:
        return []
    sieve = [True] * (n+1)
    for x in range(3, int(n ** 0.5) + 1, 2):
        for y in range(3, (n // x) + 1, 2):
            sieve[(x * y)] = False

    return [2]+[i for i in range(3, n, 2) if sieve[i]]


def problem3():
    print("Find the largest prime factor of a given number")

    while True:
        num = raw_input("What Number? ")
        try:
            num = int(num)
            if num > 0:
                primes = primes_up_to(int(num ** .5) + 1)
                primes.reverse()
                found_flag = False
                for prime in primes:
                    if num % prime == 0:
                        print("Answer = %i" % prime)
                        found_flag = True
                        break
                if not found_flag:
                    "Answer = 1"
                break
            else:
                print "*** Upper bound must be positive. ***"
        except ValueError:
            print "*** %s is not a valid integer. ***" % num

problem3()

