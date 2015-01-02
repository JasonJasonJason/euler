""" Project Euler Problem 37:
	The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

	Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

	NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
"""
	Thoughts:
	* I already have my is_prime function in util. Yay!
	* We know there's only eleven of these, so no worry about end case. Once I've found all 11, stop.
"""

import math
from util import *


def right_truncateable(num):
	right = str(num)

	while len(right) > 0:
		if is_prime(int(right)) == False:
			return False
		right = right[:-1]

	return True

def left_truncateable(num):
	left = str(num)
	while len(left) > 0:
		if is_prime(int(left)) == False:
			return False
		left = left[1:]

	return True

total = 0
count = 0
num = 9
while count < 11:
	num += 1
	if left_truncateable(num) and right_truncateable(num):
		print 'truncatable prime found: ' + str(num)
		total += num
		count += 1

print 'Total of the eleven truncatable primes: ' + str(total)