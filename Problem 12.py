#!/usr/bin/env python 
__author__ = 'Ned Udomkesmalee'

#What is the value of the first triangle number to have over five hundred divisors?


def num_factors(n):
    return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


def problem12():
    print("Find the first triangle number to have n divisors")

    while True:
        n = raw_input("What is n? ")
        try:
            n = int(n)
            if n > 0:
                next_num = 2
                t_num = 1
                while num_factors(t_num) < n:
                    t_num += next_num
                    next_num += 1
                print "Answer = %i" % t_num
                break
            else:
                print "*** n must be positive. ***"
        except ValueError:
            print "*** %s is not a valid integer. ***" % n

problem12()
