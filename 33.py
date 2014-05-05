""" Project Euler Problem 33:

	The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

	We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

	There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

	If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
"""
	Thoughts: 
	* a/b for a,b in [10,99] is not many cases to check.
	* For each combination, check if a/b is equal to a[0]/b[0], a[1]/b[1], a[0]/b[1], or a[1]/b[0]
	* I'll worry about lowest common terms in a minute.
"""

def gcd(a,b):
	(a,b) = (max(a,b), min(a,b))
	while b > 0:
		(a,b) = (b, a%b)
	return a

numerator   = 1
denominator = 1

for b in range(10,100):
	for a in range(10,b):
		quotient = float(a)/float(b)
		
		a0 = float(a%10)
		a1 = float(a/10)
		b0 = float(b%10)
		b1 = float(b/10)

		if a1 == b1 != 0 and b0 != 0:
			if quotient == float(a0)/float(b0):
				print 'Found one! ' + str(a) + " / " + str(b)
				numerator   *= a
				denominator *= b
		if a0 == b1 != 0 and b0 != 0:
			if quotient == float(a1)/float(b0):
				print 'Found one! ' + str(a) + " / " + str(b)
				numerator   *= a
				denominator *= b
		if a0 == b0 != 0 and b1 != 0:
			if quotient == float(a1)/float(b1):
				print 'Found one! ' + str(a) + " / " + str(b)
				numerator   *= a
				denominator *= b
		if a1 == b0 != 0 and b1 != 0:
			if quotient == float(a0)/float(b1):
				print 'Found one! ' + str(a) + " / " + str(b)
				numerator   *= a
				denominator *= b

final_gcd = gcd(numerator, denominator)
print str(numerator) + " / " + str(denominator) + " =",
numerator   /= final_gcd
denominator /= final_gcd
print str(numerator) + " / " + str(denominator)
print 'After finding the product of all 4 fractions, and reducing to lowest terms, the denominator is: ' + str(denominator)