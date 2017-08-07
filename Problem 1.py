#!/usr/bin/env python
__author__ = 'Ned Udomkesmalee'

#Find the sum of all the multiples of 3 or 5 below 1000.


def problem1():
    print("Find the sum of all the multiples of 3 or 5 below a given value.")
    while True:
        upper_bound = raw_input("What upper bound? ")
        try:
            upper_bound = int(upper_bound)
            if upper_bound > 0:
                valid_nums = [i for i in range(0, upper_bound) if (i % 3 == 0 or i % 5 == 0)]
                print("Answer = %i" % sum(valid_nums))
                break
            else:
                print "*** Upper bound must be positive ***"
        except ValueError:
            print "*** %s is not a valid integer ***" % upper_bound

problem1()
