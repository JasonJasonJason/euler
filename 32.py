""" Project Euler Problem 32:

	We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

	The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

	Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

	HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
"""
	Idea: Let's see what the maximum is...
		1 x 1234 = 1234 => 9 digits
		So, I think if I run through all combinations of a x b where a in [1, 1234] and b in [1, 1234] I'll hit all possible solutions.

	Wrong! Did not get the '1234' maximum guess right. Ex: 4 x 1963 = 7852

	Finally figured it out. Problem was that I was using multiple products...Namely this:
		198 x 27 = 5346
		297 x 18 = 5346
	and
		138 x 42 = 5796
		483 x 12 = 5796
	I didn't understand the directions.
"""

def isPandigital(a,b):
	r = str(a) + str(b) + str(a*b)
	if len(r) != 9:
		return False
	res = sorted(r)
	return res[0] == '1' and res[1] == '2' and res[2] == '3' and res[3] == '4' and res[4] == '5' and res[5] == '6' and res[6] == '7' and res[7] == '8' and res[8] == '9'

pandigitals = set()
for a in range(0, 5000):
	for b in range(0, 100):
		if isPandigital(a, b):
			pandigitals.add(a*b)
			print 'Whoop! ' + str(a) + ' x ' + str(b) + ' = ' + str(a*b)

print 'Total: ' + str(sum(pandigitals))

