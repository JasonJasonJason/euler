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


def is_palindrome(n):
    n_str = str(n)
    n_str_back = n_str[::-1]

    for i in range(0,len(n_str)):
        if n_str[i] != n_str_back[i]:
            return False
    return True


def dec_to_bin(x):
    return int(bin(x)[2:])