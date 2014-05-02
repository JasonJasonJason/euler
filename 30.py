""" Project Eurler Problem 30:

	Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

	1634 = 1^4 + 6^4 + 3^4 + 4^4
	8208 = 8^4 + 2^4 + 0^4 + 8^4
	9474 = 9^4 + 4^4 + 7^4 + 4^4
	As 1 = 14 is not a sum it is not included.

	The sum of these numbers is 1634 + 8208 + 9474 = 19316.

	Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
"""
	Idea: The max number we're looking at is 9^5 + 9^5... => 59049 + 59049... => At 999,999 we yield a sum of 354,294, which is six digits.
	TL;DR We need to go max 6 digits.
	
	Idea: BRUTE FORCE
	If it takes too long, find a smaller max like 555,555 or something, because 999,999 is too high.
"""

candidate_sum = 0
for i in range(2,999999):
	num = i
	sum = 0
	while num:
		digit = num % 10
		num /= 10
		sum += digit**5

	if sum == i:
		print "Found a candidate: " + str(i)
		candidate_sum += i

print "Resulting sum: " + str(candidate_sum)