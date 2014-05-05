from util import *


max = 0
for a in range(-1000, 1000):
	for b in range(-1000, 1000):
		n = 0
		while is_prime(n*n + a*n + b):
			n += 1
		if n > max:
			max = n
			print "New max! Found " + str(n) + " primes in a row with: (a * b) = (" + str(a) + " * " + str(b) + ") = " + str(a*b)