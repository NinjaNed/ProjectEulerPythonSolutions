#!/usr/bin/env python 
__author__ = 'Ned Udomkesmalee'

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

print("Find the sum of the even-valued Fibonacci terms below a given value.")

while True:
    upper_bound = raw_input("What upper bound? ")
    try:
        upper_bound = int(upper_bound)
        if upper_bound > 0:
            fib_nums = [0, 1]
            n = 1
            while fib_nums[n] < upper_bound:
                fib_nums += [fib_nums[n] + fib_nums[n-1]]
                n += 1
            print("Answer = %i" % sum([i for i in fib_nums[:-1] if i % 2 == 0]))
            break
        else:
            print "*** Upper bound must be positive. ***"
    except ValueError:
        print "*** %s is not a valid integer. ***" % upper_bound

