#!/usr/bin/env python 
__author__ = 'Ned Udomkesmalee'

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def problem6():
    print("Find the difference between the sum of squares and square of sum up to n")
    while True:
        n = raw_input("What is n? ")
        try:
            n = int(n)
            if n > 1:
                square_of_sum = (((n + 1) * n) / 2) ** 2
                sum_of_square = sum(map(lambda x: x ** 2, range(0, n+1)))
                print "Answer is %i" % (square_of_sum - sum_of_square)
                break
            elif n == 0 or n == 1:
                print "Answer is 0"
            else:
                print "*** n must be positive ***"
        except ValueError:
            print "*** %s is not a valid integer ***" % n

problem6()