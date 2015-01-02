""" Project Euler Problem 36:
	The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

	Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

	(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
"""
	Thoughts:
	* I'll need a isPalindrome function that could take in the number as a string (put in util)
	* I'll need a way to convert base-10 digit number to binary (also put this in util)
"""

import math
from util import *

total = 0
for num in range(1,1000000):
	if is_palindrome(num) and is_palindrome(dec_to_bin(num)):
		total += num
		print "palindrome: " + str(num)

print "total: " + str(total)
