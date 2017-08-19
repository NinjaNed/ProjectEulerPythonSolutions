#!/usr/bin/env python 
__author__ = 'Ned Udomkesmalee'

# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def problem2():
    print("Find the sum of the even-valued Fibonacci terms up to n.")
    while True:
        n = raw_input("What is n? ")
        try:
            n = int(n)
            if n > 0:
                fib_nums = [0, 1]
                n = 1
                while fib_nums[n] < n:
                    fib_nums += [fib_nums[n] + fib_nums[n-1]]
                    n += 1
                print("Answer = %i" % sum([i for i in fib_nums[:-1] if i % 2 == 0]))
                break
            else:
                print "*** n must be positive. ***"
        except ValueError:
            print "*** %s is not a valid integer. ***" % n

problem2()
