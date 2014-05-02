def isprime(n):
    n = abs(int(n)) 
    if n < 3:
    	if n == 2: 
	        return True
        return False

    if n % 2 == 0: # even
        return False
    
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


max = 0
for a in range(-1000, 1000):
	for b in range(-1000, 1000):
		n = 0
		while isprime(n*n + a*n + b):
			n += 1
		if n > max:
			max = n
			print "New max! Found " + str(n) + " primes in a row with: (a * b) = (" + str(a) + " * " + str(b) + ") = " + str(a*b)