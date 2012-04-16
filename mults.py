# Sum of all numbers < 1000 that are multiples of 3 or 5 or both
sum = 0
for i in range(1000):
	if i % 3 == 0 or i % 5 == 0:
		sum += i
print sum
