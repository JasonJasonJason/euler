""" Project Euler Problem 38:
	Take the number 192 and multiply it by each of 1, 2, and 3:

	192 x 1 = 192
	192 x 2 = 384
	192 x 3 = 576
	By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

	The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

	What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2,...,n) where n > 1?
"""
"""
	Thoughts:
	* The number has to be less than 99,999 because total we need 9 digits. if we take this 5 digit number and it multiplied by 2 we have 10 digits.
"""

import math
from util import *

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_pandigital(n):
	num = str(n)
	for digit in digits:
		if not digit in num:
			return False

	return len(num) == 9

biggest_pandigital = 0
for num in range(1,99999):
	total = ''
	multiplyer = 1
	while len(total) < 9:
		total += str(num*multiplyer)
		multiplyer += 1
		
	if len(total) == 9 and is_pandigital(int(total)):
		biggest_pandigital = max(biggest_pandigital, int(total))
		print str(num) + ' yields the pandigital: ' + str(total)

print 'The largest 1 to 9 pandigital 9-digit number is ' + str(biggest_pandigital)