""" Project Euler Problem 39:
	If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

	{20,48,52}, {24,45,51}, {30,40,50}

	For which value of p <= 1000, is the number of solutions maximised?
"""
"""
	Thoughts:
	* Pythagorean theorem!!
	* a^2 + b^2 = c^2
	* c always is the biggest

	* I bet there are some side lengths that can be ignored, but I don't know the rules around it...
"""

import math
from util import *

most_number_of_solutions = 0

for p in range(1, 1000):
	number_of_solutions = 0
	for c in range(p/3,p):
		for b in range(1, c):
			a = p - b - c
			if a > 0 and a*a + b*b == c*c:
				number_of_solutions += 1
	if most_number_of_solutions < number_of_solutions:
		most_number_of_solutions = number_of_solutions
		print str(p) + ' yielded a new most number_of_solutions: ' + str(most_number_of_solutions)
print 'Done'