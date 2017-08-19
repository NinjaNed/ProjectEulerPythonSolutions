#!/usr/bin/env python
__author__ = 'Ned Udomkesmalee'

#Find the sum of all the multiples of 3 or 5 below 1000.


def problem1():
    print("Find the sum of all the multiples of 3 or 5 up to n.")
    while True:
        n = raw_input("What is n? ")
        try:
            n = int(n)
            if n > 0:
                valid_nums = [i for i in range(0, n) if (i % 3 == 0 or i % 5 == 0)]
                print("Answer = %i" % sum(valid_nums))
                break
            else:
                print "*** Upper bound must be positive ***"
        except ValueError:
            print "*** %s is not a valid integer ***" % n

problem1()
