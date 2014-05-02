""" Project Euler Problem 31:

	In England the currency is made up of pound, lb, and pence, p, and there are eight coins in general circulation:

	1p, 2p, 5p, 10p, 20p, 50p, lb1 (100p) and lb2 (200p).
	It is possible to make lb2 in the following way:

	1x100 + 1x50 + 2x20 + 1x5 + 1x2 + 3x1
	How many different ways can 2 pounds be made using any number of coins?
"""
"""
	Theory: Recursion...would be nice, cause I would do just the necessary amount of work. But, BRUTE FORCE!!
"""

count = 1 #2 pounds itself is a way!
for a in range(0,3): #100
	for b in range(0, 5): #50
		if a*100 + b*50 < 201:
			for c in range(0, 11): #20
				if a*100 + b*50 + c*20 < 201:
					for d in range(0, 21): #10
						if a*100 + b*50 + c*20 + d*10 < 201:
							for e in range(0, 41): #5
								if a*100 + b*50 + c*20 + d*10 + e*5 < 201:
									for f in range(0, 101): #2
										if a*100 + b*50 + c*20 + d*10 + e*5 + f*2 < 201:
											for g in range(0, 201): #1
												if a*100 + b*50 + c*20 + d*10 + e*5 + f*2 + g*1 == 200:
													count += 1

print "Total ways to make two pounds: " + str(count)