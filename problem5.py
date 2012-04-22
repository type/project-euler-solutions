#Smallest positive number that's evenly divisible by all integers between 1 and 20

def smallestWithFactorsInRange(rbegin, rend):
	"""Finds the smallest number divisible by all numbers between rbegin and rend, inclusive"""
	rlist = range(rbegin, rend + 1)
	minNum = 1
	factlist = []

	for i in rlist:			#all the numbers in the range
		factors = findPrimeFactors(i)
		for x in factors:	#all the factors of this particular number
			while factors.count(x) > factlist.count(x):
				factlist.append(x)
	for i in factlist:
		minNum *= i
	return minNum

def findPrimeFactors(n):
	"""Returns a list with all occurrences of all prime factors of n"""
	result = []
	
	i = 2								#first possible prime factor
	while i <= n:
		while n % i == 0: #count all times this factor occurs
			n = n / i
			result.append(i)
		i += 1
	return result


print smallestWithFactorsInRange(1, 20)
