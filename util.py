def is_prime(n):
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