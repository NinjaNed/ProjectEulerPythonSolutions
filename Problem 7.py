#!/usr/bin/env python
__author__ = 'Ned Udomkesmalee'

#What is the 10 001st prime number?


def problem7():
    print("Find the nth prime number")
    while True:
        n = raw_input("What is n? ")
        try:
            n = int(n)
            if n < 1:
                print "*** Upper bound must be a positive non-zero integer ***"

            else:
                prime_list = [2]
                counter = 1
                next_num = 3
                while counter < n:
                    next_num_is_prime = True
                    for prime in prime_list:
                        if next_num % prime == 0:
                            next_num_is_prime = False
                            break
                    if next_num_is_prime:
                        prime_list.append(next_num)
                        counter += 1
                    next_num += 2
                print "The %ith prime is %i" % (n, prime_list[n-1])
                break

        except ValueError:
            print "*** %s is not a valid integer ***" % n

problem7()