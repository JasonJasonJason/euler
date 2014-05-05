""" Project Euler Problem 34:

	145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

	Find the sum of all numbers which are equal to the sum of the factorial of their digits.

	Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
"""
	Thoughts: 
	* We'll be summing a lot of factorials, but only 1!-9!. Thus, create a static mapping of those results, instead of calculating them a billion times.
	* When do I stop?? Spooky. 
		Got it! 9*8*7*6*5*4*3*2*1 = 362880
		So, if we have the number 9999999, we have a sum of 2540160. This seems like a good stopping point, cause it cannot
		possibly have any more digits than 7. Since the sum is 2540160 (7 digits), nothing can go past that point.
"""

import math

digits = {}
for digit in range(0,10):
	digits[str(digit)] = math.factorial(digit)

match_sum = 0
for i in range(3, 2540160):
	if i == sum([digits[d] for d in str(i)]):
		print 'Found one: ' + str(i)
		match_sum += i
print 'Total: ' + str(match_sum)
