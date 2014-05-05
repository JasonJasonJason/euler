""" Project Euler Problem 35:
	The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

	There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

	How many circular primes are there below one million?
"""
"""
	Thoughts:
	* I have an is_prime function, created a couple problems ago. I'll extensilize that and use it here.
	* Rotating digits?
"""

import math
from util import *

count = 0
for i in range(2,1000000):
	num = i
	digits = int(math.log10(num))
	if is_prime(num):
		all_prime = True
		for j in range(0,digits):
			mod = num % 10
			num /= 10
			num += mod*10**digits
			if not is_prime(num):
				all_prime = False
		if all_prime:
			print 'all prime! ' + str(i)
			count += 1

print 'Number of circular primes below one million: ' + str(count)
