#!/usr/bin/env python
__author__ = 'Ned Udomkesmalee'

#What is the 10 001st prime number?

#Important facts: Primes > 3 will be of the form 6k +/- 1 and you only need to check for prime divisibility up to sqrt i


def problem7():
    print("Find the nth prime number")
    while True:
        n = raw_input("What is n? ")
        try:
            n = int(n)
            if n < 1:
                print "*** Upper bound must be a positive non-zero integer ***"

            else:
                prime_list = [2, 3]
                counter = 2
                i = 6
                while counter < n:
                    for next_num in [i-1, i+1]:
                        next_num_is_prime = True
                        upper_bound = next_num ** .5
                        for prime in prime_list:
                            if next_num % prime == 0:
                                next_num_is_prime = False
                                break
                            elif prime > upper_bound:
                                break
                        if next_num_is_prime:
                            prime_list.append(next_num)
                            counter += 1
                    i += 6
                print "The %ith prime is %i" % (n, prime_list[n-1])
                break

        except ValueError:
            print "*** %s is not a valid integer ***" % n

problem7()