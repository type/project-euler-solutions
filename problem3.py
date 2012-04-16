#Find the largest prime factor of a number (600851475143)

#Continually divide the number by its factors
#Each successful factor is exhausted, thus it cannot be a factor in any other "factors" of n
#and so it must be prime

def findprimes(n=600851475143):	
	"""Find the prime factors of an integer"""
	result = []
	
	i = 2
	while i <= n: #if you make this < n you get second highest prime
		flag = 0
		
		while n % i == 0: #eliminate all times this factor occurs
			if flag == 0: #only add the factor the first time you see it
				print "adding", i
				result.append(i)
				flag = 1
			n = n/i
		i = i + 1
	
	return result.pop()

print findprimes()
